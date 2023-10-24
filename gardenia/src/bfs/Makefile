include ../common.mk
INCLUDES+=-I $(CUB_DIR)
ICPCFLAGS+=-std=c++98
B40_DIR=../../back40computing-read-only
B40C_INC=-I $(B40_DIR) -I $(B40_DIR)/test
OBJS= main.o verifier.o 
 #bfs_omp_beamer bfs_omp_base

#gcc main.cc -o main.o -c -I ../../include
#gcc verifier.cc -o verifier.o -c -I ../../include
#nvcc linear_base.cu -o linear_base.o -c -I ../../include -lcudart -arch=sm_61
#nvcc linear_base.o main.o verifier.o -o bfs_linear_base -I ../../include -arch=sm_61 -L /usr/lib64

CXX=gcc
NVCC_FLAGS= -arch=sm_70 -lcudart

all: bfs_linear_base \
		 bfs_linear_lb 

#		 bfs_linear_pb \
#		 bfs_linear_vector \
#	   bfs_topo_base \
#		 bfs_topo_vector \
#		 bfs_topo_lb \
#		 bfs_topo_pb \
#		 bfs_fusion \
#		 bfs_hybrid_base \
#		 bfs_hybrid_vector \
#		 bfs_hybrid_lb \
#		 bfs_hybrid_tile \
#		 bfs_afree \
#		 bfs_bu \
#		 bfs_merrill 


%.o: %.cpp
	$(ICPC) $(ICPCFLAGS) $(INCLUDES) -c $<

ifeq ($(HOST),X86)
%.o: %.cc
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $<
else
%.o: %.cc
	$(CXX) $(SIMFLAGS) $(INCLUDES) -c $<
endif

%.o: %.cu
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) -c $<

bfs_ocl_base: ocl_base.o $(OBJS)
	$(CXX) $(CXXFLAGS) $(INCLUDES) $(OBJS) ocl_base.o -o $@ -lOpenCL

bfs_linear_base: linear_base.o $(OBJS)
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) $(OBJS) linear_base.o -o $@ $(LIBS)

bfs_linear_pb: linear_pb.o $(OBJS)
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) $(OBJS) linear_pb.o -o $@ $(LIBS)

bfs_linear_vector: linear_vector.o $(OBJS)
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) $(OBJS) linear_vector.o -o $@ $(LIBS)

bfs_linear_lb: linear_lb.o $(OBJS)
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) $(OBJS) linear_lb.o -o $@ $(LIBS)

bfs_topo_base: topo_base.o $(OBJS)
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) $(OBJS) topo_base.o -o $@ $(LIBS)

bfs_topo_vector: topo_vector.o $(OBJS)
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) $(OBJS) topo_vector.o -o $@ $(LIBS)

bfs_topo_lb: topo_lb.o $(OBJS)
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) $(OBJS) topo_lb.o -o $@ $(LIBS)

bfs_topo_pb: topo_pb.o $(OBJS)
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) $(OBJS) topo_pb.o -o $@ $(LIBS)

bfs_fusion: fusion.o $(OBJS)
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) $(OBJS) fusion.o -o $@ $(LIBS)

bfs_hybrid_base: hybrid_base.o $(OBJS)
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) $(OBJS) hybrid_base.o -o $@ $(LIBS)

bfs_hybrid_vector: hybrid_vector.o $(OBJS)
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) $(OBJS) hybrid_vector.o -o $@ $(LIBS)

bfs_hybrid_lb: hybrid_lb.o $(OBJS)
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) $(OBJS) hybrid_lb.o -o $@ $(LIBS)

bfs_hybrid_tile: hybrid_tile.o $(OBJS)
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) $(OBJS) hybrid_tile.o -o $@ $(LIBS)

bfs_afree: atomic_free.o $(OBJS)
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) $(OBJS) atomic_free.o -o $@ $(LIBS)

bfs_bu: bottom_up.o $(OBJS)
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) $(OBJS) bottom_up.o -o $@ $(LIBS)

bfs_merrill: merrill.cu main.o verifier.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(B40C_INC) -c merrill.cu -o merrill.o
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) main.o merrill.o verifier.o -o $@ $(LIBS)

clean:
	rm *.o


#bfs_omp_beamer: omp_beamer.o $(OBJS)
#	$(CXX) $(CXXFLAGS) $(INCLUDES) $(OBJS) omp_beamer.o -o $@ -lgomp
#	mv $@ $(BIN)
#bfs_omp_target: omp_target.o $(OBJS)
#	$(ICPC) $(CXXFLAGS) $(INCLUDES) $(EXTRA) $(OBJS) omp_target.o -o $@ $(LIBS)
#	mv $@ $(BIN)

#bfs_omp_base: omp_base.o $(OBJS)
#	$(CXX) $(CXXFLAGS) $(INCLUDES) $(EXTRA) $(OBJS) omp_base.o -o $@ -lgomp
#	mv $@ $(BIN)
#bfs_omp_topo: omp_topo.o $(OBJS)
#	$(CXX) $(CXXFLAGS) $(INCLUDES) $(OBJS) omp_topo.o -o $@ -lgomp
#	mv $@ $(BIN)
