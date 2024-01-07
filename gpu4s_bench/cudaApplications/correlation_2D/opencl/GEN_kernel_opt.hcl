
std::string kernel_code = 
"void kernel mean_matrices (global const bench_t *A, global const bench_t *B,global result_bench_t *mean_A ,global result_bench_t *mean_B ,const int n){\n"
"unsigned int size = n;\n"
"int i = get_global_id(0);\n"
"int j = get_global_id(1);\n"
"unsigned int tid_x = get_local_id(0);\n"
"unsigned int tid_y = get_local_id(1);\n"
"__local  bench_t shared_data_A[BLOCK_SIZE * BLOCK_SIZE];\n"
"__local  bench_t shared_data_B[BLOCK_SIZE * BLOCK_SIZE];\n"
"if (i < size && j < size){\n"
"shared_data_A[tid_x*get_local_size(1) + tid_y] = A[i*size + j];\n"
"shared_data_B[tid_x*get_local_size(1) + tid_y] = B[i*size + j];\n"
"// sinc theads\n"
"barrier(CLK_LOCAL_MEM_FENCE);\n"
"for(unsigned int s_y = get_local_size(1)/2; s_y > 0; s_y >>= 1)\n"
"{\n"
"if (tid_y < s_y)\n"
"{\n"
"shared_data_A[tid_x * get_local_size(1) + tid_y] += shared_data_A[tid_x * get_local_size(1) + tid_y + s_y];\n"
"shared_data_B[tid_x * get_local_size(1) + tid_y] += shared_data_B[tid_x * get_local_size(1) + tid_y + s_y];\n"
"}\n"
"barrier(CLK_LOCAL_MEM_FENCE);\n"
"}\n"
"for(unsigned int s_x = get_local_size(0)/2; s_x > 0; s_x >>= 1 )\n"
"{\n"
"if(tid_x < s_x)\n"
"{\n"
"shared_data_A[tid_x * get_local_size(1)] += shared_data_A[(tid_x + s_x) * get_local_size(1)];\n"
"shared_data_B[tid_x * get_local_size(1)] += shared_data_B[(tid_x + s_x) * get_local_size(1)];\n"
"}\n"
"barrier(CLK_LOCAL_MEM_FENCE);\n"
"}\n"
"if( tid_x == 0 && tid_y == 0)\n"
"{\n"
"atomic_add_global(mean_A, shared_data_A[0]);\n"
"atomic_add_global(mean_B, shared_data_B[0]);\n"
"}\n"
"}\n"
"}\n"
"void kernel correlation_2D(global const bench_t *A,global const bench_t *B,global result_bench_t *R, global result_bench_t *mean_A ,global result_bench_t *mean_B, global result_bench_t *acumulate_value_a_b, global result_bench_t *acumulate_value_a_a, global result_bench_t *acumulate_value_b_b,const int n){\n"
"unsigned int size = n;\n"
"int i = get_global_id(0);\n"
"int j = get_global_id(1);\n"
"unsigned int tid_x = get_local_id(0);\n"
"unsigned int tid_y = get_local_id(1);\n"
"result_bench_t mean_a_matrix =  *mean_A / (n * n);\n"
"result_bench_t mean_b_matrix =  *mean_B / (n * n);\n"
"__local bench_t shared_data_A_B[BLOCK_SIZE * BLOCK_SIZE];\n"
"__local bench_t shared_data_A_A[BLOCK_SIZE * BLOCK_SIZE];\n"
"__local bench_t shared_data_B_B[BLOCK_SIZE * BLOCK_SIZE];\n"
"if (i < size && j < size){\n"
"result_bench_t result_mean_a = 0;\n"
"result_bench_t result_mean_b = 0;\n"
"result_mean_a = A[i*size+j] - mean_a_matrix;\n"
"result_mean_b = B[i*size+j] - mean_b_matrix;\n"
"shared_data_A_B[tid_x*get_local_size(1) + tid_y] = result_mean_a * result_mean_b;\n"
"shared_data_A_A[tid_x*get_local_size(1) + tid_y] = result_mean_a * result_mean_a;\n"
"shared_data_B_B[tid_x*get_local_size(1) + tid_y] = result_mean_b * result_mean_b;\n"
"// first get the final value  in A (A - mean(a)) and in B (B - mean(b))\n"
"__syncthreads();\n"
"for(unsigned int s_y = get_local_size(1)/2; s_y > 0; s_y >>= 1)\n"
"{\n"
"if (tid_y < s_y)\n"
"{\n"
"shared_data_A_B[tid_x * get_local_size(1) + tid_y] += shared_data_A_B[tid_x * get_local_size(1) + tid_y + s_y];\n"
"shared_data_A_A[tid_x * get_local_size(1) + tid_y] += shared_data_A_A[tid_x * get_local_size(1) + tid_y + s_y];\n"
"shared_data_B_B[tid_x * get_local_size(1) + tid_y] += shared_data_B_B[tid_x * get_local_size(1) + tid_y + s_y];\n"
"}\n"
"barrier(CLK_LOCAL_MEM_FENCE);\n"
"}\n"
"for(unsigned int s_x = get_local_size(0)/2; s_x > 0; s_x >>= 1 )\n"
"{\n"
"if(tid_x < s_x)\n"
"{\n"
"shared_data_A_B[tid_x * get_local_size(1)] += shared_data_A_B[(tid_x + s_x) * get_local_size(1)];\n"
"shared_data_A_A[tid_x * get_local_size(1)] += shared_data_A_A[(tid_x + s_x) * get_local_size(1)];\n"
"shared_data_B_B[tid_x * get_local_size(1)] += shared_data_B_B[(tid_x + s_x) * get_local_size(1)];\n"
"}\n"
"barrier(CLK_LOCAL_MEM_FENCE);\n"
"}\n"
"if( tid_x == 0 && tid_y == 0)\n"
"{\n"
"atomic_add_global(acumulate_value_a_b, shared_data_A_B[0]);\n"
"atomic_add_global(acumulate_value_a_a, shared_data_A_A[0]);\n"
"atomic_add_global(acumulate_value_b_b, shared_data_B_B[0]);\n"
"}\n"
"}\n"
"}\n"
;