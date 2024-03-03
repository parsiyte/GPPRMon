import numpy as np
import csv
import matplotlib.pyplot as plt
import sys 
# Determine GPU and architecture specs
from architectureInformation import collectArchitectureInformation


def l1d_metrics(nofl1d, kid, start, finish, freq):
  dir_path = "../runtime_profiling_metrics/memory_accesses/kernel_" + str(kid) + "/l1d/l1d_"

  intervals = []
  file = open(dir_path + "0.csv", 'r')
  reader = csv.reader(file)
  for row in reader:
    if "cycle" not in row:
      intervals.append(int(row[0]))
    if len(intervals) == 2:
      break
  file.close()

  # simulator sampling frequency
  simSampFreq = intervals[1] - intervals[0]
  startCycle = 0

  windowIntervalStart = 0
  if start > 999999:
    windowIntervalStart = int(start / 1000000)

  windowIntervalFinish = 0
  if finish > 999999:
    windowIntervalFinish = int(finish / 1000000)

  path = ""
  l1d = np.zeros((6, int((finish)/freq)), dtype = int)
  for i in range(windowIntervalStart, windowIntervalFinish + 1):
    for j in range (0, nofl1d):
      if i > 0:
        path = dir_path + str(j) + "_" + str(i+1) + ".csv"
      else:
        path = dir_path + str(j) + ".csv"

      file = open(path, 'r')
      reader = csv.reader(file)

      hits = 0
      hitReses = 0
      misses = 0
      resFails = 0
      secMisses = 0
      mshrHits = 0
      cycle = 0
      for row in reader:
        if "cycle" not in row and (int(row[0]) < finish) and (int(row[0]) >= start):
          cycle = int(row[0])
          hits += int(row[1])    # hit accesses
          hitReses += int(row[2])    # hit reserved accesses
          misses += int(row[3])    # miss accesses
          resFails += int(row[4])    # reservation failures
          secMisses += int(row[5])    # sector misses 
          mshrHits += int(row[6])    # mshr hits

        if "cycle" not in row and cycle % freq == 0 and (int(row[0]) < finish) and (int(row[0]) >= start):
          l1d[0][int(cycle / freq)] += hits    # hit accesses
          l1d[1][int(cycle / freq)] += hitReses    # hit reserved accesses
          l1d[2][int(cycle / freq)] += misses    # miss accesses
          l1d[3][int(cycle / freq)] += resFails    # reservation failures
          l1d[4][int(cycle / freq)] += secMisses    # sector misses 
          l1d[5][int(cycle / freq)] += mshrHits    # mshr hits
          hits = 0
          hitReses = 0
          misses = 0
          resFails = 0
          secMisses = 0
          mshrHits = 0

        if cycle >= finish:
          break
      file.close()

  total_access = 0 
  total_misses = 0
  l1dRes = [[], [], [], [], [], []]

  for i in range(0, len(l1d[0])):
    for j in range(0, 6): # hit, hit_res, miss, res_fail, sec_miss, mshr_hit.
      if j in [0,1,2,3,4]:
        total_access += l1d[j][i]
      if j in [2,4]:
        total_misses += l1d[j][i]

    for j in range(0, 6):
      if j != 5:
        if total_access == 0:
          l1dRes[j].append(0)  
        else:
          l1dRes[j].append(float(l1d[j][i]) / total_access)
      else:
        if total_misses == 0:
          l1dRes[j].append(0)  
        else:
          l1dRes[j].append(float(l1d[j][i]) / total_misses)

    total_access = 0 
    total_misses = 0

#  print(l1dRes)
  return l1dRes

