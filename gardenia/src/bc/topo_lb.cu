// Copyright (c) 2020 MIT
// Xuhao Chen <cxh@mit.edu>
#include "bc.h"
#include "cuda_launch_config.hpp"
#include "cutil_subset.h"
#include "worklistc.h"
#include "timer.h"
#include <vector>
#include <cub/cub.cuh>
#include <thrust/extrema.h>
#include <thrust/execution_policy.h>

typedef cub::BlockScan<int, BLOCK_SIZE> BlockScan;
typedef cub::BlockReduce<ScoreT, BLOCK_SIZE> BlockReduce;

__global__ void initialize(int m, int source, 
                           ScoreT *scores, int *path_counts, 
                           int *depths, ScoreT *deltas, 
                           bool *visited, bool *expanded) {
	int id = blockIdx.x * blockDim.x + threadIdx.x;
	if (id < m) {
		scores[id] = 0;
		deltas[id] = 0;
		expanded[id] = false;
		if(id == source) {
			visited[id] = true;
			path_counts[id] = 1;
			depths[id] = 0;
		} else {
			visited[id] = false;
			path_counts[id] = 0;
			depths[id] = -1;
		}
	}
}

__global__ void forward_base(int m, const uint64_t *row_offsets, 
                             const IndexT *column_indices, 
                             int *depths, int *path_counts, 
                             int depth, bool *visited, bool *expanded) {
	int src = blockIdx.x * blockDim.x + threadIdx.x;
	if(src < m && visited[src] && !expanded[src]) {
		int row_begin = row_offsets[src];
		int row_end = row_offsets[src+1];
		int value = path_counts[src];
		for (int offset = row_begin; offset < row_end; ++ offset) {
			int dst = column_indices[offset];
			if (depths[dst] == -1) {
				depths[dst] = depth;
			}
			if (depths[dst] == depth) {
				atomicAdd(&path_counts[dst], value);
			}
		}
	}
}

__device__ __forceinline__ void process_edge(int value, int depth, int dst,
                                             int *path_counts, int *depths) {
	if(depths[dst] == -1) {
		depths[dst] = depth;
	}
	if (depths[dst] == depth) {
		atomicAdd(&path_counts[dst], value);
	}
}

__device__ __forceinline__ void expandByCta(int m, const uint64_t *row_offsets, 
                                            const IndexT *column_indices, 
                                            int *path_counts, int *depths, 
                                            int depth, bool *visited, bool *expanded) {
	int src = blockIdx.x * blockDim.x + threadIdx.x;
	__shared__ int owner;
	__shared__ int sh_src;
	owner = -1;
	int size = 0;
	if(src < m && visited[src] && !expanded[src]) {
		size = row_offsets[src+1] - row_offsets[src];
	}
	while(true) {
		if(size > BLOCK_SIZE)
			owner = threadIdx.x;
		__syncthreads();
		if(owner == -1)
			break;
		__syncthreads();
		if(owner == threadIdx.x) {
			sh_src = src;
			expanded[src] = 1;
			owner = -1;
			size = 0;
		}
		__syncthreads();
		int row_begin = row_offsets[sh_src];
		int row_end = row_offsets[sh_src+1];
		int neighbor_size = row_end - row_begin;
		int num = ((neighbor_size + blockDim.x - 1) / blockDim.x) * blockDim.x;
		int value = path_counts[sh_src];
		for(int i = threadIdx.x; i < num; i += blockDim.x) {
			int offset = row_begin + i;
			int dst = column_indices[offset];
			if(i < neighbor_size) {
				process_edge(value, depth, dst, path_counts, depths);
			}
		}
	}
}

__device__ __forceinline__ unsigned LaneId() {
	unsigned ret;
	asm("mov.u32 %0, %laneid;" : "=r"(ret));
	return ret;
}

