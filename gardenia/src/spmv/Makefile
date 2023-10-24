#gcc main.cc -o main.o -c -I ../../include
#gcc verifier.cc -o verifier.o -c -I ../../include
#nvcc base.cu -o base.o -arch=sm_61 -lcudart -c -I ../../include
#nvcc base.o main.o verifier.o -o spmv_base -arch=sm_61 -lcudart -I ../../include -L /usr/lib64

include ../common.mk
SRC=main.cc
OBJS=vector.o omp_base.o verifier.o main.o
INCLUDES += -I${MKLROOT}/include -I$(CUB_DIR)
LIBS += -L${MKLROOT}/lib/intel64

CXX=gcc
NVCC_FLAGS= -arch=sm_70 -lcudart 

#						 spmv_cusparse \
#						 spmv_tiling \
#						 spmv_partition \
#						 spmv_push_tile \

all: $(OBJS) spmv_vector \
						 spmv_warp \
						 spmv_base \
						 spmv_push #.mtx

%.o: %.cpp
	$(ICPC) $(ICPCFLAGS) $(INCLUDES) -march=core-avx2 -D__PURE_INTEL_C99_HEADERS__ -c $<

ifeq ($(HOST),X86)
%.o: %.cc
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $<
else
%.o: %.cc
	$(CXX) $(SIMFLAGS) $(INCLUDES) -c $<
endif

%.o: %.cu
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) -c $<

spmv_base: main.o base.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) main.o base.o verifier.o -o $@ $(LIBS)

spmv_warp: main.o warp.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) main.o warp.o verifier.o -o $@ $(LIBS)

spmv_vector: main.o vector.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) main.o vector.o verifier.o -o $@ $(LIBS)

spmv_push: main.o push.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) main.o push.o verifier.o -o $@ $(LIBS)

clean:
	rm *.o


#spmv_mkl: main.o mkl.o verifier.o
#	$(ICPC) $(ICPCFLAGS) $(INCLUDES) main.o mkl.o verifier.o -o $@ $(LIBS) -lmkl_intel_lp64 -lmkl_core -lmkl_sequential -lpthread -lm
#	mv $@ $(BIN)

#spmv_omp_simd: omp_simd.o main.o verifier.o
#	$(ICPC) $(ICPCFLAGS) $(INCLUDES) main.o omp_simd.o verifier.o -o $@
#	mv $@ $(BIN)

#spmv_omp_base: omp_base.o main.o verifier.o
#	$(CXX) $(CXXFLAGS) $(INCLUDES) main.o omp_base.o verifier.o -o $@ -lgomp
#	mv $@ $(BIN)
#
#spmv_omp_pb: omp_pb.o main.o verifier.o
#	$(CXX) $(CXXFLAGS) $(INCLUDES) main.o omp_pb.o verifier.o -o $@ -lgomp
#	mv $@ $(BIN)
#
#spmv_omp_push: omp_push.o main.o verifier.o
#	$(CXX) $(CXXFLAGS) $(INCLUDES) main.o omp_push.o verifier.o -o $@ -lgomp
#	mv $@ $(BIN)
#
#spmv_omp_base_sim: omp_base.o main.o verifier.o
#	$(CXX) $(SIMFLAGS) $(INCLUDES) main.o omp_base.o verifier.o $(M5OP) -o $@ -lgomp
#	mv $@ $(BIN)
#
#spmv_omp_target: main.o omp_target.o verifier.o
#	$(ICPC) $(ICPCFLAGS) $(INCLUDES) $(EXTRA) main.o omp_target.o verifier.o -o $@ $(LIBS)
#	mv $@ $(BIN)