def l2_metrics(nofl2, kid, start, finish, freq):
  dir_path = "../runtime_profiling_metrics/memory_accesses/kernel_" + str(kid) + "/l2/l2_"
  intervals = []
  file = open(dir_path + "0.csv", 'r')
  reader = csv.reader(file)
  for row in reader:
    if "cycle" not in row:
      intervals.append(int(row[0]))
    if len(intervals) == 2:
      break
  file.close()

  # simulator sampling frequency
  simSampFreq = intervals[1] - intervals[0]
  startCycle = 0

  windowIntervalStart = 0
  if start > 999999:
    windowIntervalStart = int(start / 1000000)

  windowIntervalFinish = 0
  if finish > 999999:
    windowIntervalFinish = int(finish / 1000000)

  path = ""
  l2 = np.zeros((6, int((finish)/freq)), dtype = int)
  for i in range(windowIntervalStart, windowIntervalFinish + 1):
    for j in range (0, nofl2):
      if i > 0:
        path = dir_path + str(j) + "_" + str(i+1) + ".csv"
      else:
        path = dir_path + str(j) + ".csv"
      file = open(path, 'r')
      reader = csv.reader(file)

      hits = 0
      hitReses = 0
      misses = 0
      resFails = 0
      secMisses = 0
      mshrHits = 0
      cycle = 0
      for row in reader:
        if "cycle" not in row and (int(row[0]) < finish) and (int(row[0]) >= start):
          cycle = int(row[0])
          hits += int(row[1])    # hit accesses
          hitReses += int(row[2])    # hit reserved accesses
          misses += int(row[3])    # miss accesses
          resFails += int(row[4])    # reservation failures
          secMisses += int(row[5])    # sector misses 
          mshrHits += int(row[6])    # mshr hits

        if "cycle" not in row and cycle % freq == 0 and (int(row[0]) < finish) and (int(row[0]) >= start):
          l2[0][int(cycle / freq)] += hits    # hit accesses
          l2[1][int(cycle / freq)] += hitReses    # hit reserved accesses
          l2[2][int(cycle / freq)] += misses    # miss accesses
          l2[3][int(cycle / freq)] += resFails    # reservation failures
          l2[4][int(cycle / freq)] += secMisses    # sector misses 
          l2[5][int(cycle / freq)] += mshrHits    # mshr hits
          hits = 0
          hitReses = 0
          misses = 0
          resFails = 0
          secMisses = 0
          mshrHits = 0

        if cycle >= finish:
          break
      file.close()

  total_access = 0 
  total_misses = 0
  l2Res = [[], [], [], [], [], []]
  for i in range(0, len(l2[0])):
    for j in range(0, 6): # hit, hit_res, miss, res_fail, sec_miss, mshr_hit.
      if j in [0,1,2,3,4]:
        total_access += l2[j][i]
      if j in [2,4]:
        total_misses += l2[j][i]

    for j in range(0, 6):
      if j != 5:
        if total_access == 0:
          l2Res[j].append(0)  
        else:
          l2Res[j].append(float(l2[j][i]) / total_access)
      else:
        if total_misses == 0:
          l2Res[j].append(0)
        else:
          l2Res[j].append(float(l2[j][i]) / total_misses)
    total_access = 0 
    total_misses = 0

  return l2Res

def dram_metrics(nofdram, kid, start, finish, freq):
  dir_path = "../runtime_profiling_metrics/memory_accesses/kernel_" + str(kid) + "/dram/dram_"
  intervals = []
  file = open(dir_path + "0.csv", 'r')
  reader = csv.reader(file)
  for row in reader:
    if "cycle" not in row:
      intervals.append(int(row[0]))
    if len(intervals) == 2:
      break
  file.close()

  # simulator sampling frequency
  simSampFreq = intervals[1] - intervals[0]
  startCycle = 0

  windowIntervalStart = 0
  if start > 999999:
    windowIntervalStart = int(start / 1000000)

  windowIntervalFinish = 0
  if finish > 999999:
    windowIntervalFinish = int(finish / 1000000)

  path = ""
  dram = np.zeros((2, int((finish)/freq)), dtype = int)
  for i in range(windowIntervalStart, windowIntervalFinish + 1):
    for j in range (0, nofdram):
      if i > 0:
        path = dir_path + str(j) + "_" + str(i+1) + ".csv"
      else:
        path = dir_path + str(j) + ".csv"
      file = open(path, 'r')
      reader = csv.reader(file)

      hits = 0
      misses = 0
      cycle = 0
      for row in reader:
        if "cycle" not in row and (int(row[0]) < finish) and (int(row[0]) >= start):
          cycle = int(row[0])
          hits += int(row[1])    # hit accesses
          misses += int(row[2])    # miss accesses

        if "cycle" not in row and cycle % freq == 0 and (int(row[0]) < finish) and (int(row[0]) >= start):
          dram[0][int(cycle / freq)] += hits    # hit accesses
          dram[1][int(cycle / freq)] += misses    # miss accesses
          hits = 0
          misses = 0

        if cycle >= finish:
          break
      file.close()

  total_access = 0 
  dramRes = [[], []]
  for i in range(0, len(dram[0])):
    for j in range(0, 2): # hit, miss.
      total_access += dram[j][i]
    for j in range(0, 2):
      if total_access == 0:
        dramRes[j].append(0)
      else:
        dramRes[j].append(float(dram[j][i]) / total_access)
    total_access = 0 
  return dramRes

