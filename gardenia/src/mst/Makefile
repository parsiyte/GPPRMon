include ../common.mk
INCLUDES+=-I $(CUB_DIR)
SRC=main.cu
EXE=mst


#nvcc main.cu -o mst_topo -arch=sm_61 -lcudart -I ../../include

CXX=gcc
NVCC_FLAGS= -arch=sm_70 -lcudart

all: $(EXE)_topo

$(EXE)_base:
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) $(SRC) base.o -o $@ $(LIBS)

$(EXE)_topo:
	$(NVCC) $(NVCC_FLAGS) $(INCLUDES) $(EXTRA) $(SRC) -o $@

clean:
	rm *.o

