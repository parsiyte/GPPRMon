#pragma once
#include <limits>
#include <cmath>
#include <algorithm>

inline size_t bytes_per_spmv(int m, int nnz) {
    size_t bytes = 0;
    bytes += 2*sizeof(IndexT) * m;    // row pointer
    bytes += 1*sizeof(IndexT) * nnz;  // column index
    bytes += 2*sizeof(ValueT) * nnz;  // A[i,j] and x[j]
    bytes += 2*sizeof(ValueT) * m;    // y[i] = y[i] + ...
    return bytes;
}

template <typename T>
T maximum_relative_error(const T * A, const T * B, const size_t N) {

	unsigned err = 0;
	unsigned err_1 = 0;
	unsigned err_2 = 0;
	unsigned err_3 = 0;
	unsigned err_4 = 0;
	unsigned err_5 = 0;
	float errPercent = 0;
	T max_error = 0;
	T eps = std::sqrt( std::numeric_limits<T>::epsilon() );
	
	for(size_t i = 0; i < N; i++) 
	{
		const T a = A[i];
		const T b = B[i];
		const T error = std::abs(a - b);
		if (error != 0) 
		{
			err++;
			double res = std::abs(a - b);
			errPercent = (res / std::abs(a)) * 100;
			max_error = std::max(max_error, error/(std::abs(a) + std::abs(b) + eps));

			if (errPercent <= 0.1)
				err_1++;

			else if (errPercent > 0.1 && errPercent <= 1)
				err_2++;

			else if (errPercent > 1 && errPercent <= 5)
				err_3++;

			else if (errPercent > 5 && errPercent <= 10)
				err_4++;

			else
				err_5++;
		}
	}
	printf("Total element = %d, || elements whose err <= %0.1 = %d || elements whose 0.1 < err  <= %1 = %d || elements whose %1 < err <= %5 = %d"
				 " || elements whose %5 < err <= %10 = %d || elements whose %10 < err = %d || total err Element = %d\n",
				 N, err_1, err_2, err_3, err_4, err_5, err);

	return max_error;
}

inline void SpmvSerial(int m, int nnz, const uint64_t *Ap, const IndexT *Aj, const ValueT *Ax, const ValueT *x, ValueT *y) {
	for (int i = 0; i < m; i++){
		auto row_begin = Ap[i];
		auto row_end   = Ap[i+1];
		auto sum = y[i];
		for (auto jj = row_begin; jj < row_end; jj++) {
			auto j = Aj[jj];  //column index
			sum += x[j] * Ax[jj];
		}
		y[i] = sum; 
	}
}

template <typename T>
T l2_error(size_t N, const T * a, const T * b) {
	T numerator   = 0;
	T denominator = 0;
	for (size_t i = 0; i < N; i++) {
		numerator   += (a[i] - b[i]) * (a[i] - b[i]);
		denominator += (b[i] * b[i]);
	}
	return numerator/denominator;
}