def ipc_col_calc(nofl1d, kid, start, finish, freq):
  dir_path = "../runtime_profiling_metrics/memory_accesses/kernel_" + str(kid) + "/ipc/ipc"
  intervals = []
  file = open(dir_path + ".csv", 'r')
  reader = csv.reader(file)
  for row in reader:
    if "cycle" not in row:
      intervals.append(int(row[0]))
    if len(intervals) == 2:
      break
  file.close()

  # simulator sampling frequency
  simSampFreq = intervals[1] - intervals[0]
  startCycle = 0

  windowIntervalStart = 0
  if start > 999999:
    windowIntervalStart = int(start / 1000000)

  windowIntervalFinish = 0
  if finish > 999999:
    windowIntervalFinish = int(finish / 1000000)

  path = ""
  ipc = np.zeros((int((finish)/freq)), dtype = float)
  for i in range(windowIntervalStart, windowIntervalFinish + 1):
    if i > 0:
      path = dir_path + "_" + str(i+1) + ".csv"
    else:
      path = dir_path + ".csv"
    file = open(path, 'r')
    reader = csv.reader(file)

    ipc_per_interval = []
    for j in range (nofl1d):
      ipc_per_interval.append([])
    ipc_per_interval.append([])

    for row in reader:
      if "cycle" not in row and (int(row[0]) < finish) and (int(row[0]) >= start):
        for idx, val in enumerate(row):
          if idx == 0:
            ipc_per_interval[idx].append(int(val))
          else:
            ipc_per_interval[idx].append(float(val))

      if "cycle" not in row and int(row[0]) >= finish:
        break
    file.close()

    zeroIPCs = []
    for j in range (1, len(ipc_per_interval)):
      if sum(ipc_per_interval[j]) == 0:
        zeroIPCs.append(j)

    nofActiveSMs = nofl1d - len(zeroIPCs)

    for j in range(0, len(ipc_per_interval[0])):
      for k in range(1, len(ipc_per_interval)):
        ipc[int(ipc_per_interval[0][j]/freq)] += ipc_per_interval[k][j]
      ipc[int(ipc_per_interval[0][j]/freq)] = \
                    ipc[int(ipc_per_interval[0][j]/freq)] / nofActiveSMs
  return ipc

