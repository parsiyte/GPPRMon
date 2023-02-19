1. [Prerequisites, Installing and Building the GPGPU-Sim v4.2](https://github.com/topcuburak/GPGPU-Sim_Runtime_MemAccess-EnergyConsumption_Profiler/blob/main/README.md#1-prerequisites-installing-and-building-the-gpgpu-sim-v42) <br >
   1.1. [Installing prerequisite libraries and simulator](https://github.com/topcuburak/GPGPU-Sim_Runtime_MemAccess-EnergyConsumption_Profiler/blob/main/README.md#installing-prerequisite-libraries-and-simulator) <br > 
   1.2. [Building simulator with doxygen files](https://github.com/topcuburak/GPGPU-Sim_Runtime_MemAccess-EnergyConsumption_Profiler/blob/main/README.md#building-simulator-with-doxygen-files) <br > 
2. [Tracking Runtime IPC, Instruction Monitoring, and Memory Accesses on L1D, L2, and DRAM ](https://github.com/topcuburak/GPGPU-Sim_Runtime_MemAccess-EnergyConsumption_Profiler/blob/main/README.md#2-tracking-runtime-memory-access-on-l1d-l2-and-dram) <br >
3. [Tracking Runtime Power Consumption of GPU and Sub-components](https://github.com/topcuburak/GPGPU-Sim_Runtime_MemAccess-EnergyConsumption_Profiler/blob/main/README.md#3-tracking-runtime-power-consumption-of-gpu-and-sub-components) <br >
4. [Visualizing Power Consumption, Memory Accesses, and Streaming Multiprocessor Metrics](https://github.com/topcuburak/GPGPU-Sim_Runtime_MemAccess-EnergyConsumption_Profiler/blob/main/README.md#4-visualizing-power-consumption-memory-access-and-core-metrics) <br />

## 1. Prerequisites, Installing and Building the GPGPU-Sim v4.2
Detailed documentation on GPGPU-Sim, what GPU models and architectures exist, how to configure it, and a guide to the source code can be found [here](http://gpgpu-sim.org/manual/). Also, detailed documentation on AccelWattch to collect power consumption metrics for subcomponents and a guide to the source code can be found [here](https://accel-sim.github.io/accelwattch.html).

### Installing prerequisite libraries and simulator
> **GPGPU-Sim dependencies:** ```gcc, g++, make, makedepend, xutils, bison, flex, zlib, CUDA Toolkit``` <br>
> (optional) **GPGPU-Sim documentation dependencies:** ```doxygen, graphvi``` <br>
> (optional) **AerialVision dependencies:** ```python-pmw, python-ply, python-numpy, libpng12-dev, python-matplotlib``` <br>
> **CUDA SDK dependencies:** ```libxi-dev, libxmu-dev, libglut3-dev```  <br> 

After installing prerequisite libraries to run the simulator properly, clone the accelWattch implementation of the simulator (GPGPU-Sim 4.2). Then, you should follow the below commands inside the simulator directory to build the simulator.

### Building simulator with doxygen files
```console
user@gpgpu_sim:~$ source setup_environment <build_type> 
# That command sets the environment variables such that simulator can find related executables in the linkage path. <br>
# If you want to debug the simulator (as it was written in C/C++), you should specify build_type as `debug` <br>
# Otherwise, you don't need to specify it, blank as empty. It will automatically build the executables wiht `release` version <br>
```


Then, 
```console
user@gpgpu_sim:~$ make
``` 
command builds the simulator compiling and creating executables. Furthermore, 
```console
user@gpgpu_sim:~$ make clean
``` 
command cleans the executables of the simulator. <br>

Also if you want to generate documentations files whose dependency files are specified as optional, you must first install the dependencies. Afterwards, you can obtain the docs with 
```console
user@gpgpu_sim:~$ make docs
``` 
and delete them with 
```console
user@gpgpu_sim:~$ make cleandocs
```
commands. These doxygen-generated documentation will help you to understand classes, templates, functions, etc.

## 2. Tracking Runtime Memory Access on L1D, L2 and DRAM
During the simulation, the simulator creates memory access information in the 
```console
user@gpgpu_sim/runtime_profiling_metrics/memory_accesses:~$
``` 
folder. To enable memory access metric collection, one needs to specify the below flags in the `gpgpusim.config` file.

| Flags | Descriptions | Default value |
|:------|:-------------|:--------------|
| -mem_profiler | Enables collecting memory access metrics | 0 = not enabled |
| -mem_runtime_stat | Sampling frequency for the metric collection | 100 = sample for each 100 GPU cycles |
| -IPC_per_prof_interval | Record IPC rates for each metric collection sample | 0 = do not collect | 
| -instruction_monitor | Record issue/completetion stats of the instructions | 0 = do not collect |
| -L1D_metrics | Enable collecting metrics for L1D cache accesses | 0 = do not collect |
| -L2_metrics | Enable collecting metrics for L2 cache accesses | 0 = do not collect |
| -DRAM_metrics | Enable collecting metrics for DRAM accesses | 0 = do not collect |
| -store_enable | Enable collecting metrics for both store and load instructions | 0 = just record metrics for load |
| -accumulate_stats | Accumulate collected metrics | 0 = not accumulate | 

## 3. Tracking Runtime Power Consumption of GPU and Sub-components
During simulation, the simulator records power consumption metrics in the 
```console
user@gpgpu_sim/runtime_profiling_metrics/energy_consumption:~$
```
folder. For each kernel, simulator will create seperate folders and power profiling metrics at runtime. For now, the below power consumption metrics is provided, but these metrics may be enhanced further to investigate sub-units in an independent manner.

> **GPU**  
>> **Core**
>>> **Execution Unit** (Register FU, Schedulers, Functional Units etc.) <br>
>>> **Load Store Unit** (Crossbar, Shared Memory, Shared Mem Miss/Fill Buffer, Cache, Cache Prefetch Buffer, Cache WriteBack Buffer, Cache Miss Buffer etc.) <br>
>>> **Instruction Functional Unit** (Instruction Cache, Branch Target Buffer, Decoder, Branch Predictor etc.) <br>
>>
>> **Network on Chip** <br>
>> **L2 Cache** <br>
>> **DRAM + Memory Controller** <br>
>>> **Frontend Engine** <br>
>>> **PHY Between Memory Controller and DRAM** <br>
>>> **Transaction Engine** (BackEnd Engine) <br>
>>> **DRAM** <br>

| Flags | Descriptions | Default value |
|:------|:-------------|:--------------|
| -power_simulation_enabled | Enables collecting power consumption metrics | 0 = not enabled |
| -gpgpu_runtime_stat | Sampling frequency in terms of GPU cycle | 1000 cycles |
| -power_per_cycle_dump | Dumps detailed power output in each sample | 0 = not enabled | 
| -dvfs_enabled | Turns on/off dynamic voltage frequency scaling for power model | 0 = not enabled| 
| -aggregate_power_stats | Record issue/completetion stats of the instructions | 0 = do not aggregate |
| -steady_power_levels_enabled | Produce a file for the steady power levels | 0 = off |
| -steady_state_definition | allowed deviation:number of samples | 8:4 |
| -power_trace_enabled | Produce a file for the power trace | 0 = off |
| -power_trace_zlevel | Compression level of the power trace output log | 6, (0=no comp, 9=highest) |
| -power_simulation_mode | Switch performance counter input for power simulation | 0, (0=Sim, 1=HW, 2=HW-Sim Hybrid) |

## 4. Visualizing Power Consumption, Memory Access and Core metrics

Our visualizer tool takes csv files obtained via run-time simulation of a GPU kernel, and generates three different visualization schemes Here, the simulator supports `GTX480_FERMI, QV100_VOLTA, RTX2060S_TURING, RTX2060_TURING, RTX3070_AMPERE, TITAN_KEPLER, TITANV_VOLTA, TITANX_PASCAL` GPUs currently. As each GPU has a different memory hiearchy, I designed different schemes for each hiearchy. However, I designed SM visualization and GPU visualization once, and used these schemes for all GPUs. 

1) A CTA's instruction issue/completion, Power consumption of the corresponding SM of and L1D usage of that SM. <br> 
![KID=0_onSM=1_withCTA=1_interval=55500_56000](https://user-images.githubusercontent.com/73446582/219937394-0df2a6ed-92a7-4198-8532-9a36b1df83c8.png)

The first visualization displays the instructions of the CTA_ID=0 which is mapped onto SM=1. PC shows the instruction's pcs, Opcode shows the operational codes of the instructions of thread block, operands are the registers for each opcodes of the instructions. At the right most column (ISSUE/COMPLETION), visualizer displays the issuing and completion information of the instructionns for each warp at the first row and second row respectively. For example, For the above png file, cvta.to.global.u64 instruction whose PC = 656 is issued at 55557'th cycle for warp 7, and completed at 55563'th cycle. This scheme shows the issued and completed instructions of a CTA within a predetermined cycle interval. For the above example this interval is the \[55500, 56000).  <br>
In addition, consumed run time power measurements is shown for the subcomponents of the SMs with the L1D cache usage. Total consumed power is represented by the **RunTimeDynm** parameter. Power components of an SM is calculated with four main parts as exe-units, functional-units, load-store units and idle-core. Also, IPC per SM is displayed at the bottom. <br> 

2) Access information on the memory units and power consumption of memory controller + DRAM units. <br>
![KID=0_memStatsForInterval=51000_51500](https://user-images.githubusercontent.com/73446582/219937330-5a3c4ed6-124a-44cb-95ff-5cd60c78a6c1.png)

The second visualization shows the accesses on L1D, L2 caches (as ``` hits, hit_reserved_status, misses, reservation_failures, sector_misses, and mshr_hits ```) and DRAM partitions (as ```row buffer hits and row buffer misses```) within the simulator interval. For caches, access descriptions are as following:
 - **Hits:** Data is found in the corresponding sector of the line.
 - **Hit Reserved:** The line is allocated for the data, but the data does not arrive yet. Data will be located to the corresponding line and sector.
 - **Misses:** Miss is used for a cache line eviction. Line eviction is determined with respect to a dirty counter. Replacement policy is determined via cache configuration.
 - **Reservation Failures:** Whenever an access cannot find the data in the cache, it tries to create a miss request in MSHR buffer. When there is no slot to hold the corresponding miss in the buffer, it stalls the memory pipeline and the status for this situation is the reservation failures. 
 - **Sector Misses:** When data is not found in the looked sector of the cache line, access status is the sector miss.
 - **MSHR Hits:** When data is not found in the looked sector of the cache line, and miss request is already located in the MSHR buffer, it is recorded as MSHR hit. <br>

For DRAM, access descriptions are as following:
 - **Row Buffer Hits:** Data is found in the corresponding sector of the line.
 - **Row Buffer Misses:** The line is allocated for the data, but the data does not arrive yet. Data will be located to the corresponding line and sector.

3) GPU Throughput and Power Consumption <br>
GPUs mainly consist of SMs ,which holds functional units, register files and caches, NoCs and memory partitions in which there are DRAM banks and L2 caches. For the configured architectures, the number of L1D cache is equal to SMs (SIMT Core Clusters), the number of DRAM banks is equal to the number of memory partition and the number of L2 caches is equal to the number of memory partition * 2. <br>
![KID=0_gpuAverageStatsForInterval=55000_55500](https://user-images.githubusercontent.com/73446582/219937405-6ea3e694-706f-4b1d-866a-8c198e45424e.png)

The third visualization shows the on average L1D, L2 cache and DRAM access statistics in the Memory Usage Metrics, average IPC among active SMs and Power Consumption Metrics of NoCs, memory partitions of L2 caches and MC+DRAM, and SMs.    

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
 - **sampling_cycle** is the run-time visualization interval. 
 - **arch_name** is the GPU name which may be ``` GTX480, TITAN, TITANX, RTX2060, RTX2060S, TITANV, QV100, RTX3070```

#### TO DO:
- Shared memory extension, non-coalesced extension.
- Figures for each of two methods. 
