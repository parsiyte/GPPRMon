// Copyright (c) 2019, Xuhao Chen
#include "kcl.h"
#include "timer.h"
#include "cutil_subset.h"
#include "cuda_launch_config.hpp"
#include <cub/cub.cuh>
#define USE_SIMPLE
#define USE_BASE_TYPES
#include "gpu_mining/miner.cuh"
#include <thrust/scan.h>
#include <thrust/execution_policy.h>
typedef unsigned long long AccType;
typedef uint64_t emb_index_t;

#define USE_SHM
typedef cub::BlockScan<int, BLOCK_SIZE> BlockScan;
typedef cub::BlockReduce<AccType, BLOCK_SIZE> BlockReduce;

__global__ void extend_alloc(size_t begin, size_t end, 
                             unsigned level, unsigned max_size, 
                             GraphGPU graph, EmbeddingList emb_list, 
                             emb_index_t *num_new_emb, AccType *total) {
  unsigned tid = threadIdx.x;
  unsigned pos = blockIdx.x * blockDim.x + threadIdx.x;
  __shared__ typename BlockReduce::TempStorage temp_storage;
#ifdef USE_SHM
  __shared__ IndexT emb[BLOCK_SIZE][MAX_SIZE];
#else
  IndexT emb[MAX_SIZE];
#endif
  AccType local_num = 0;
  if(pos < end - begin) {
#ifdef USE_SHM
    emb_list.get_embedding(level, begin + pos, emb[tid]);
#else
    emb_list.get_embedding(level, begin + pos, emb);
#endif
    auto vid = emb_list.get_vid(level, begin + pos);
    auto row_begin = graph.edge_begin(vid);
    auto row_end = graph.edge_end(vid);
    num_new_emb[pos] = 0;
    for (auto e = row_begin; e < row_end; e++) {
      auto dst = graph.getEdgeDst(e);
#ifdef USE_SHM
      if (is_all_connected_dag(dst, emb[tid], level, graph)) {
#else
      if (is_all_connected_dag(dst, emb, level, graph)) {
#endif
        if (level < max_size-2) num_new_emb[pos] ++;
        else local_num += 1;
      }
    }
  }
  AccType block_num = BlockReduce(temp_storage).Sum(local_num);
  if(threadIdx.x == 0) atomicAdd(total, block_num);
}

__global__ void extend_alloc_lb(size_t begin, size_t end, unsigned level, unsigned max_size, 
                                GraphGPU graph, EmbeddingList emb_list, 
                                emb_index_t *num_new_emb, AccType *total) {
  //expandByCta(m, row_offsets, column_indices, depths, in_queue, out_queue, depth);
  //expandByWarp(m, row_offsets, column_indices, depths, in_queue, out_queue, depth);
  unsigned tid = threadIdx.x;
  unsigned base_id = blockIdx.x * blockDim.x;
  unsigned pos = blockIdx.x * blockDim.x + threadIdx.x;
  __shared__ typename BlockReduce::TempStorage reduce_storage;

  const unsigned SCRATCHSIZE = BLOCK_SIZE;
  __shared__ BlockScan::TempStorage temp_storage;
  __shared__ int gather_offsets[SCRATCHSIZE];
  __shared__ unsigned src[SCRATCHSIZE];
  __shared__ IndexT emb[BLOCK_SIZE][MAX_SIZE];

  gather_offsets[threadIdx.x] = 0;
  int neighbor_size = 0;
  int neighbor_offset = 0;
  int scratch_offset = 0;
  int total_edges = 0;
  IndexT row_begin = 0;
  IndexT row_end = 0;

  AccType local_num = 0;
  if (pos < end - begin) {
    //emb_list.get_embedding(level, begin + pos, emb);
    emb_list.get_embedding(level, begin + pos, emb[tid]);
    auto vid = emb_list.get_vid(level, begin + pos);
    row_begin = graph.edge_begin(vid);
    row_end = graph.edge_end(vid);
    num_new_emb[pos] = 0;
    neighbor_offset = row_begin;
    neighbor_size = row_end - row_begin;
  }
  BlockScan(temp_storage).ExclusiveSum(neighbor_size, scratch_offset, total_edges);
  int done = 0;
  int neighbors_done = 0;
  while(total_edges > 0) {
    __syncthreads();
    int i;
    for(i = 0; neighbors_done + i < neighbor_size && (scratch_offset + i - done) < SCRATCHSIZE; i++) {
      gather_offsets[scratch_offset + i - done] = neighbor_offset + neighbors_done + i;
      src[scratch_offset + i - done] = tid;
    }
    neighbors_done += i;
    scratch_offset += i;
    __syncthreads();
    if(tid < total_edges) {
      auto e = gather_offsets[tid];
      auto dst = graph.getEdgeDst(e);
      auto idx = src[tid];
      if (is_all_connected_dag(dst, emb[idx], level, graph)) {
        if (level < max_size-2) atomicAdd((AccType*)(num_new_emb+base_id+idx), 1);
        else local_num += 1;
      }
    }
    total_edges -= BLOCK_SIZE;
    done += BLOCK_SIZE;
  }
  AccType block_num = BlockReduce(reduce_storage).Sum(local_num);
  if (tid == 0) atomicAdd(total, block_num);
}


__global__ void extend_insert(size_t begin, size_t end, unsigned level, 
                              GraphGPU graph, EmbeddingList emb_list, emb_index_t *indices) {
  unsigned tid = threadIdx.x;
  unsigned pos = blockIdx.x * blockDim.x + threadIdx.x;
#ifdef USE_SHM
  __shared__ IndexT emb[BLOCK_SIZE][MAX_SIZE];
#else
  IndexT emb[MAX_SIZE];
#endif
  if(pos < end - begin) {
#ifdef USE_SHM
    emb_list.get_embedding(level, begin + pos, emb[tid]);
#else
    emb_list.get_embedding(level, begin + pos, emb);
#endif
    IndexT vid = emb_list.get_vid(level, begin + pos);
    IndexT start = indices[pos];
    IndexT row_begin = graph.edge_begin(vid);
    IndexT row_end = graph.edge_end(vid);
    for (IndexT e = row_begin; e < row_end; e++) {
      IndexT dst = graph.getEdgeDst(e);
#ifdef USE_SHM
      if (is_all_connected_dag(dst, emb[tid], level, graph)) {
#else
      if (is_all_connected_dag(dst, emb, level, graph)) {
#endif
        emb_list.set_idx(level+1, start, begin + pos);
        emb_list.set_vid(level+1, start++, dst);
      }
    }
  }
}

#define N_CHUNK 1
void KclSolver(Graph &g, unsigned k, AccType &total) {
  //print_device_info(0);
  size_t m = g.num_vertices();
  size_t nnz = g.num_edges();
  int nthreads = BLOCK_SIZE;
  int nblocks = DIVIDE_INTO(m, nthreads);
  CUDA_Context_Mining cuda_ctx;
  cuda_ctx.hg = &g;
  cuda_ctx.build_graph_gpu();
  cuda_ctx.emb_list.init(nnz, k);
  init_gpu_dag<<<nblocks, nthreads>>>(m, cuda_ctx.gg, cuda_ctx.emb_list);
  CUDA_SAFE_CALL(cudaDeviceSynchronize());
  AccType h_total = 0, *d_total;
  AccType zero = 0;
  size_t chunk_length = (nnz - 1) / N_CHUNK + 1;
  CUDA_SAFE_CALL(cudaMalloc((void **)&d_total, sizeof(AccType)));
  printf("Launching CUDA TC solver (%d CTAs, %d threads/CTA) ...\n", nblocks, nthreads);

  Timer t;
  t.Start();
  std::cout << "number of single-edge embeddings: " << nnz << "\n";
  for (size_t cid = 0; cid < N_CHUNK; cid ++) {
    size_t chunk_begin = cid * chunk_length;
    size_t chunk_end = std::min((cid+1) * chunk_length, nnz);
    size_t cur_size = chunk_end-chunk_begin;
    std::cout << "Processing the " << cid << " chunk of " << cur_size << " edges\n";

    unsigned level = 1;
    while (1) {
      emb_index_t *num_new_emb;
      size_t num_emb = cuda_ctx.emb_list.size();
      size_t begin = 0, end = num_emb;
      if (level == 1) { begin = chunk_begin; end = chunk_end; num_emb = end - begin; }
      std::cout << "\t number of embeddings in level " << level << ": " << num_emb << "\n";
      CUDA_SAFE_CALL(cudaMalloc((void **)&num_new_emb, sizeof(emb_index_t) * (num_emb+1)));
      CUDA_SAFE_CALL(cudaMemset(num_new_emb, 0, sizeof(emb_index_t) * (num_emb+1)));
      nblocks = (num_emb-1)/nthreads+1;
      CUDA_SAFE_CALL(cudaMemcpy(d_total, &zero, sizeof(AccType), cudaMemcpyHostToDevice));
      //std::cout << "\t Starting Extend_alloc ...\n";
      extend_alloc<<<nblocks, nthreads>>>(begin, end, level, k, cuda_ctx.gg, cuda_ctx.emb_list, num_new_emb, d_total);
      //extend_alloc_lb<<<nblocks, nthreads>>>(begin, end, level, k, cuda_ctx.gg, cuda_ctx.emb_list, (unsigned long long *)num_new_emb, d_total);
      CUDA_SAFE_CALL(cudaMemcpy(&h_total, d_total, sizeof(AccType), cudaMemcpyDeviceToHost));
      total += h_total;
      CudaTest("solving extend alloc failed");
      //std::cout << "\t Extend_alloc Done\n";
      if (level == k-2) {
        CUDA_SAFE_CALL(cudaFree(num_new_emb));
        break; 
      }
      emb_index_t *indices;
      CUDA_SAFE_CALL(cudaMalloc((void **)&indices, sizeof(emb_index_t) * (num_emb+1)));
      thrust::exclusive_scan(thrust::device, num_new_emb, num_new_emb+num_emb+1, indices);
      //std::cout << "\t PrefixSum Done\n";
      CUDA_SAFE_CALL(cudaFree(num_new_emb));
      size_t new_size;
      CUDA_SAFE_CALL(cudaMemcpy(&new_size, &indices[num_emb], sizeof(unsigned), cudaMemcpyDeviceToHost));
      std::cout << "\t number of new embeddings: " << new_size << "\n";
      cuda_ctx.emb_list.add_level(new_size);
      //std::cout << "\t Starting Extend_insert ...\n";
      extend_insert<<<nblocks, nthreads>>>(begin, end, level, cuda_ctx.gg, cuda_ctx.emb_list, indices);
      CudaTest("solving extend insert failed");
      //std::cout << "\t Extend_insert Done\n";
      CUDA_SAFE_CALL(cudaFree(indices));
      level ++;
    }
    cuda_ctx.emb_list.reset_level();
  }
  CUDA_SAFE_CALL(cudaDeviceSynchronize());
  t.Stop();

  printf("\truntime [cuda_base] = %f sec\n", t.Seconds());
  std::cout << "\n\ttotal_num_cliques = " << total << "\n\n";
  CUDA_SAFE_CALL(cudaFree(d_total));
}