def power_col_calc(kid, start, finish, freq):
  baseline_path = "../runtime_profiling_metrics/energy_consumption/kernel_" + str(kid) 

  intervals = []
  file = open(baseline_path + "/f_processor.csv", 'r')
  reader = csv.reader(file)
  for row in reader:
    if "Cycle" not in row:
      intervals.append(int(row[0]))
    if len(intervals) == 2:
      break
  file.close()

  # simulator sampling frequency
  simSampFreq = intervals[1] - intervals[0]
  startCycle = 0

  windowIntervalStart = 0
  if start > 999999:
    windowIntervalStart = int(start / 1000000)

  windowIntervalFinish = 0
  if finish > 999999:
    windowIntervalFinish = int(finish / 1000000)

  pow_metrics = {}
  pow_metrics["total"] = np.zeros((int((finish)/freq)), dtype = float)
  proc_total_path = baseline_path + "/f_processor"
  path = ""
  for i in range(windowIntervalStart, windowIntervalFinish + 1):
    if i > 0:
      path = proc_total_path + "_" + str(i+1) + ".csv"
    else:
      path = proc_total_path + ".csv"
    file = open(path, 'r')
    reader = csv.reader(file)

    powCounter = 0
    cycle = 0
    for row in reader:
      if ("Cycle" not in row) and int(row[0]) < finish and (int(row[0]) >= start):
        powCounter += float(row[7])
        cycle = int(row[0])

      if cycle >= finish:
        break

      if "Cycle" not in row and cycle % freq == 0 and (int(row[0]) < finish) and (int(row[0]) >= start):
        pow_metrics["total"][int(cycle / freq)] += powCounter    # hit accesses
        powCounter = 0

    file.close()

  pow_metrics["cores"] = np.zeros((int((finish)/freq)), dtype = float)
  proc_cores_path = baseline_path + "/f_p_total_cores"
  for i in range(windowIntervalStart, windowIntervalFinish + 1):
    if i > 0:
      path = proc_cores_path + "_" + str(i+1) + ".csv"
    else:
      path = proc_cores_path + ".csv"
    file = open(path, 'r')
    reader = csv.reader(file)

    powCounter = 0
    cycle = 0
    for row in reader:
      if ("Cycle" not in row) and (int(row[0]) < finish) and (int(row[0]) >= start):
        powCounter += float(row[5])
        cycle = int(row[0])

      if cycle >= finish:
        break

      if "Cycle" not in row and cycle % freq == 0 and (int(row[0]) < finish) and (int(row[0]) >= start):
        pow_metrics["cores"][int(cycle / freq)] += powCounter    # hit accesses
        powCounter = 0
    file.close()

  pow_metrics["l2"] = np.zeros((int((finish)/freq)), dtype = float)
  proc_l2_path = baseline_path + "/f_p_total_l2"
  for i in range(windowIntervalStart, windowIntervalFinish + 1):
    if i > 0:
      path = proc_l2_path + "_" + str(i+1) + ".csv"
    else:
      path = proc_l2_path + ".csv"
    file = open(path, 'r')
    reader = csv.reader(file)

    powCounter = 0
    cycle = 0
    for row in reader:
      if ("Cycle" not in row) and (int(row[0]) < finish) and (int(row[0]) >= start) :
        powCounter += float(row[5])
        cycle = int(row[0])

      if cycle >= finish:
        break

      if "Cycle" not in row and cycle % freq == 0 and (int(row[0]) < finish) and (int(row[0]) >= start):
        pow_metrics["l2"][int(cycle / freq)] += powCounter    # hit accesses
        powCounter = 0
    file.close()

  pow_metrics["mcs"] = np.zeros((int((finish)/freq)), dtype = float)
  proc_mcs_path = baseline_path + "/f_p_total_mcs"
  for i in range(windowIntervalStart, windowIntervalFinish + 1):
    if i > 0:
      path = proc_mcs_path + "_" + str(i+1) + ".csv"
    else:
      path = proc_mcs_path + ".csv"
    file = open(path, 'r')
    reader = csv.reader(file)

    powCounter = 0
    cycle = 0
    for row in reader:
      if ("Cycle" not in row) and (int(row[0]) < finish) and (int(row[0]) >= start):
        powCounter += float(row[5])
        cycle = int(row[0])

      if cycle >= finish:
        break

      if "Cycle" not in row and cycle % freq == 0 and (int(row[0]) < finish) and (int(row[0]) >= start):
        pow_metrics["mcs"][int(cycle / freq)] += powCounter    # hit accesses
        powCounter = 0
    file.close()

  pow_metrics["nocs"] = np.zeros((int((finish)/freq)), dtype = float)
  proc_nocs_path = baseline_path + "/f_p_total_nocs"
  for i in range(windowIntervalStart, windowIntervalFinish + 1):
    if i > 0:
      path = proc_nocs_path + "_" + str(i+1) + ".csv"
    else:
      path = proc_nocs_path + ".csv"
    file = open(path, 'r')
    reader = csv.reader(file)

    powCounter = 0
    cycle = 0
    for row in reader:
      if ("Cycle" not in row) and (int(row[0]) < finish) and (int(row[0]) >= start):
        powCounter += float(row[5])
        cycle = int(row[0])

      if cycle >= finish:
        break

      if "Cycle" not in row and cycle % freq == 0 and (int(row[0]) < finish) and (int(row[0]) >= start):
        pow_metrics["nocs"][int(cycle / freq)] += powCounter    # hit accesses
        powCounter = 0
    file.close()

  return pow_metrics

def get_config_information():
  file = open("plot.config", 'r')
  total_lines = len(file.readlines())
  file.close()

  global gpu_plot_en, core_plot_en, mem_hierar_plot_en, sampling_freq_en, arch_name, cta_ids_to_be_collected
  global sim_file
  file = open("plot.config", 'r')
  for i in range(0, total_lines):
    line = file.readline()
    if "-plot_gpu" in line:
      gpu_plot_en = int(line[len("-plot_gpu "):len(line)-1])
    elif "-plot_memory_hiearchy" in line:
      mem_hierar_plot_en = int(line[len("-plot_memory_hiearchy "):len(line)-1])
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


