// Copyright 2016, National University of Defense Technology
// Authors: Xuhao Chen <cxh@illinois.edu>
#include "pr.h"
#include "timer.h"
#include <vector>
#include "simd_utils.h"
#include "prop_blocking.h"
#define PR_VARIANT "omp_pb" // propagation blocking

// m: number of vertices, nnz: number of non-zero values
void PRSolver(int m, int nnz, IndexT *in_row_offsets, IndexT *in_column_indices, IndexT *out_row_offsets, IndexT *out_column_indices, int *degrees, ScoreT *scores) {
	int num_threads = 1;
	#pragma omp parallel
	{
	num_threads = omp_get_num_threads();
	}
	printf("Launching OpenMP PR solver (%d threads) ...\n", num_threads);
	const ScoreT base_score = (1.0f - kDamp) / m;
	vector<ScoreT> sums(m, 0);
	int num_bins = (m-1) / BIN_WIDTH + 1; // the number of bins is the number of vertices in the graph divided by the bin width

	int iter = 0;
	double error = 0;
	preprocessing(m, nnz, out_row_offsets, out_column_indices);

	vector<vector<aligned_vector<IndexT> > > local_vertex_bins(num_threads);
	vector<vector<aligned_vector<ScoreT> > > local_contri_bins(num_threads);
	vector<vector<aligned_vector<IndexT> > > vertex_bufs(num_threads);
	vector<vector<aligned_vector<ScoreT> > > contri_bufs(num_threads);
	vector<vector<size_t> > buf_counter(num_threads);
	for (int tid = 0; tid < num_threads; tid ++) {
		local_vertex_bins[tid].resize(num_bins);
		local_contri_bins[tid].resize(num_bins);
		vertex_bufs[tid].resize(num_bins);
		contri_bufs[tid].resize(num_bins);
		buf_counter[tid].resize(num_bins);
		for (int bid = 0; bid < num_bins; bid ++) {
			vertex_bufs[tid][bid].resize(buf_size);
			contri_bufs[tid][bid].resize(buf_size);
			buf_counter[tid][bid] = 0;
		}
	}

	Timer t;
	t.Start();
	do {
		iter ++;
		#pragma omp parallel for schedule(dynamic, 64)
		for (int u = 0; u < m; u ++) {
			//int tid = omp_get_thread_num();
			const IndexT row_begin = out_row_offsets[u];
			const IndexT row_end = out_row_offsets[u+1];
			int degree = row_end - row_begin;
			ScoreT c = scores[u] / (ScoreT)degree; // contribution
			for (IndexT offset = row_begin; offset < row_end; offset ++) {
				IndexT v = out_column_indices[offset];
				int dest_bin = v >> BITS; // v / BIN_WIDTH
				value_bins[dest_bin][pos[offset]] = c;
/*
				if (buf_counter[tid][dest_bin] < buf_size) {
					contri_bufs[tid][dest_bin][buf_counter[tid][offset]] = c;
					if (buf_counter[tid][dest_bin] == buf_size) {
						streaming_store<ScoreT>(contri_bufs[tid][dest_bin].data(), value_bins[dest_bin].data()+pos[offset]);
						buf_counter[tid][dest_bin] = 0;
					}
				}
*/
			}
		}
		/*
		for (int tid = 0; tid < num_threads; tid ++) {
			for (int bid = 0; bid < num_bins; bid ++) {
				if (buf_counter[tid][bid] > 0) {
					// padding
					do {
						contri_bufs[tid][bid][buf_counter[tid][bid]++] = 0;
					} while (buf_counter[tid][bid] != buf_size);
					// dump buffer to memory
					streaming_store<ScoreT>(contri_bufs[tid][bid].data(), local_contri_bins[tid][bid].data()+pos[tid][bid]);
					pos[tid][bid] += buf_size;
					buf_counter[tid][bid] = 0;
				}
			}
		}
*/
		//#pragma omp parallel for schedule(dynamic, 64)
		for (int bid = 0; bid < num_bins; bid ++) {
			for(int k = 0; k < sizes[bid]; k++) {
				ScoreT c = value_bins[bid][k];
				IndexT v = vertex_bins[bid][k];
				sums[v] = sums[v] + c;
			}
		}

		error = 0;
		#pragma omp parallel for reduction(+ : error)
		for (int u = 0; u < m; u ++) {
			ScoreT new_score = base_score + kDamp * sums[u];
			error += fabs(new_score - scores[u]);
			scores[u] = new_score;
			sums[u] = 0;
		}
		printf(" %2d    %lf\n", iter, error);
		if (error < EPSILON) break;
	} while(iter < MAX_ITER);
	t.Stop();
	printf("\titerations = %d.\n", iter);
	printf("\truntime [%s] = %f ms.\n", PR_VARIANT, t.Millisecs());
	return;
}

