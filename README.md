
[1 - Install and build simulator](##1 - Prerequisites, Installing and Building of Simulator) <br />
[About tracking runtime memory accesses](##About-tracking-runtime-memory-accesses) <br />
	[Example scenario](####Example-scenario) <br />
[Visualization of a kernel in runtime of simulation](##Visualization-of-a-kernel-in-runtime-of-simulation) <br />

## 1 - Prerequisites, Installing and Building of Simulator
---------------------------------
Detailed documentation on what GPGPU-Sim models are, how to configure it, and a guide to the source code can be found here: <http://gpgpu-sim.org/manual/>. Also a detailed documentation on AccelWattch, including how to configure it and a guide to the source code, can be found here: <https://accel-sim.github.io/accelwattch.html>.
### To install 
> **GPGPU-Sim dependencies:** ```gcc, g++, make, makedepend, xutils, bison, flex, zlib ,CUDA Toolkit``` <br>
> (optional) **GPGPU-Sim documentation dependencies:** ```doxygen, graphvi``` <br>
> (optional) **AerialVision dependencies:** ```python-pmw, python-ply, python-numpy, libpng12-dev, python-matplotlib``` <br>
> **CUDA SDK dependencies:** ```libxi-dev libxmu-dev libglut3-dev```  <br> 

After installing prerequisite libraries including the simulator, clone the accelWattch implementation of the simulator (GPGPU-Sim 4.2). Then, you should follow the below commands inside the simulator directory to build the simulator.

### To build 
![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png) `../gpgpu_sim``$source setup_environment <build_type>` sets the environment accordingly to build the simulator correctly.
> For debugging, build_type -> `debug` <br>
> For normal release -> you don't need to specify build_type, blank as empty. <br>

<h1 style="color:purple;">Hello World</h1>


Then, 
`**../gpgpu_sim**$make` command builds the simulator compiling and creating executables. <br>
`**../gpgpu_sim**$make clean` command cleans the executables of the simulator. <br>

Also if you want to generate documentations files whose dependency files are specified as optional, you must first install the dependencies. Afterwards, you can obtain the docs with `**../gpgpu_sim**$make docs` and delete them with `**../gpgpu_sim**$make cleandocs` commands. These doxygen-generated documentation will help you to understand classes, templates, functions, etc.

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
 - [x] gpgpu_runtime_stat : 100 ---- Sampling frequency (in terms of gpu sim cycle) (default = 100)

#### Example scenario:
1. mvt application from PolyBench benchmark suite is compiled with ```nvcc mvt.cu -o mvt -lcudart -arch=sm_70``` command and executed with ```./mvt > mvt.txt``` where **mvt.txt** will record normal performance outputs of the simulator. 
2. Here, runtime metrics related to the memory access to the components and energy consumption will be recorded in the runtime_profiling_metrics folder.
	
	2.1. Memory access metrics are collected via kernel basis such that there are separate memory accesses for each kernel because each kernel is called by the main function separately for our target applications.
	
	2.2. Energy consumption metrics are collected without taking care of kernel sequence. It will collect power dissipation till the end of GPU usage.
	
	2.3. After each 1 million cycles, new .csv files are generated to store the metrics in order not to fulfill RAM during the runtime of long GPU kernels. For instance, while f_core_eu.csv is the first metric file, f_core_eu_1.csv is the second metric file for the same application. f_core_eu_1.csv file is generated after the first 1 million cycles.
3. Instead of using .txt files, the output format was converted to .csv files to easily manipulate those metrics as DataFrames in python.
4. In addition to accumulating options for each metric type, one can collect metrics separately for each sampling cycle interval.
5. Collecting store memory access option is added to the simulator because write misses occur on both L1D and L2.

## Visualization of a kernel in runtime of simulation
-------------------------------------------
This is a visualizer tool that takes csv files obtained via run-time simulation of a GPU kernel, and generates corresponding memory access mapping onto a visualization for the corresponding architecture. In GPUs, there are L1D caches located onto SMs, lots of memory partitions which includes L2 caches and DRAM banks and NoCs which connects L2 and DRAMs to the SMs. For the configured architectures, the number of L1D cache is equal to SMs, the number of DRAM banks is equal to the number of memory partition and the number of L2 caches is equal to the number of memory partition * 2. 

Here, we created architecture schemes for all of the ```SM2_GTX480, SM3_KEPLER_TITAN, SM6_TITANX, SM7_QV100, SM7_TITANV, SM75_RTX2060, SM75_RTX2060_S, SM86_RTX3070 ``` GPUs. 

The represented metrics for caches: ``` hits, hit_reserved_status, misses, reservation_failures, sector_misses, and mshr_hits ```. Whenever an access created, the corresponding memory access looks for the closest cache. Cache is sectored such that if a line is 128 bytes, one sector for this cache line is 32 bytes.

 - **Hits:** Data is found in the corresponding sector of the line.
 - **Hit Reserved:** The line is allocated for the data, but the data does not arrive yet. Data will be located to the corresponding line and sector.
 - **Misses:** Miss is used for a cache line eviction. Line eviction is determined with respect to a dirty counter. Replacement policy is determined via cache configuration.
 - **Reservation Failures:** Whenever an access cannot find the data in the cache, it tries to create a miss request in MSHR buffer. When there is no slot to hold the corresponding miss in the buffer, it stalls the memory pipeline and the status for this situation is the reservation failures. 
 - **Sector Misses:** When data is not found in the looked sector of the cache line, access status is the sector miss.
 - **MSHR Hits:** When data is not found in the looked sector of the cache line, and miss request is already located in the MSHR buffer, it is recorded as MSHR hit.

To execute the runtime memory access visualizer for a kernel, you must enable memory collection metrics as above. Then, you can viusalize the runtime memory access as executing the following command. 
```console
user@simulator_path/runtime_visualizer$ python3 metric_manipulator.py sampling_cycle arch_name
```
 - **sampling_cycle** is the run-time visualization interval. 
 - **arch_name** is the GPU name which may be ``` GTX480, TITAN, TITANX, RTX2060, RTX2060S, TITANV, QV100, RTX3070```


1. (5500-6000)
![5500_5980](https://user-images.githubusercontent.com/73446582/215438622-621d34ba-7e9b-4c84-bac7-67d971745f5b.png)
2. (6000-6500)
![6000_6480](https://user-images.githubusercontent.com/73446582/215438628-9956b99f-9524-4ae8-9a96-58f6af588540.png)
3. (6500-7000)
![6500_6980](https://user-images.githubusercontent.com/73446582/215438634-81faa265-52d8-4b24-829b-a5b0cab2258e.png)
4. (7000-7500)
![7000_7480](https://user-images.githubusercontent.com/73446582/215438820-f6eb42fb-f8eb-4ecb-9a1a-d16423ac8130.png)
5. (7500-8000)
![7500_7980](https://user-images.githubusercontent.com/73446582/215438644-2f60bbcd-f26d-409d-b0f3-e4bf1ab97c62.png)
6. (8000-8500)
![8000_8480](https://user-images.githubusercontent.com/73446582/215438657-f0afc67e-8634-455c-a4fa-60074fdf76f5.png)
7. (8500-9000)
![8500_8980](https://user-images.githubusercontent.com/73446582/215438664-291fe3a9-70f5-4c0c-b5fe-a09c3720a035.png)
...
420. (215000-215500)
![215000_215480](https://user-images.githubusercontent.com/73446582/215439556-78824537-83e1-4d3f-8da8-004b9afb01b1.png)
439. (224000-225500)
![224500_224980](https://user-images.githubusercontent.com/73446582/215439792-e83f72df-3400-4bf0-bcfa-a4cc7cce0485.png)



#### TO DO:
- Shared memory extension, non-coalesced extension.
- Figures for each of two methods. 
