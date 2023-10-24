include ../common.mk
INCLUDES+=-I$(CUB_DIR)
CXXFLAGS+= #-std=c++11 -march=core-avx2
SRC=main.cu
OBJS=base.o warp.o main.o verifier.o omp_base.o

#gcc main.cc -o main.o -c -I ../../include
#gcc verifier.cc -o verifier.o -c -I ../../include
#nvcc base.cu -o base.o -c -I ../../include -lcudart -arch=sm_61
#nvcc base.o main.o verifier.o -o pr_base -I ../../include -arch=sm_61 -L /usr/lib64

CXX=gcc
NVCC_FLAGS= -arch=sm_70 -lcudart

#					   pr_ocl_base \
#					   pr_pb \
#					   pr_push \
#					   pr_push_pb \
#					   pr_vector \
#					   pr_lb \
#					   pr_delta \
#					   pr_fusion \
#					   pr_partition \
#					   pr_tiling \
#					   pr_push_tile \
#					   pr_nvgraph 

all: $(OBJS) pr_base \
						 pr_warp 

verifier.o:
	gcc verifier.cc -o verifier.o -c -I ../../include
main.o: 
	gcc main.cc -o main.o -c -I ../../include
base.o:
	nvcc base.cu -o base.o -c -I ../../include -lcudart -arch=sm_70
warp.o:
	nvcc warp.cu -o warp.o -c -I ../../include -lcudart -arch=sm_70

pr_base: main.o base.o verifier.o
	nvcc base.o main.o verifier.o -o pr_base -I ../../include -arch=sm_70 -lcudart -L /usr/lib64

#nvcc base.o warp.o verifier.o -o pr_warp -I ../../include -arch=sm_75 -lcudart -L /usr/lib64
pr_warp: main.o warp.o verifier.o
	nvcc main.o warp.o verifier.o -o pr_warp -arch=sm_70 -lcudart -I ../../include -L /usr/lib64
#	$(NVCC) $(NVCC_FLAGS) $(INCLUDES)  main.o warp.o verifier.o -o $@ 

%.o: %.cpp
	$(ICPC) $(ICPCFLAGS) $(INCLUDES) -c $<

ifeq ($(HOST),X86)
%.o: %.cc pr.h
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $<
else
%.o: %.cc pr.h
	$(CXX) $(SIMFLAGS) $(INCLUDES) -c $<
endif

%.o: %.cu pr.h
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) -c $<

pr_ocl_base: ocl_base.o main.o verifier.o
	$(CXX) $(CXXFLAGS) $(INCLUDES) main.o ocl_base.o verifier.o -o $@ -lOpenCL
pr_pb: pb.o main.o verifier.o
	$(CXX) $(CXXFLAGS) $(INCLUDES) main.o pb.o verifier.o -o $@ -lgomp
pr_push: main.o push.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o push.o verifier.o -o $@ $(LIBS)
pr_push_pb: main.o push_pb.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o push_pb.o verifier.o -o $@ $(LIBS)


	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o base.o verifier.o -o $@ $(LIBS)

pr_vector: main.o vector.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o vector.o verifier.o -o $@ $(LIBS)
pr_lb: main.o lb.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o lb.o verifier.o -o $@ $(LIBS)
pr_delta: main.o delta.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o delta.o verifier.o -o $@ $(LIBS)
pr_fusion: main.o fusion.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o fusion.o verifier.o -o $@ $(LIBS)
pr_partition: main.o partition.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o partition.o verifier.o -o $@ $(LIBS)
pr_tiling: tiling.o main.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o tiling.o verifier.o -o $@ $(LIBS)
pr_push_tile: main.o push_tile.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o push_tile.o verifier.o -o $@ $(LIBS)
pr_nvgraph: main.o nvgraph.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o nvgraph.o verifier.o -o $@ $(LIBS) -lnvgraph

clean:
	rm *.o

#pr_omp_base: omp_base.o main.o verifier.o
#	$(CXX) $(CXXFLAGS) $(INCLUDES) main.o omp_base.o verifier.o -o $@ -lgomp
#	mv $@ $(BIN)
#
#pr_omp_push: omp_push.o main.o verifier.o
#	$(CXX) $(CXXFLAGS) $(INCLUDES) main.o omp_push.o verifier.o -o $@ -lgomp
#	mv $@ $(BIN)
#
#pr_omp_target: main.o omp_target.o verifier.o
#	$(ICPC) $(CXXFLAGS) $(INCLUDES) $(EXTRA) main.o omp_target.o verifier.o -o $@ $(LIBS)
#	mv $@ $(BIN)
#pr_omp_delta: omp_delta.o main.o verifier.o
#	$(CXX) $(CXXFLAGS) $(INCLUDES) main.o omp_delta.o verifier.o -o $@ -lgomp
#	mv $@ $(BIN)
#
#pr_omp_partition: omp_partition.o main.o verifier.o
#	$(CXX) $(CXXFLAGS) $(INCLUDES) main.o omp_partition.o verifier.o -o $@ -lgomp
#pr_omp_sim: omp_sim.o main.o verifier.o
#	$(CXX) $(SIMFLAGS) $(INCLUDES) main.o omp_sim.o verifier.o $(M5OP) -o $@ -lgomp
#pr_omp_pb: omp_pb.o main.o verifier.o
#	$(CXX) $(CXXFLAGS) $(INCLUDES) main.o omp_pb.o verifier.o -o $@ -lgomp
#	mv $@ $(BIN)
#						 pr_omp_base \