def plot_statistics(l1dR, l2R, dramR, ipcR, power_metricsR, start, finish, freq):

  figure, axis = plt.subplots(4, 1)
  X = np.arange(start = 0, stop = finish, step = freq)

  axis[0].plot(X, l1dR[0], color='g', label='Hit')
  axis[0].plot(X, l1dR[1], color='b', label='Hit Reserved')
  axis[0].plot(X, l1dR[2], color='r', label='Miss')
  axis[0].plot(X, l1dR[3], color='m', label='Reservation Failure')
  axis[0].plot(X, l1dR[4], color='y', label='Sector Miss')
  axis[0].plot(X, l1dR[5], color='c', label='MSHR Hits')
  axis[0].set_title("Average L1D Access Statistics During Runtime")
  axis[0].set_ylabel("Access Rates")
  axis[0].legend(loc = 'upper right')

  axis[1].plot(X, l2R[0], color='g', label='Hit')
  axis[1].plot(X, l2R[1], color='b', label='Hit Reserved')
  axis[1].plot(X, l2R[2], color='r', label='Miss')
  axis[1].plot(X, l2R[3], color='m', label='Reservation Failure')
  axis[1].plot(X, l2R[4], color='y', label='Sector Miss')
  axis[1].plot(X, l2R[5], color='c', label='MSHR Hits')
  axis[1].set_title("Average L2 Access Statistics During Runtime")
  axis[1].set_ylabel("Access Rates")

  axis[2].plot(X, dramR[0], color='g', label='Row Buffer Hit')
  axis[2].plot(X, dramR[1], color='c', label='Row Buffer Miss')
  axis[2].set_title("Average Row Buffer Access Statistics During Runtime")
  axis[2].set_ylabel("Access Rates")

  axis[3].plot(X, power_metricsR["total"], color='r', label='Total Diss. Power', linewidth = 1)
  axis[3].plot(X, power_metricsR["cores"], color='g', label='Pow on SMs', linewidth = 1)
  axis[3].plot(X, power_metricsR["l2"], color='m',    label='Pow on L2', linewidth = 1)
  axis[3].plot(X, power_metricsR["mcs"], color='y',   label='Pow on Mem. Part', linewidth = 1)
  axis[3].plot(X, power_metricsR["nocs"], color='c',  label='Pow on InterCon. Net.', linewidth = 1)
  axis[3].set_ylabel("Dissipated Power (mW)", color="black", fontsize=10)
  axis[3].set_xlabel("Cycles", fontsize = 10)
  axis[3].legend(loc = 2)
  axis[3].set_title("IPC and Dissipated Power During Runtime")

  axis1=axis[3].twinx()
  axis1.plot(X, ipcR, color='b', label='IPC', linewidth = 1.2, ls = 'dashed')
  axis1.set_ylabel("IPC rates", color='black', fontsize=10)
  axis1.legend(loc = 1)

  plt.xlabel("Cycles")
  plt.show()

if __name__ == '__main__':
  gpu_plot_en = 0
  core_plot_en = 0
  mem_hierar_plot_en = 0
  sampling_freq_en = 0
  arch_name = ""
  cta_ids_to_be_collected = []
  sim_file = ""

  get_config_information()
  print(arch_name)
  nofL1D, nofL2, nofDRAM, nofSM, _ = collectArchitectureInformation(arch_name)
  print("Nof L1D: " + str(nofL1D))
  print("Nof L2: " + str(nofL2))
  print("Nof DRAM: " + str(nofDRAM))
  print("Nof SM: " + str(nofSM))

  kid = int(sys.argv[1])
  start = int(sys.argv[2])
  finish = int(sys.argv[3])
  freq = int(sys.argv[4])

  l1dR = l1d_metrics(nofL1D, kid, start, finish, freq)
  l2R = l2_metrics(nofL2, kid, start, finish, freq)
  dramR = dram_metrics(nofDRAM, kid, start, finish, freq)
  ipcR = ipc_col_calc(nofL1D, kid, start, finish, freq)
  power_metricsR = power_col_calc(kid, start, finish, freq)
  plot_statistics(l1dR, l2R, dramR, ipcR, power_metricsR, start, finish, freq)

