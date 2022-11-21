## For the installation and build
---------------------------------
Detailed documentation on what GPGPU-Sim models are, how to configure it, and a
guide to the source code can be found here: <http://gpgpu-sim.org/manual/>.
Instructions for building Doxygen source code documentation are included below.
Detailed documentation on GPUWattch, including how to configure it and a guide
to the source code, can be found here: <http://gpgpu-sim.org/gpuwattch/>.

**GPGPU-Sim dependencies:** ```gcc, g++, make, makedepend, xutils, bison, flex, zlib ,CUDA Toolkit```

**GPGPU-Sim documentation dependencies:** ```doxygen, graphvi```

**AerialVision dependencies:** ```python-pmw, python-ply, python-numpy, libpng12-dev, python-matplotlib```

**CUDA SDK dependencies:** ```install libxi-dev libxmu-dev libglut3-dev```

$source setup_environment <build_type> 
 - For debugging, build_type -> ```debug```
 - For normal release -> you dont need to specify build_type, blank as empty.

To build the simulator ```user$ make```, clean executables of the simulator ```user$ make clean```, build the Doxygen generated documentation ```user$ make docs```, clean the docs ```user$ make cleandocs```. This doxygen-generated documentation will help you to understand classes, templates, functions, etc.

## About tracking runtime memory accesses
-------------------------------------------
During simulation, the simulator creates memory access information in the **runtime_profiling_metrics/memory_accesses** folder. 
 - [x] mem_profiler : 1 ---- memory access runtime profiling (0 = not enabled)
 - [x] mem_runtime_stat :100 ---- mem_runtime_stat collection frequency
 - [x] L1D_metrics : 1 ---- memory access runtime profiling for L1 data cache (0 = not enabled)
 - [x] L2_metrics : 1 ---- memory access runtime profiling for L2 cache (0 = not enabled)
 - [x] DRAM_metrics : 1 ---- memory access runtime profiling for DRAM (0 = not enabled)
 - [x] store_enable : 1 ---- To collect statistics for the store instructions (write operations onto L1D, L2 caches, and DRAM) in addition to loads. (0 = for just loads)
 - [x] accumulate_stats : 1 ---- To accumulate statistics. If not enabled, each statistic will reveal just the corresponding interval statistics.

## About tracking runtime energy consumption of components
-------------------------------------------
During simulation, the simulator creates memory access information in the **runtime_profiling_metrics/energy_consumption** folder. 
 - [x] power_simulation_enabled : 1 ---- Turn on power simulator (1=On, 0=Off).
 - [x] power_per_cycle_dump : 1 ---- Dump detailed power output each cycle
 - [x] dvfs_enabled : 1 ---- Turn on DVFS for power model.
 - [x] aggregate_power_stats : 1 ---- Accumulate power across all kernels
 - [x] steady_power_levels_enabled :  0 ---- produce a file for the steady power levels (1=On, 0=Off)
 - [x] steady_state_definition : 8:4 ---- allowed deviation:number of samples
 - [x] power_trace_enabled : 0 ---- produce a file for the power trace (1=On, 0=Off) 
 - [x] power_trace_zlevel : 0 ---- Compression level of the power trace output log (0=no comp, 9=highest)
 - [x] power_simulation_mode : 0 ---- Switch performance counter input for power simulation (0=Sim, 1=HW, 2=HW-Sim Hybrid)

### About tracking runtime energy consumption of components
**Example scenario: **
1. mvt application from PolyBench benchmark suite is compiled with ```nvcc mvt.cu -o mvt -lcudart -arch=sm_75``` command and executed with ```./mvt > mvt.txt``` where **mvt.txt** will record normal performance outputs of the simulator. 
2. Here, runtime metrics related to the memory access to the components and energy consumption will be recorded in the runtime_profiling_metrics folder.
	
	2.1. Memory access metrics are collected via kernel basis such that there are separate memory accesses for each kernel because each kernel is called by the main function separately for our target applications.
	
	2.2. Energy consumption metrics are collected without taking care of kernel sequence. It will collect power dissipation till the end of GPU usage.
	
	2.3. After each 1 million cycles, new .csv files are generated to store the metrics in order not to fulfill RAM during the runtime of long GPU kernels. For instance, while f_core_eu.csv is the first metric file, f_core_eu_1.csv is the second metric file for the same application. f_core_eu_1.csv file is generated after the first 1 million cycles.
3. Instead of using .txt files, the output format was converted to .csv files to easily manipulate those metrics as DataFrames in python.
4. In addition to accumulating options for each metric type, one can collect metrics separately for each sampling cycle interval.
5. Collecting store memory access option is added to the simulator because write misses occur on both L1D and L2.

The below figures explain the components: 

