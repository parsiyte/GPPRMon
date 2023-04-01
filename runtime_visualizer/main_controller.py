import numpy as np
import time
import os
import subprocess
import csv

from os.path import isfile

# Performance metric collection functions
from metricCollector import collectProfilingMetricsMem
from metricCollector import ctaInstructionMonitoringAtIssue
from metricCollector import ctaInstructionMonitoringAtCompletion
from metricCollector import IPC

#from instructionMonitor import per_cluster_inst_window
from systemControlFunctions import newKernelQuery
from systemControlFunctions import isPathExists

# Processing collected metrics
from metricManipulator import calculatePlotRatesMetricsMem
from metricManipulator import calculatePlotRatesMetricsPower
from metricManipulator import lastCycleCheck

# Power metrics collection functions
from powerMetricsCollector import collectPowerMetricsCore
from powerMetricsCollector import collectPowerMetricsMemoryController
from powerMetricsCollector import collectPowerMetricsGPUComponents

# Determine GPU and architecture specs
from architectureInformation import collectArchitectureInformation

# Coordinate generator per GPU
from coordinateGenerator import plot

def get_config_information():
  file = open("plot.config", 'r')
  total_lines = len(file.readlines())
  file.close()

  global gpu_plot_en, core_plot_en, mem_hiear_plot_en, sampling_freq_en, arch_name, cta_ids_to_be_collected
  global sim_file
  file = open("plot.config", 'r')
  for i in range(0, total_lines):
    line = file.readline()
    if "-plot_gpu" in line:
      gpu_plot_en = int(line[len("-plot_gpu "):len(line)-1])
    elif "-plot_memory_hiearchy" in line:
      mem_hiear_plot_en = int(line[len("-plot_memory_hiearchy "):len(line)-1])
    elif "-plot_core" in line:
      core_plot_en = int(line[len("-plot_core "):len(line)-1])
    elif "-sampling_frequency" in line:
      sampling_freq_en = int(line[len("-sampling_frequency "):len(line)-1])
    elif "-arch_name" in line:
      arch_name = line[len("-arch_name "):len(line)-1]
    elif "-cta_ids" in line:
      if "all" in line:
        cta_ids_to_be_collected = "all"
      else:
        ctas = line[len("-cta_ids "):]
        id_tmp = ""
        for j in range (0, len(ctas)):
          if ctas[j] != ',' and ctas[j] != '\n':
            id_tmp += ctas[j]
          if ctas[j] == ',' or ctas[j] == '\n':
            cta_ids_to_be_collected.append(int(id_tmp))
            id_tmp = ""
    elif "-simulation_file_output" in line:
      sim_file = line[len("-simulation_file_output "): len(line)-1]
  file.close()

def sm_metrics(int_start, int_finish, cta_id, kid, cid):
  seq = int(int_start / 1000000)
  issued_path = ""
  completion_path = ""
  if seq == 0:
    issued_path = "../runtime_profiling_metrics/memory_accesses/kernel_" + str(kid) + "/inst_prof/" \
                  + "inst_mon_issue_" + str(cid) + ".csv"
    completion_path = "../runtime_profiling_metrics/memory_accesses/kernel_" + str(kid) + "/inst_prof/" \
                  + "inst_mon_completion_" + str(cid) + ".csv"
  else:
    issued_path = "../runtime_profiling_metrics/memory_accesses/kernel_" + str(kid) + "/inst_prof/" \
                  + "inst_mon_issue_" + str(cid) + "_" + str(seq + 1) + ".csv"
    completion_path = "../runtime_profiling_metrics/memory_accesses/kernel_" + str(kid) + "/inst_prof/" \
                  + "inst_mon_completion_" + str(cid) +  "_"  +str(seq + 1) + ".csv"

  instructions_issued = ctaInstructionMonitoringAtIssue(issued_path, cta_id, int_start, int_finish)
  instructions_completed = ctaInstructionMonitoringAtCompletion(completion_path, cta_id, int_start, int_finish)
  return instructions_issued, instructions_completed