__device__ __forceinline__ void expandByWarp(int m, const uint64_t *row_offsets, 
                                             const IndexT *column_indices, 
                                             int *path_counts, int *depths, 
                                             int depth, bool *visited, bool *expanded) {
	int src = blockIdx.x * blockDim.x + threadIdx.x;
	int warp_id = threadIdx.x >> LOG_WARP_SIZE;
	unsigned lane_id = LaneId();
	__shared__ int owner[NUM_WARPS];
	__shared__ int sh_src[NUM_WARPS];
	owner[warp_id] = -1;
	int size = 0;
	if(src < m && visited[src] && !expanded[src]) {
		size = row_offsets[src+1] - row_offsets[src];
	}
	while(__any_sync(0xFFFFFFFF, size) >= WARP_SIZE) {
		if(size >= WARP_SIZE)
			owner[warp_id] = lane_id;
		if(owner[warp_id] == lane_id) {
			sh_src[warp_id] = src;
			expanded[src] = true;
			owner[warp_id] = -1;
			size = 0;
		}
		int winner = sh_src[warp_id];
		int row_begin = row_offsets[winner];
		int row_end = row_offsets[winner + 1];
		int neighbor_size = row_end - row_begin;
		int num = ((neighbor_size + WARP_SIZE - 1) / WARP_SIZE) * WARP_SIZE;
		int value = path_counts[winner];
		for(int i = lane_id; i < num; i+= WARP_SIZE) {
			int edge = row_begin + i;
			int dst = column_indices[edge];
			if(i < neighbor_size) {
				process_edge(value, depth, dst, path_counts, depths);
			}
		}
	}
}

__global__ void forward_lb(int m, const uint64_t *row_offsets, 
                           const IndexT *column_indices, 
                           int *depths, int *path_counts, int depth, 
                           bool *visited, bool *expanded) {
	//TODO: a bug exists in expandByCta
	//expandByCta(m, row_offsets, column_indices, path_counts, depths, depth, visited, expanded, changed);
	expandByWarp(m, row_offsets, column_indices, path_counts, depths, depth, visited, expanded);
	int src = blockIdx.x * blockDim.x + threadIdx.x;
	const int SCRATCHSIZE = BLOCK_SIZE;
	__shared__ BlockScan::TempStorage temp_storage;
	__shared__ int gather_offsets[SCRATCHSIZE];
	__shared__ int srcsrc[SCRATCHSIZE];
	__shared__ int values[BLOCK_SIZE];
	gather_offsets[threadIdx.x] = 0;
	int neighbor_size = 0;
	int neighbor_offset = 0;
	int scratch_offset = 0;
	int total_edges = 0;
	if(src < m && visited[src] && !expanded[src]) { // visited but not expanded
		expanded[src] = true;
		neighbor_offset = row_offsets[src];
		neighbor_size = row_offsets[src+1] - neighbor_offset;
		values[threadIdx.x] = path_counts[src];
	}
	BlockScan(temp_storage).ExclusiveSum(neighbor_size, scratch_offset, total_edges);
	int done = 0;
	int neighbors_done = 0;
	while(total_edges > 0) {
		__syncthreads();
		int i;
		for(i = 0; neighbors_done + i < neighbor_size && (scratch_offset + i - done) < SCRATCHSIZE; i++) {
			gather_offsets[scratch_offset + i - done] = neighbor_offset + neighbors_done + i;
			srcsrc[scratch_offset + i - done] = threadIdx.x;
		}
		neighbors_done += i;
		scratch_offset += i;
		__syncthreads();
		if(threadIdx.x < total_edges) {
			int offset = gather_offsets[threadIdx.x];
			int dst = column_indices[offset];
			process_edge(values[srcsrc[threadIdx.x]], depth, dst, path_counts, depths);
		}
		total_edges -= BLOCK_SIZE;
		done += BLOCK_SIZE;
	}
}

// Dependency accumulation by back propagation
__global__ void reverse_base(int num, const uint64_t *row_offsets, 
                             const IndexT *column_indices, int start, 
                             int *frontiers, ScoreT *scores, int *path_counts, 
                             int *depths, int depth, ScoreT *deltas) {
	int id = blockIdx.x * blockDim.x + threadIdx.x;
	if(id < num) {
		int src = frontiers[start + id];
		int row_begin = row_offsets[src];
		int row_end = row_offsets[src+1];
		ScoreT delta_src = 0;
		for (int offset = row_begin; offset < row_end; ++ offset) {
			int dst = column_indices[offset];
			if(depths[dst] == depth + 1) {
				delta_src += static_cast<ScoreT>(path_counts[src]) / 
					static_cast<ScoreT>(path_counts[dst]) * (1 + deltas[dst]);
			}
		}
		deltas[src] = delta_src;
		scores[src] += deltas[src];
	}
}

