// Copyright 2016, National University of Defense Technology
// Authors: Xuhao Chen <cxh@illinois.edu>
#include "spmv.h"
#include "timer.h"
#include <mkl.h>
#define SPMV_VARIANT "spmv_mkl"

void SpmvSolver(int m, int nnz, IndexT *ApT, IndexT *AjT, ValueT *AxT, IndexT *Ap, IndexT *Aj, ValueT *Ax, ValueT *x, ValueT *y, int *degrees) {
	int num_threads = 1;
	#pragma omp parallel
	{
		num_threads = omp_get_num_threads();
	}
	printf("Launching OpenMP SpMV solver (%d threads) ...\n", num_threads);

	Timer t;
	t.Start();
	MKL_INT n = m;
	mkl_cspblas_scsrgemv("N", &n, Ax, Ap, Aj, x, y);
	t.Stop();

	printf("\truntime [%s] = %f ms.\n", SPMV_VARIANT, t.Millisecs());
	return;
}