def mem_metrics(nofL1D, nofL2, nofDRAM, kernel, int_start, int_finish, core, mem, gpu):
  l1dArr = []
  l2Arr = []
  dramArr = []

  if mem == 1 or gpu == 1:
    l1dArr, l2Arr, dramArr = collectProfilingMetricsMem(nofL1D, nofL2, nofDRAM, kernel, int_start, int_finish, 
                                                        True, True, True)

  elif core == 1:
    l1dArr, l2Arr, dramArr = collectProfilingMetricsMem(nofL1D, nofL2, nofDRAM, kernel, int_start, int_finish,
                                                        True, False, False)

  l1d_res, l2_res, dram_res = calculatePlotRatesMetricsMem(l1dArr, l2Arr, dramArr)
  return l1d_res, l2_res, dram_res

def ipc_metrics(l1d, int_start, int_finish, kernel):
  return IPC(l1d,  int_start, int_finish, kernel)  


# core, mem_controller, gpu = power_metrics(start, finalize, kernel, core_plot_en, mem_hiear_plot_en, gpu_plot_en)
def power_metrics(int_start, int_finish, kid, core, mem, gpu):
  mem_controller_items = ['mc_fee', 'mc_phy', 'mc_te', 'mc_total']
  gpu_component = ['proc_total', 'proc_cores', 'proc_l2', 'proc_mcs', 'proc_nocs']
  core_items = ['eu_core', 'inst_fu_core', 'idle_core', 'ldst_core', 'total_core']

  mem_controller_power_metrics = {}
  core_power_metrics = {}
  gpu_total_power_metrics = {}

  if core == True:
    for i in core_items:
      core_power_metrics[i] = collectPowerMetricsCore(int_start, int_finish, kid, i)
    core_power_metrics = calculatePlotRatesMetricsPower(core_power_metrics, True, False, False)

  if mem == True:
    for i in mem_controller_items:
      mem_controller_power_metrics[i] = collectPowerMetricsMemoryController(int_start, int_finish, kid, i)
    mem_controller_power_metrics = calculatePlotRatesMetricsPower(mem_controller_power_metrics, False, True, False)

  if gpu == True:
    for i in gpu_component:
      gpu_total_power_metrics[i] = collectPowerMetricsGPUComponents(int_start, int_finish, kid, i)
    gpu_total_power_metrics = calculatePlotRatesMetricsPower(gpu_total_power_metrics, False, False, True)

  return core_power_metrics, mem_controller_power_metrics, gpu_total_power_metrics


def calculate_cta_for_ith_cluster(int_start, int_finish, kid, cluster_id):
  path = "../runtime_profiling_metrics/memory_accesses/kernel_" + str(kid) + "/inst_prof/" 
  seq = int(int_start / 1000000)
 
  path_iss = ""
  path_comp = ""
  if seq == 0:
    path_iss= path + "inst_mon_issue_" + str(cluster_id) + ".csv"
    path_comp = path + "inst_mon_completion_" + str(cluster_id) + ".csv"
  else:
    path_iss = path + "inst_mon_issue_" + str(cluster_id) + "_" + str(seq + 1) + ".csv"
    path_comp = path + "inst_mon_completion_" + str(cluster_id) + "_" + str(seq + 1) + ".csv"
  
  file = open(path_iss, 'r')
  reader = csv.reader(file) 
  ctas = []
  for row in reader:
    if ("cycle" not in row) and (int(row[3]) == cluster_id) and (int(row[0]) >= int_start and int(row[0]) < int_finish):
      ctaid = int(row[2])
      if ctaid not in ctas:
        ctas.append(ctaid)
  file.close()

  file = open(path_comp, 'r')
  reader = csv.reader(file) 
  for row in reader:
#    print(row)
    if ("cycle" not in row) and (int(row[3]) == cluster_id) and (int(row[0]) >= int_start and int(row[0]) < int_finish):
      ctaid = int(row[2])
      if ctaid not in ctas:
        ctas.append(ctaid)
  file.close()

  return ctas