__device__ __forceinline__ void reverse_expand_cta(int num, 
                                                   const uint64_t *row_offsets, 
                                                   const IndexT *column_indices, 
                                                   int start, IndexT *frontiers, 
                                                   ScoreT *scores, const int *path_counts, 
                                                   int *depths, int depth, ScoreT *deltas) {
	int tid = blockIdx.x * blockDim.x + threadIdx.x;
	__shared__ typename BlockReduce::TempStorage temp_storage;
	int src = 0;
	int size = 0;
	__shared__ int owner;
	__shared__ int sh_src;
	owner = -1;
	if(tid < num) {
		src = frontiers[start + tid];
		size = row_offsets[src+1] - row_offsets[src];
	}
	while(true) {
		if(size > BLOCK_SIZE)
			owner = threadIdx.x;
		__syncthreads();
		if(owner == -1) break;
		__syncthreads();
		if(owner == threadIdx.x) {
			sh_src = src;
			frontiers[start + tid] = -1;
			owner = -1;
			size = 0;
		}
		__syncthreads();
		int row_begin = row_offsets[sh_src];
		int row_end = row_offsets[sh_src+1];
		int neighbor_size = row_end - row_begin;
		int num = ((neighbor_size + blockDim.x - 1) / blockDim.x) * blockDim.x;
		int count = path_counts[sh_src];
		ScoreT sum = 0;
		for(int i = threadIdx.x; i < num; i += blockDim.x) {
			int offset = row_begin + i;
			if(i < neighbor_size) {
				int dst = column_indices[offset];
				if(depths[dst] == depth + 1) {
					ScoreT value = static_cast<ScoreT>(count) /
						static_cast<ScoreT>(__ldg(path_counts+dst)) * (1 + deltas[dst]);
					sum += value;
				}
			}
		}
		ScoreT delta_src = BlockReduce(temp_storage).Sum(sum);
		if(threadIdx.x == 0) {
			deltas[sh_src]  = delta_src;
			scores[sh_src] += delta_src;
		}
	}
}

__device__ __forceinline__ void reverse_expand_warp(int num, 
                                                    const uint64_t *row_offsets, 
                                                    const IndexT *column_indices, 
                                                    int start, IndexT *frontiers, 
                                                    ScoreT *scores, const int *path_counts, 
                                                    int *depths, int depth, ScoreT *deltas) {
	unsigned tid = blockIdx.x * blockDim.x + threadIdx.x;
	unsigned warp_id = threadIdx.x >> LOG_WARP_SIZE;
	unsigned lane_id = LaneId();
	__shared__ int owner[NUM_WARPS];
	__shared__ int sh_src[NUM_WARPS];
	__shared__ ScoreT sdata[BLOCK_SIZE + 16];
	owner[warp_id] = -1;
	int size = 0;
	int src = -1;
	if(tid < num) {
		src = frontiers[start + tid];
		if(src != -1) {
			size = row_offsets[src+1] - row_offsets[src];
		}
	}
	while(__any_sync(0xFFFFFFFF, size) >= WARP_SIZE) {
		if(size >= WARP_SIZE)
			owner[warp_id] = lane_id;
		if(owner[warp_id] == lane_id) {
			sh_src[warp_id] = src;
			frontiers[start + tid] = -1;
			owner[warp_id] = -1;
			size = 0;
		}
		int winner = sh_src[warp_id];
		int row_begin = row_offsets[winner];
		int row_end = row_offsets[winner+1];
		int neighbor_size = row_end - row_begin;
		int num = ((neighbor_size + WARP_SIZE - 1) / WARP_SIZE) * WARP_SIZE;
		int count = path_counts[winner];
		ScoreT sum = 0;
		for(int i = lane_id; i < num; i+= WARP_SIZE) {
			int edge = row_begin + i;
			if(i < neighbor_size) {
				int dst = column_indices[edge];
				if(depths[dst] == depth + 1) {
					ScoreT value = static_cast<ScoreT>(count) /
						static_cast<ScoreT>(__ldg(path_counts+dst)) * (1 + deltas[dst]);
					sum += value;
				}
			}
		}
		sdata[threadIdx.x] = sum; __syncthreads();
		sdata[threadIdx.x] = sum = sum + sdata[threadIdx.x + 16]; __syncthreads();
		sdata[threadIdx.x] = sum = sum + sdata[threadIdx.x +  8]; __syncthreads();
		sdata[threadIdx.x] = sum = sum + sdata[threadIdx.x +  4]; __syncthreads();
		sdata[threadIdx.x] = sum = sum + sdata[threadIdx.x +  2]; __syncthreads();
		sdata[threadIdx.x] = sum = sum + sdata[threadIdx.x +  1]; __syncthreads();
		if(lane_id == 0) {
			deltas[winner]  = sdata[threadIdx.x];
			scores[winner] += sdata[threadIdx.x];
		}
	}
}

