include ../common.mk
INCLUDES += -I$(CUB_DIR)
OBJS = base.o warp.o omp_base.o verifier.o main.o


#gcc main.cc -o main.o -c -I ../../include
#gcc verifier.cc -o verifier.o -c -I ../../include
#nvcc base.cu -o base.o -c -I ../../include -lcudart -arch=sm_61 
#nvcc main.o verifier.o base.o -o cc_base -arch=sm_61 -lcudart -I ../../include -L /usr/lib64

CXX=gcc
NVCC_FLAGS= -arch=sm_70 -lcudart

#		 cc_fusion\
#		 cc_partition\
#		 cc_ocl_base

all: cc_base \
		 cc_warp \
		 cc_afforest 

%.o: %.cpp
	$(ICPC) $(ICPCFLAGS) $(INCLUDES) -c $<

%.o: %.cc
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $<

%.o: %.cu
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) -c $<

cc_ocl_base: ocl_base.o main.o verifier.o
	$(CXX) $(CXXFLAGS) $(INCLUDES) $(LIBS) main.o ocl_base.o verifier.o -o $@ -lOpenCL

cc_base: main.o base.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o base.o verifier.o -o $@ $(LIBS)

cc_afforest: main.o afforest.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o afforest.o verifier.o -o $@ $(LIBS)

cc_partition: main.o partition.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o partition.o verifier.o -o $@ $(LIBS)

cc_warp: main.o warp.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o warp.o verifier.o -o $@ $(LIBS)

cc_fusion: main.o fusion.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) main.o fusion.o verifier.o -o $@ $(LIBS)

clean:
	rm *.o

#cc_omp_base: omp_base.o main.o verifier.o
#	$(CXX) $(CXXFLAGS) $(INCLUDES) main.o omp_base.o verifier.o -o $@ -lgomp
#	mv $@ $(BIN)
#
#cc_omp_afforest: omp_afforest.o main.o verifier.o
#	$(CXX) $(CXXFLAGS) $(INCLUDES) main.o omp_afforest.o verifier.o -o $@ -lgomp
#	mv $@ $(BIN)
#cc_omp_target: main.o omp_target.o verifier.o
#	$(ICPC) $(CXXFLAGS) $(INCLUDES) $(EXTRA) main.o omp_target.o verifier.o -o $@ $(LIBS)
#	mv $@ $(BIN)