def last_cycle_check(core_plot_en, mem_hiear_plot_en, gpu_plot_en, kernel, start, finish):
  base_path = "../runtime_profiling_metrics/memory_accesses/kernel_" + str(kernel)
  if core_plot_en:
    seq = int(start / 1000000)
    path = ""
    if seq == 0:
      path = base_path + "/ipc/ipc.csv"
    else:
      path = base_path + "/ipc/ipc_" + str(seq + 1) + ".csv"

    cycle = 0
    file = open(path, 'r')
    reader = csv.reader(file) 
    for row in reader:
      if ("cycle" not in row):
        cycle = int(row[0])
      if cycle > finish:
        break
    file.close()
    return cycle

  elif mem_hiear_plot_en or gpu_plot_en:
    seq = int(start / 1000000)
    path = ""
    if seq == 0:
      path = base_path + "/l2/l2_0.csv"
    else:
      path = base_path + "/l2_0_" + str(seq + 1) + ".csv"

    cycle = 0
    file = open(path, 'r')
    reader = csv.reader(file) 
    for row in reader:
      if ("cycle" not in row):
        cycle = int(row[0])
      if cycle > finish:
        break
    file.close()
    return cycle

def checkNofActiveSM(sim_output_file, kernel):
  file = open(sim_output_file, 'r')
  nofLine = len(file.readlines())
  file.close()

  file = open(sim_output_file, 'r')
  counter = 0
  for i in range(0, nofLine):
    line = file.readline()
    if ("bind to kernel " + str(kernel+1)) in line:
      counter += 1
  file.close()
  return counter

def kernelSpecs(sim_output_file, kernel):
  file = open(sim_output_file, 'r')
  nofLine = len(file.readlines())
  file.close()

  file = open(sim_output_file, 'r')
  kernel_id_counter = 0
  grid = ""
  block = ""
  for i in range(0, nofLine):
    line = file.readline()
    if "gridDim=" in line:
      kernel_id_counter += 1

    if (kernel_id_counter - 1) == kernel and "gridDim=" in line:
      line_idx = 0
      grid_found = False
      while True:
        if line[line_idx] == '(' and grid_found == False:
          while True:
            if line[line_idx] != ')':
              grid += line[line_idx]
              line_idx += 1
            else:
              line_idx += 1
              grid_found = True
              grid += ')'
              break
        if line[line_idx] == '(' and grid_found == True:
          while True:
            if line[line_idx] != ')':
              block += line[line_idx]
              line_idx += 1
            else:
              line_idx += 1
              block += ')'
              break
          break
        line_idx += 1
      break
  
  file.close()
  return grid, block
# GPGPU-Sim PTX: pushing kernel '_Z11mvt_kernel2PfS_S_' to stream 0, gridDim= (1,1,1) blockDim = (1024,1,1) 
  
subprocess.run(["mkdir", "plot_results"])
gpu_plot_en = 0
core_plot_en = 0
mem_hiear_plot_en = 0
sampling_freq_en = 0
arch_name = ""
cta_ids_to_be_collected = []
sim_file = ""
get_config_information()

if gpu_plot_en:
  subprocess.run(["mkdir", "plot_results/gpu_average"])
if core_plot_en:
  subprocess.run(["mkdir", "plot_results/SMs"])
if mem_hiear_plot_en:
  subprocess.run(["mkdir", "plot_results/memory"])

nofL1D, nofL2, nofDRAM, nofSM, ker_launch_lat = collectArchitectureInformation(arch_name)

nofL1D = 8
nofSM = 8
nofL2 = 16
nofDRAM = 8

print("-" * 80)
print("Architecture name : " + str(arch_name))
print("Total number of SM and L1D cache : " + str(nofL1D))
print("Total number of memory partitions and DRAM : " + str(nofDRAM))
print("Number of sub_partition = 2, and Total number of L2 cache : " + str(nofL2))
print("Here, program will plot results for: ")
if gpu_plot_en:
  print("\t - on average memory usage, IPC, power consumption and application information of GPU")
if core_plot_en:
  print("\t - Instruction monitoring, IPC, L1D cache, and power consumption metrics of the core")