__global__ void reverse_lb(int num, const uint64_t *row_offsets, 
                           const IndexT *column_indices, 
                           int start, IndexT *frontiers, 
                           ScoreT *scores, const int *path_counts, 
                           int *depths, int depth, ScoreT *deltas) {
	reverse_expand_cta(num, row_offsets, column_indices, start, frontiers, scores, path_counts, depths, depth, deltas);
	reverse_expand_warp(num, row_offsets, column_indices, start, frontiers, scores, path_counts, depths, depth, deltas);
	int tid = blockIdx.x * blockDim.x + threadIdx.x;
	int tx = threadIdx.x;
	__shared__ BlockScan::TempStorage temp_storage;
	__shared__ int gather_offsets[BLOCK_SIZE];
	//__shared__ int srcs[BLOCK_SIZE];
	__shared__ int idx[BLOCK_SIZE];
	__shared__ int sh_counts[BLOCK_SIZE];
	__shared__ ScoreT sh_deltas[BLOCK_SIZE];
	gather_offsets[tx] = 0;
	//srcs[tx] = 0;
	idx[tx] = 0;
	sh_counts[tx] = 0;
	sh_deltas[tx] = 0;
	int neighbor_size = 0;
	int neighbor_offset = 0;
	int scratch_offset = 0;
	int total_edges = 0;
	int src = -1;
	if(tid < num) {
		src = frontiers[start + tid];
		if(src != -1) {
			neighbor_offset = row_offsets[src];
			neighbor_size = row_offsets[src+1] - neighbor_offset;
			sh_counts[tx] = path_counts[src];
		}
	}
	BlockScan(temp_storage).ExclusiveSum(neighbor_size, scratch_offset, total_edges);
	int done = 0;
	int neighbors_done = 0;
	while(total_edges > 0) {
		__syncthreads();
		int i;
		for(i = 0; neighbors_done + i < neighbor_size && (scratch_offset + i - done) < BLOCK_SIZE; i++) {
			int j = scratch_offset + i - done;
			gather_offsets[j] = neighbor_offset + neighbors_done + i;
			//srcs[j] = src;
			idx[j] = tx;
		}
		neighbors_done += i;
		scratch_offset += i;
		__syncthreads();
		if(tx < total_edges) {
			int offset = gather_offsets[tx];
			int dst = column_indices[offset];
			if(depths[dst] == depth + 1) {
				ScoreT value = static_cast<ScoreT>(sh_counts[idx[tx]]) / 
					static_cast<ScoreT>(__ldg(path_counts+dst)) * (1 + deltas[dst]);
				atomicAdd(&sh_deltas[idx[tx]], value); 
			}
		}
		total_edges -= BLOCK_SIZE;
		done += BLOCK_SIZE;
	}
	__syncthreads();
	if(src != -1) {
		deltas[src]  = sh_deltas[tx];
		scores[src] += sh_deltas[tx];
	}
}

__global__ void reverse_warp(int num, const uint64_t *row_offsets, 
                             const IndexT *column_indices, int start, 
                             int *frontiers, ScoreT *scores, 
                             int *path_counts, int *depths, 
                             int depth, ScoreT *deltas) {
	__shared__ int ptrs[BLOCK_SIZE/WARP_SIZE][2];
	__shared__ ScoreT sdata[BLOCK_SIZE + 16];                       // padded to avoid reduction conditionals

	const int thread_id   = BLOCK_SIZE * blockIdx.x + threadIdx.x;  // global thread index
	const int thread_lane = threadIdx.x & (WARP_SIZE-1);            // thread index within the warp
	const int warp_id     = thread_id   / WARP_SIZE;                // global warp index
	const int warp_lane   = threadIdx.x / WARP_SIZE;                // warp index within the CTA
	const int num_warps   = (BLOCK_SIZE / WARP_SIZE) * gridDim.x;   // total number of active warps

	for(int index = warp_id; index < num; index += num_warps) {
		int src = frontiers[start + index];
		// use two threads to fetch Ap[row] and Ap[row+1]
		// this is considerably faster than the straightforward version
		if(thread_lane < 2)
			ptrs[warp_lane][thread_lane] = row_offsets[src + thread_lane];
		const int row_begin = ptrs[warp_lane][0];                   //same as: row_start = row_offsets[row];
		const int row_end   = ptrs[warp_lane][1];                   //same as: row_end   = row_offsets[row+1];
		ScoreT sum = 0;
		for(int offset = row_begin + thread_lane; offset < row_end; offset += WARP_SIZE) {
			int dst = column_indices[offset];
			if(depths[dst] == depth + 1) {
				sum += static_cast<ScoreT>(path_counts[src]) / 
					static_cast<ScoreT>(path_counts[dst]) * (1 + deltas[dst]);
			}
		}
		// store local sum in shared memory
		sdata[threadIdx.x] = sum; __syncthreads();

		// reduce local sums to row sum
		sdata[threadIdx.x] = sum = sum + sdata[threadIdx.x + 16]; __syncthreads();
		sdata[threadIdx.x] = sum = sum + sdata[threadIdx.x +  8]; __syncthreads();
		sdata[threadIdx.x] = sum = sum + sdata[threadIdx.x +  4]; __syncthreads();
		sdata[threadIdx.x] = sum = sum + sdata[threadIdx.x +  2]; __syncthreads();
		sdata[threadIdx.x] = sum = sum + sdata[threadIdx.x +  1]; __syncthreads();
		if (thread_lane == 0) {
			deltas[src] += sdata[threadIdx.x];
			scores[src] += deltas[src];
		}
	}
}

