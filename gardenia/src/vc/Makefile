#gcc main.cc -o main.o -c -I ../../include
#gcc verifier.cc -o verifier.o -c -I ../../include
#nvcc linear_base.cu -o linear_base.o -arch=sm_61 -lcudart -c -I ../../include
#nvcc linear_base.o main.o verifier.o -o vc_linear_base -arch=sm_61 -lcudart -I ../../include -L /usr/lib64

include ../common.mk
INCLUDES+=-I $(CUB_DIR)
SRC=main.cc
#OBJS=omp_base.o topo_base.o topo_bitset.o topo_warp.o linear_base.o linear_bitset.o linear_warp.o main.o verifier.o
OBJS=omp_base.o linear_bitset.o main.o verifier.o

CXX=gcc
NVCC_FLAGS= -arch=sm_70 -lcudart

#vc_omp_base vc_linear_warp vc_topo_warp vc_topo_base

all: $(OBJS) vc_linear_base vc_linear_bitset 
 
%.o: %.cpp
	$(ICPC) $(ICPCFLAGS) $(INCLUDES) -c $<

%.o: %.cc
	$(CXX) $(CXXFLAGS) $(PARFLAG) $(INCLUDES) -c $<

%.o: %.cu
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) -c $<

vc_topo_base: main.o topo_base.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o topo_base.o verifier.o -o $@

vc_topo_bitset: main.o topo_bitset.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o topo_bitset.o verifier.o -o $@

vc_topo_warp: main.o topo_warp.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o topo_warp.o verifier.o -o $@

vc_linear_base: main.o linear_base.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o linear_base.o verifier.o -o $@

vc_linear_bitset: main.o linear_bitset.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o linear_bitset.o verifier.o -o $@

vc_linear_warp: main.o linear_warp.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o linear_warp.o verifier.o -o $@

clean:
	rm *.o

#vc_omp_base: omp_base.o main.o verifier.o
#	$(CXX) $(CXXFLAGS) $(INCLUDES) main.o omp_base.o verifier.o -o $@ -lgomp
#
#vc_omp_target: main.o omp_target.o verifier.o
#	$(ICPC) $(ICPCFLAGS) $(INCLUDES) $(EXTRA) main.o omp_target.o verifier.o -o $@ $(LIBS)