if mem_hiear_plot_en:
  print("\t - Memory hiearchy utilization and throughput values in terms of hits and misses")
print("-" * 80)

kid = 1
nofActiveSM = 0
start = ker_launch_lat
finish = ker_launch_lat + sampling_freq_en

while True:
  kernel_exists = False
  new_kernel_timer = 0
  while kernel_exists == False:
    kernel_exists = os.path.isfile("../runtime_profiling_metrics/kernel_" + str(kid))
    if kernel_exists == False:
      time.sleep(1)
      new_kernel_timer += 1
    else:
      nofActiveSM = checkNofActiveSM("../" + str(sim_file), kid)
      grid_size, cta_size = kernelSpecs("../" + str(sim_file), kid)

    if new_kernel_timer > 150:
      print(str(kid-1) + "'th kernel is the last kernel")
      exit()

  while True:
    if (start - ker_launch_lat) % (sampling_freq_en * 10) == 0:
      print("Plotting [" + str(start) + "-" + str(start + sampling_freq_en * 10) + "] cycle interval for " + str(kid) + "'th kernel")

    kernel_continue_timer = 0
    while True:
      last_cycle = last_cycle_check(core_plot_en, mem_hiear_plot_en, gpu_plot_en, kid, start, finish)
      this_kernel_completed = False
      if last_cycle < finish:
        time.sleep(1)
        kernel_continue_timer += 1
        if kernel_continue_timer > 100:
          this_kernel_completed = True
          break
      else:
        break
    
    if this_kernel_completed:
      kid += 1
      start = ker_launch_lat 
      finish = ker_launch_lat + sampling_freq_en
      break

    ipc_rates = []

    l1_met = []
    l2_met = []
    dram_met = []

    pow_core = []
    pow_mem_controller = []
    pow_gpu = []

    if core_plot_en or gpu_plot_en:
      ipc_rates = ipc_metrics(nofSM, start, finish, kid)

    if core_plot_en:
      l1_met, l2_met, dram_met = mem_metrics(nofL1D, nofL2, nofDRAM, kid, start, finish, True, False, False)
      pow_core, pow_mem_controller, pow_gpu = power_metrics(start, finish, kid, True, False, False)
      for i in range(0, nofSM):
        ctas_for_ith_cluster = calculate_cta_for_ith_cluster(start, finish, kid, i)
        for j in ctas_for_ith_cluster:
          if cta_ids_to_be_collected == "all" or j in cta_ids_to_be_collected:
            issued, completed = sm_metrics(start, finish, j, kid, i) #sm_metrics(start, finalize, cta_id, kernel, cluster_id)
            #def plot(l1d, l2, dram, core, mem, gpu, arch, kernel, cta_iss, cta_comp, cluster_id, cta_id, ipc_rate,
            #         power_core, power_mem, power_total, int_start, int_finish, nof_active_SMs, grid_size, cta_size):
            plot(l1_met, l2_met, dram_met, True, False, False, arch_name, kid, issued, completed, i, j, ipc_rates,
                 pow_core, None, pow_gpu, start, finish, None, None, None)

    if mem_hiear_plot_en or gpu_plot_en: 
      l1_met, l2_met, dram_met = mem_metrics(nofL1D, nofL2, nofDRAM, kid, start, finish, False, True, True)
      pow_core, pow_mem_controller, pow_gpu = power_metrics(start, finish, kid, False, True, True)

    if mem_hiear_plot_en:
      plot(l1_met, l2_met, dram_met, False, True, False, arch_name, kid, None, None, 0, 0, None,
           None, pow_mem_controller, None, start, finish, None, None, None)

    if gpu_plot_en:
      plot(l1_met, l2_met, dram_met, False, False, True, arch_name, kid, None, None, None, None, ipc_rates,
           None, None, pow_gpu, start, finish, nofActiveSM, grid_size, cta_size)

    start += sampling_freq_en
    finish += sampling_freq_en

# 2107105 fulya hanım
# 2103422 özgür bey.


