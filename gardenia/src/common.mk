CUDA_HOME=/usr/local/cuda
PAPI_HOME=/usr/local/papi-6.0.0
ICC_HOME=/opt/intel/compilers_and_libraries/linux/bin/intel64
GEM5_HOME=/home/cxh/gem5
MKLROOT=/opt/intel/mkl
CUB_DIR=../../cub
OCL_DIR=/usr/local/cuda/targets/x86_64-linux/lib/
BIN=../../bin
HOST=X86
ifeq ($(HOST),X86)
CC=gcc
CXX=g++
else 
CC=aarch64-linux-gnu-gcc
CXX=aarch64-linux-gnu-g++
endif
ICC=$(ICC_HOME)/icc
ICPC=$(ICC_HOME)/icpc
NVCC=nvcc
#NVCC=$(CUDA_HOME)/bin/nvcc
COMPUTECAPABILITY=sm_70
CUDA_ARCH := \
	-gencode arch=compute_70,code=sm_70
CXXFLAGS=
ICPCFLAGS=
NVFLAGS=$(CUDA_ARCH)
#NVFLAGS+=-Xptxas -v
NVFLAGS+=-lcudart 
ifeq ($(HOST),X86)
#SIMFLAGS=-O3 -Wall -DSIM -fopenmp -static -L/home/cxh/m5threads/ -lpthread
SIMFLAGS=-Wall -fopenmp -O3 -g -static -lpthread -L$(GEM5_HOME)/m5threads
else
SIMFLAGS=-flto -fwhole-program -O3 -Wall -fopenmp -static -g
endif
#M5OP=$(GEM5_HOME)/util/m5/src/arm/m5op.S
M5OP=$(GEM5_HOME)/util/m5/src/x86/m5op.S
ifeq ($(DEBUG), 1)
	CXXFLAGS += -g -O0
	NVFLAGS += -G -lineinfo
else
	CXXFLAGS += 
	NVFLAGS += 
endif
CU_INC = -I/usr/include/cuda
CU_INC = -I$(CUDA_HOME)/include
INCLUDES = -I../../include
#INCLUDES += $(CU_INC)
#LIBS = -L$(CUDA_HOME)/lib64
LIBS = -L/usr/lib64

ifeq ($(PAPI), 1)
CXXFLAGS += -DENABLE_PAPI
INCLUDES += -I$(PAPI_HOME)/include
LIBS += -L$(PAPI_HOME)/lib -lpapi
endif

ifeq ($(USE_TBB), 1)
LIBS += -L/h2/xchen/work/gardenia_code/tbb2020/lib/intel64/gcc4.8/ -ltbb
else
LIBS += -lgomp
endif

ifeq ($(SIM), 1)
CXXFLAGS=-DSIM $(SIMFLAGS) 
EXTRA=$(M5OP)
INCLUDES+=-I$(GEM5_HOME)/include
LIBS += -pthread -lrt -ldl
endif

VPATH += ../common
OBJS=main.o VertexSet.o graph.o
