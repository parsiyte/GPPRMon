#gcc main.cc -o main.o -c -I ../../include
#gcc verifier.cc -o verifier.o -c -I ../../include
#nvcc linear_base.cu -o linear_base.o -arch=sm_61 -lcudart -c -I ../../include
#nvcc linear_base.o main.o verifier.o -o sssp_base -arch=sm_61 -lcudart -I ../../include -L /usr/lib64

include ../common.mk
INCLUDES+=-I $(CUB_DIR)
EXE=sssp
OBJS=main.o verifier.o

CXX=gcc
NVCC_FLAGS= -arch=sm_70 -lcudart

# sssp_ocl_base sssp_ocl_base sssp_topo_base sssp_topo_lb 
all: sssp_linear_base sssp_linear_lb 

#$(EXE)_omp_base

%.o: %.cpp
	$(ICPC) $(ICPCFLAGS) $(INCLUDES) -c $<

%.o: %.cc
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $<

%.o: %.cu
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) -c $<

sssp_ocl_base: ocl_base.o $(OBJS)
	$(CXX) $(CXXFLAGS) $(INCLUDES) $(OBJS) ocl_base.o -o $@ -lOpenCL

$(EXE)_linear_base: main.o linear_base.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o linear_base.o verifier.o -o $@ $(LIBS)

$(EXE)_linear_lb: main.o linear_lb.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o linear_lb.o verifier.o -o $@ $(LIBS)

$(EXE)_dstep: main.o dstep.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o dstep.o verifier.o -o $@ $(LIBS)

$(EXE)_topo_base: main.o topo_base.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o topo_base.o verifier.o -o $@ $(LIBS)

$(EXE)_topo_lb: main.o topo_lb.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o topo_lb.o verifier.o -o $@ $(LIBS)

clean:
	rm *.o

#$(EXE)_omp_base: omp_base.o $(OBJS)
#	$(CXX) $(CXXFLAGS) $(INCLUDES) $(EXTRA) $(OBJS) omp_base.o -o $@ -lgomp
#	mv $@ $(BIN)
#
#$(EXE)_omp_target: main.o omp_target.o verifier.o
#	$(ICPC) $(ICPCFLAGS) $(INCLUDES) $(EXTRA) main.o omp_target.o verifier.o -o $@
#	mv $@ $(BIN)
