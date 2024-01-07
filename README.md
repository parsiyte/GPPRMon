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
# That command sets the environment variables so that the simulator can find related executables in the linkage path.
# If you want to debug the simulator (as it was written in C/C++), you should specify build_type as `debug`.
# Otherwise, you do not need to specify it; blank as empty. It will automatically build the executables with `release` version.
```
```console
user@gpgpu_sim:~$ make     #To compile source files, create and link the executable files of the simulator.
user@gpgpu_sim:~$ make clean      #To clean the simulator executables
``` 
Moreover, if you want to generate documentation files whose dependencies are specified as optional, you must first install the dependencies. Afterward, you can obtain the docs with 
```console
user@gpgpu_sim:~$ make docs     # Generates doxygen files describing simulator elements 
user@gpgpu_sim:~$ make cleandocs  	# Deletes pre-generated doxygen files if they exist.
``` 
The generated documentation with doxygen eases understanding classes, templates, functions, etc., for the simulator.

## 2. Tracking Runtime Memory Access on L1D, L2 and DRAM
During the simulation, the simulator creates memory access information in the below path.  
```console
user@gpgpu_sim/runtime_profiling_metrics/memory_accesses:~$
``` 
To enable memory access metric collection, one needs to specify the below flags in the `gpgpusim.config` file.

| Flags | Descriptions | Default value |
|:------|:-------------|:--------------|
| -mem_profiler | Enabling collecting memory access metrics | 0 = off |
| -mem_runtime_stat | Determining the sampling frequency for the metric collection | 100 (record after each 100 GPU cycles) |
| -IPC_per_prof_interval | Recording IPC rates for each metric collection sample | 0 = do not collect | 
| -instruction_monitor | Recording issue/completion stats of the instructions | 0 = do not collect |
| -L1D_metrics | Recording metrics for L1D cache accesses | 0 = do not collect |
| -L2_metrics | Recordingollecting metrics for L2 cache accesses | 0 = do not collect |
| -DRAM_metrics | Recording metrics for DRAM accesses | 0 = do not collect |
| -store_enable | Recording metrics for both store and load instructions | 0 = just record metrics for load |
| -accumulate_stats | Accumulating collected metrics | 0 = do not accumulate | 

## 3. Tracking Runtime Power Consumption of GPU and Sub-components
During simulation, the simulator records power consumption metrics in the below path.
```console
user@gpgpu_sim/runtime_profiling_metrics/energy_consumption:~$
```
The simulator will create separate folders and power profiling metrics for each kernel at runtime. For now, the below power consumption metrics are supported, but these metrics may be enhanced further to investigate sub-units independently.

> **GPU**  
>> **Core**
>>> **Execution Unit** (Register FU, Schedulers, Functional Units, etc.) <br>
>>> **Load Store Unit** (Crossbar, Shared Memory, Shared Mem Miss/Fill Buffer, Cache, Cache Prefetch Buffer, Cache WriteBack Buffer, Cache Miss Buffer, etc.) <br>
>>> **Instruction Functional Unit** (Instruction Cache, Branch Target Buffer, Decoder, Branch Predictor, etc.) <br>
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
| -power_simulation_enabled | Enableing collecting power consumption metrics | 0 = off |
| -gpgpu_runtime_stat | Determining the sampling frequency in terms of GPU cycle | 1000 cycles |
| -power_per_cycle_dump | Dumping detailed power output in each sample | 0 = off | 
| -dvfs_enabled | Turning on/off dynamic voltage frequency scaling for power model | 0 = not enabled| 
| -aggregate_power_stats | Recording issue/completion stats of the instructions | 0 = do not aggregate |
| -steady_power_levels_enabled | Producing a file for the steady power levels | 0 = off |
| -steady_state_definition | allowed deviation:number of samples | 8:4 |
| -power_trace_enabled | Producing a file for the power trace | 0 = off |
| -power_trace_zlevel | Compression level of the power trace output log | 6, (0=no comp, 9=highest) |
| -power_simulation_mode | Switch performance counter input for power simulation | 0, (0=Sim, 1=HW, 2=HW-Sim Hybrid) |

## 4. Visualizing Power Consumption, Memory Access and Core metrics

Our visualizer tool takes .csv files obtained via runtime simulation of a GPU kernel and generates three different visualization schemes. Currently, the simulator supports `GTX480_FERMI, QV100_VOLTA, RTX2060S_TURING, RTX2060_TURING, RTX3070_AMPERE, TITAN_KEPLER, TITANV_VOLTA, TITANX_PASCAL` GPUs currently. As each GPU has a different memory hierarchy, I designed varying schemes for each hierarchy. However, I designed SM and GPU visualizations as one such that their designs are applicable for each GPU.

1) A CTA's instruction issue/completion, Power consumption of the corresponding SM of and L1D usage of that SM. <br> 
 
![KID=0_onSM=1_withCTA=1_interval=55500_56000](https://user-images.githubusercontent.com/73446582/219937394-0df2a6ed-92a7-4198-8532-9a36b1df83c8.png)

The first visualization displays the instructions for the 1st CTA, which is mapped onto the 1st SM. While PC shows the instruction's pc, Opcode shows the operational codes of the instructions of the 1st thread block. Operands show the register IDs for the corresponding opcode of the instructions.

At the rightmost column (ISSUE/COMPLETION), the visualizer displays the issuing and completion information of the instructions for each warp in the first row and second row, respectively. For example, the first instruction is cvta.to.global.u64, whose PC is 656, is issued at the 55557th cycle by 7th warp and completed at the 55563rd cycle. 

This scheme shows a CTA's issued and completed instructions within a predetermined cycle interval. For the above example, this interval is the \[55500, 56000).  <br>

In addition, one may see the L1D cache usage and consumed runtime power measurements for the subcomponents of the SMs. The **RunTimeDynm** parameter represents the total consumed power for each section. Execution, functional and load/store units, and idle-core are the main sub-parts of an SM's power consumption. Also, IPC per SM is displayed at the bottom. <br> 

Also, we provide a display option for the average runtime memory access statistics and, IPC vs power dissipation among the units below.  
![Screenshot from 2024-01-07 16-47-19](https://github.com/parsiyte/GPPRMon/assets/73446582/c7a92ac7-de97-456c-b42f-406ba7d80ffc)


2) Access information on the memory units and power consumption of memory controller + DRAM units. <br>
 
![KID=0_memStatsForInterval=51000_51500](https://user-images.githubusercontent.com/73446582/219937330-5a3c4ed6-124a-44cb-95ff-5cd60c78a6c1.png)

The second visualization shows the accesses on L1D, L2 caches (as ``` hits, hit_reserved_status, misses, reservation_failures, sector_misses, and mshr_hits ```) and DRAM partitions (as ```row buffer hits and row buffer misses```) within the simulator interval. For caches, access descriptions are as follow:
 - **Hits:** Data is found in the corresponding sector of the line.
 - **Hit Reserved:** The line is allocated for the data, but the data does not arrive yet. Data will be located to the corresponding line and sector.
 - **Misses:** Miss is used for a cache line eviction. Line eviction is determined with a dirty counter. Replacement policy is determined via cache configuration.
 - **Reservation Failures:** Whenever an access cannot find the data in the cache, it tries to create a miss request in the MSHR buffer. When there is no slot to hold the corresponding miss in the buffer, it stalls the memory pipeline, and the status for this situation is a reservation failure. 
 - **Sector Misses:** When data is not found in the looked sector of the cache line, access status is the sector miss.
 - **MSHR Hits:** When data is not found in the looked sector of the cache line, and the miss request is already located in the MSHR buffer, it is recorded as MSHR hit. <br>

For DRAM, access descriptions are as follows:
 - **Row Buffer Hits:** The data looked for by the current instruction exists in the DRAM row buffer, which holds the element of the last access.
 - **Row Buffer Misses:** The data looked for by the current instruction does not exist in the row buffer.

3) GPU Throughput and Power Consumption <br>

GPUs mainly consist of SMs, which include functional units, register files and caches, NoCs, and memory partitions in which DRAM banks and L2 caches exist. For the configured architectures, the number of L1D caches is equal to SMs (SIMT Core Clusters), the number of DRAM banks is equal to the number of memory partitions, and the number of L2 caches is equal to twice the number of memory partitions. <br >

![KID=0_gpuAverageStatsForInterval=55000_55500](https://user-images.githubusercontent.com/73446582/219937405-6ea3e694-706f-4b1d-866a-8c198e45424e.png)

The third visualization shows the on-average L1D, L2 cache, and DRAM access statistics in the Memory Usage Metrics, average IPC among active SMs and Power Consumption Metrics of NoCs, memory partitions of L2 caches and MC+DRAM, and SMs. <br >


We have experimented the page ranking algorithm both on GV100 and RTX2060 S. Also, we have configured the GPU of Jetson AGX Xavier system on module, and emperimented the Fast Fouirer Transform Algorithm on it. Experimental profiling and displaying results are too large to upload here. However, we hold them into our local servers. If you want, we can transmit to any address. Do not hesitate contacting us for any of the result. 