__global__ void update(int m, bool *visited, int *depths, 
                       int *nitems, int *queue, 
                       int queue_len, bool *changed) {
	int id = blockIdx.x * blockDim.x + threadIdx.x;
	if (id < m && depths[id] != -1 && !visited[id]) {
		visited[id] = true;
		int pos = atomicAdd(nitems, 1);
		queue[queue_len + pos] = id;
		*changed = true;
	}
}

__global__ void bc_normalize(int m, ScoreT *scores, ScoreT max_score) {
	int tid = blockIdx.x * blockDim.x + threadIdx.x;
	if (tid < m) scores[tid] = scores[tid] / (max_score);
}

void BCSolver(Graph &g, int source, ScoreT *h_scores) {
  auto m = g.V();
  auto nnz = g.E();
  auto h_row_offsets = g.out_rowptr();
  auto h_column_indices = g.out_colidx();	
  //print_device_info(0);
  uint64_t *d_row_offsets;
  VertexId *d_column_indices;
  CUDA_SAFE_CALL(cudaMalloc((void **)&d_row_offsets, (m + 1) * sizeof(uint64_t)));
  CUDA_SAFE_CALL(cudaMalloc((void **)&d_column_indices, nnz * sizeof(VertexId)));
  CUDA_SAFE_CALL(cudaMemcpy(d_row_offsets, h_row_offsets, (m + 1) * sizeof(uint64_t), cudaMemcpyHostToDevice));
  CUDA_SAFE_CALL(cudaMemcpy(d_column_indices, h_column_indices, nnz * sizeof(VertexId), cudaMemcpyHostToDevice));

	ScoreT *d_scores, *d_deltas;
	CUDA_SAFE_CALL(cudaMalloc((void **)&d_scores, sizeof(ScoreT) * m));
	CUDA_SAFE_CALL(cudaMalloc((void **)&d_deltas, sizeof(ScoreT) * m));
	int *d_path_counts, *d_depths, *d_frontiers;
	CUDA_SAFE_CALL(cudaMalloc((void **)&d_path_counts, sizeof(int) * m));
	CUDA_SAFE_CALL(cudaMalloc((void **)&d_depths, sizeof(int) * m));
	CUDA_SAFE_CALL(cudaMalloc((void **)&d_frontiers, sizeof(int) * (m+1)));
	bool *d_changed, h_changed, *d_visited, *d_expanded;
	CUDA_SAFE_CALL(cudaMalloc((void **)&d_changed, sizeof(bool)));
	CUDA_SAFE_CALL(cudaMalloc((void **)&d_visited, m * sizeof(bool)));
	CUDA_SAFE_CALL(cudaMalloc((void **)&d_expanded, m * sizeof(bool)));
	int *d_nitems, h_nitems = 1;
	CUDA_SAFE_CALL(cudaMalloc((void **)&d_nitems, sizeof(int)));

	int zero = 0;
	int depth = 0;
	int frontiers_len = 0;
	vector<int> depth_index;
	depth_index.push_back(0);
	int nthreads = BLOCK_SIZE;
	int nblocks = (m - 1) / nthreads + 1;
	initialize <<<nblocks, nthreads>>> (m, source, d_scores, d_path_counts, d_depths, d_deltas, d_visited, d_expanded);
	CudaTest("initializing failed");
	CUDA_SAFE_CALL(cudaMemcpy(&d_frontiers[0], &source, sizeof(int), cudaMemcpyHostToDevice));

#ifdef REVERSE_WARP
	cudaDeviceProp deviceProp;
	CUDA_SAFE_CALL(cudaGetDeviceProperties(&deviceProp, 0));
	const int nSM = deviceProp.multiProcessorCount;
	const int max_blocks_per_SM = maximum_residency(reverse_warp, nthreads, 0);
	const int max_blocks = max_blocks_per_SM * nSM;
#endif
	CUDA_SAFE_CALL(cudaDeviceSynchronize());
	printf("Launching CUDA BC solver (%d CTAs/SM, %d threads/CTA) ...\n", nblocks, nthreads);

	Timer t;
	t.Start();
	do {
		depth++;
		h_changed = false;
		//printf("iteration=%d, frontire_size=%d\n", depth, h_nitems);
		CUDA_SAFE_CALL(cudaMemcpy(d_changed, &h_changed, sizeof(bool), cudaMemcpyHostToDevice));
		CUDA_SAFE_CALL(cudaMemcpy(d_nitems, &zero, sizeof(int), cudaMemcpyHostToDevice));
		frontiers_len += h_nitems;
		depth_index.push_back(frontiers_len);
		forward_lb<<<nblocks, nthreads>>>(m, d_row_offsets, d_column_indices, d_depths, d_path_counts, depth, d_visited, d_expanded);
		CudaTest("solving bc_forward failed");
		update<<<nblocks, nthreads>>>(m, d_visited, d_depths, d_nitems, d_frontiers, frontiers_len, d_changed);
		CudaTest("solving bc_update failed");
		CUDA_SAFE_CALL(cudaMemcpy(&h_changed, d_changed, sizeof(bool), cudaMemcpyDeviceToHost));
		CUDA_SAFE_CALL(cudaMemcpy(&h_nitems, d_nitems, sizeof(int), cudaMemcpyDeviceToHost));
	} while (h_changed);
	CUDA_SAFE_CALL(cudaDeviceSynchronize());
	for (int d = depth_index.size() - 2; d >= 0; d--) {
		h_nitems = depth_index[d+1] - depth_index[d];
		//thrust::sort(thrust::device, d_frontiers+depth_index[d], d_frontiers+depth_index[d+1]);
		//printf("Reverse: depth=%d, frontier_size=%d\n", d, h_nitems);
#ifdef REVERSE_WARP
		nblocks = std::min(max_blocks, DIVIDE_INTO(h_nitems, WARPS_PER_BLOCK));
		reverse_warp<<<nblocks, nthreads>>>(h_nitems, d_row_offsets, d_column_indices, depth_index[d], d_frontiers, d_scores, d_path_counts, d_depths, d, d_deltas);
#else
		nblocks = (h_nitems - 1) / nthreads + 1;
		reverse_lb<<<nblocks, nthreads>>>(h_nitems, d_row_offsets, d_column_indices, depth_index[d], d_frontiers, d_scores, d_path_counts, d_depths, d, d_deltas);
#endif

		CudaTest("solving kernel reverse failed");
	}
	ScoreT *d_max_score;
	d_max_score = thrust::max_element(thrust::device, d_scores, d_scores + m);
	ScoreT h_max_score;
	CUDA_SAFE_CALL(cudaMemcpy(&h_max_score, d_max_score, sizeof(ScoreT), cudaMemcpyDeviceToHost));
	nthreads = 512;
	nblocks = (m - 1) / nthreads + 1;
	bc_normalize<<<nblocks, nthreads>>>(m, d_scores, h_max_score);
	CUDA_SAFE_CALL(cudaDeviceSynchronize());
	t.Stop();

	printf("\titerations = %d.\n", depth);
	printf("\truntime [cuda_topo_lb] = %f ms.\n", t.Millisecs());
	CUDA_SAFE_CALL(cudaMemcpy(h_scores, d_scores, sizeof(ScoreT) * m, cudaMemcpyDeviceToHost));
	CUDA_SAFE_CALL(cudaFree(d_path_counts));
	CUDA_SAFE_CALL(cudaFree(d_depths));
	CUDA_SAFE_CALL(cudaFree(d_deltas));
	CUDA_SAFE_CALL(cudaFree(d_frontiers));
	CUDA_SAFE_CALL(cudaFree(d_row_offsets));
	CUDA_SAFE_CALL(cudaFree(d_column_indices));
}

