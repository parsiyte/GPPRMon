#gcc main.cc -o main.o -c -I ../../include
#gcc verifier.cc -o verifier.o -c -I ../../include
#1)nvcc bitset.cu -o bitset.o -lcudart -arch=sm_70 -c -I ../../include -I ../../cub
#2)nvcc topo.cu -o topo.o -lcudart -arch=sm_70 -c -I ../../include -I ../../cub
#nvcc wcc.cu -o wcc.o -lcudart -arch=sm_70 -c -I ../../include -I ../../cub
#nvcc two_phase.cu -o two_phase.o -lcudart -arch=sm_70 -c -I ../../include -I ../../cub
#nvcc base.cu -o base.o -lcudart -arch=sm_70 -c -I ../../include -I ../../cub
#nvcc main.o base.o topo.o verifier.o wcc.o -o scc_base -lcudart -arch=sm_70 -I ../../include -I ../../cub -L /usr/lib64





include ../common.mk
CXXFLAGS+=-std=c++11
INCLUDES+=-I $(CUB_DIR)
SRC=main.cc
OBJS=base.o bitset.o main.o verifier.o omp_base.o topo.o wcc.o two_phase.o

all: $(OBJS) scc_topo scc_two_phase

%.o: %.cc
	$(CXX) $(CXXFLAGS) $(PARFLAG) $(INCLUDES) -c $<

%.o: %.cu
	$(NVCC) $(NVFLAGS) $(INCLUDES) -c $<

cc_omp: omp_base.o main.o verifier.o
	$(CXX) $(CXXFLAGS) $(INCLUDES) main.o omp_base.o verifier.o -o $@ -lgomp
	mv $@ $(BIN)

scc_base: main.o base.o verifier.o
	$(NVCC) $(NVFLAGS) $(INCLUDES) $(EXTRA) main.o base.o verifier.o -o $@ $(LIBS)
	mv $@ $(BIN)

scc_topo: main.o bitset.o topo.o verifier.o
	$(NVCC) $(NVFLAGS) $(INCLUDES) $(EXTRA) main.o bitset.o topo.o verifier.o -o $@ $(LIBS)
	mv $@ $(BIN)

scc_two_phase: main.o bitset.o two_phase.o verifier.o wcc.o
	$(NVCC) $(NVFLAGS) $(INCLUDES) $(EXTRA) main.o bitset.o two_phase.o wcc.o verifier.o -o $@ $(LIBS)
	mv $@ $(BIN)

cc_lb:
	$(NVCC) $(NVFLAGS) $(INCLUDES) $(EXTRA) main.o -o $@ $(LIBS)
	mv $@ $(BIN)

clean:
	rm *.o
