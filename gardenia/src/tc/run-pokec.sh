#!/bin/bash
source /opt/intel/composer_xe_2015/bin/compilervars.sh intel64
export MIC_ENV_PREFIX=MIC
export MIC_USE_2MB_BUFFERS=32K
export MIC_KMP_AFFINITY=granularity=fine,balanced
export MIC_BUFFERSIZE=128M
export MIC_OMP_NUM_THREADS=112
#export OFFLOAD_REPORT=3
../../bin/tc_omp_target /home/cxh/datasets/soc-pokec.mtx
