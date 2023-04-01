import numpy as np
import csv
import matplotlib.pyplot as plt

l1d_array = []
l2_array = []
dram_array = [] 

finish = 1999000
start = 1000000
freq = 200

def metric_calc_memory(l1d, l2, dram, nofl1d, nofl2, nofdram):
  dir_path = ""
  if l1d == True:
    dir_path = "../runtime_profiling_metrics/memory_accesses/kernel_1/l1d/l1d_"
  elif l2 == True:
    dir_path = "../runtime_profiling_metrics/memory_accesses/kernel_1/l2/l2_" 
  elif dram == True:
    dir_path = "../runtime_profiling_metrics/memory_accesses/kernel_1/dram/dram_" 

  if l1d == True or l2 == True:
    channel = 0
    if l1d == True:
      channel = nofl1d
    elif l2 == True:  
      channel = nofl2

    array = np.zeros((channel, int((finish-start)/freq), 6), dtype = int)
    sample = 0
    for i in range(0, channel):
      path = dir_path + str(i) + "_2.csv"
      file = open(path, 'r')
      reader = csv.reader(file)
      counter_1 = 0
      counter_2 = 0
      for row in reader:
        if "cycle" not in row and (int(row[0]) < finish) and (int(row[0]) >= start):
          array[i][counter_2][0] += int(row[1])    # hit accesses
          array[i][counter_2][1] += int(row[2])    # hit reserved accesses
          array[i][counter_2][2] += int(row[3])    # miss accesses
          array[i][counter_2][3] += int(row[4])    # reservation failures
          array[i][counter_2][4] += int(row[5])    # sector misses 
          array[i][counter_2][5] += int(row[6])    # mshr hits
          counter_1 += 1
          if counter_1 == 10: 
            counter_2 += 1
            counter_1 = 0
        if "cycle" not in row and int(row[0]) >= finish:
          sample = counter_2
          break
      file.close()

    av_arr = np.zeros((sample, 6), dtype = int)
    for i in range(0, sample):
      for j in range(0, channel):
        av_arr[i][0] += array[j][i][0]
        av_arr[i][1] += array[j][i][1]
        av_arr[i][2] += array[j][i][2]
        av_arr[i][3] += array[j][i][3]
        av_arr[i][4] += array[j][i][4]
        av_arr[i][5] += array[j][i][5]

    av_rates = np.zeros((6, sample), dtype = float)
    for i in range(0, sample):
      acc = 0
      for j in range(0, 5):
        acc += av_arr[i][j]

      for j in range(0, 5):
        av_rates[j][i] = float(av_arr[i][j]) / acc
      av_rates[5][i] = float(av_arr[i][5]) / av_arr[i][4]
    return av_rates

  elif dram == True:
    array = np.zeros((nofdram, int((finish-start)/freq), 6), dtype = int)
    sample = 0
    for i in range(0, nofdram):
      path = dir_path + str(i) + "_2.csv" 
      file = open(path, 'r')
      reader = csv.reader(file)
      counter_1 = 0
      counter_2 = 0
      for row in reader:
        if "cycle" not in row and (int(row[0]) < finish) and (int(row[0]) >= start):
          array[i][counter_2][0] += int(row[1])    # hit accesses
          array[i][counter_2][1] += int(row[2])    # hit reserved accesses
          counter_1 += 1
          if counter_1 == 10: 
            counter_2 += 1
            counter_1 = 0
        if "cycle" not in row and int(row[0]) >= finish:
          sample = counter_2
          break
      file.close()

    av_arr = np.zeros((sample, 2), dtype = int)
    for i in range(0, sample):
      for j in range(0, nofdram):
        av_arr[i][0] += array[j][i][0]
        av_arr[i][1] += array[j][i][1]
  
    av_rates = np.zeros((2, sample), dtype = float)
    for i in range(0, sample):
      acc = 0
      for j in range(0, 2):
        acc += av_arr[i][j]
      for j in range(0, 2):
        av_rates[j][i] = float(av_arr[i][j]) / acc
    return av_rates

def plot(l1d, l2, dram, exp):

  figure, axis = plt.subplots(3, 1)

  X = np.arange(start = start, stop = finish, step = freq)

  # For Sine Function
  axis[0].plot(X, l1d[0], color='g', label='Hit')
  axis[0].plot(X, l1d[1], color='b', label='Hit Reserved')
  axis[0].plot(X, l1d[2], color='r', label='Miss')
  axis[0].plot(X, l1d[3], color='m', label='Reservation Failure')
  axis[0].plot(X, l1d[4], color='y', label='Sector Miss')
  axis[0].plot(X, l1d[5], color='c', label='MSHR Hits')
  axis[0].set_title("Average L1D Access Statistics During Runtime")
  axis[0].set_ylabel("Access Rates")
  axis[0].legend(loc = 'upper right')
#  plt.legend()

  axis[1].plot(X, l2[0], color='g', label='Hit')
  axis[1].plot(X, l2[1], color='b', label='Hit Reserved')
  axis[1].plot(X, l2[2], color='r', label='Miss')
  axis[1].plot(X, l2[3], color='m', label='Reservation Failure')
  axis[1].plot(X, l2[4], color='y', label='Sector Miss')
  axis[1].plot(X, l2[5], color='c', label='MSHR Hits')
  axis[1].set_title("Average L2 Access Statistics During Runtime")
  axis[1].set_ylabel("Access Rates")
  
  # For Tangent Function
  axis[2].plot(X, dram[0], color='g', label='Row Buffer Hit')
  axis[2].plot(X, dram[1], color='c', label='Row Buffer Miss')
  axis[2].set_title("Average Row Buffer Access Statistics During Runtime")
  axis[2].set_ylabel("Access Rates")

  # Naming the x-axis, y-axis and the whole graph
  plt.xlabel("Cycles")
  plt.legend(loc = 'upper right')

  plt.show()

#l1d = metric_calc_memory(True, False, False, 80, 64, 32)
#l2 = metric_calc_memory(False, True, False, 80, 64, 32)
#dram = metric_calc_memory(False, False, True, 80, 64, 32)
#plot(l1d, l2, dram, None)


def ipc_col_calc(kernel, start_int, finish_int, freq, nofSM):

  path = "../runtime_profiling_metrics/memory_accesses/kernel_" + str(kernel) + "/ipc/"

  if start_int < 1000000:
    path = path + "ipc.csv" 

  else:
    rem = int(start_int / 1000000)
    path = path + "ipc_" + str(rem + 1) + ".csv" 

  ipc_rates =  []
  
  np.zeros(int((finish_int - start_int)/freq), dtype = float)

  file = open(path, 'r')
  reader = csv.reader(file) 
  counter = 0

  for row in reader:
    if "cycle" not in row and int(row[0]) >= start_int :
      if counter == 0:
        ipc_rates.append(0)

      for j in range(0, nofSM):
        if row[j+1] == '':
          ipc_rates[len(ipc_rates)-1] += 0
        else:
          ipc_rates[len(ipc_rates)-1] += float(row[j+1])
          
      counter += 1
      if counter == int(freq/20):
        counter = 0
        ipc_rates[len(ipc_rates)-1] = float(ipc_rates[len(ipc_rates)-1]/10)
 
    if "cycle" not in row and int((finish_int - start_int)/freq) == len(ipc_rates):
      break

  file.close()
  return ipc_rates

def power_col_calc(kernel, start_int, finish_int, freq):

  baseline_path = "../runtime_profiling_metrics/energy_consumption/kernel_" + str(kernel) 
  proc_total_path = baseline_path + "/f_processor.csv"
  proc_cores_path = baseline_path + "/f_p_total_cores.csv"
  proc_l2_path = baseline_path + "/f_p_total_l2.csv"
  proc_mcs_path = baseline_path + "/f_p_total_mcs.csv"
  proc_nocs_path = baseline_path + "/f_p_total_nocs.csv"

  metrics = {"total": [], "cores" : [], "l2": [], "mcs" : [], "nocs": []}

  file = open(proc_total_path, 'r')
  reader = csv.reader(file)
  counter = 0
  for row in reader:
#    print(row)
    if ("Cycle" not in row) and (start_int <= int(row[0])):
      if counter == 0:
        metrics["total"].append(float(row[7]))

      metrics["total"][len(metrics["total"])-1] += float(row[7])

      counter += 1
      if counter == 10:
        counter = 0

    if ("Cycle" not in row) and int((finish_int - start_int)/freq) == len(metrics["total"]):
      break
  file.close()

  for i in ["cores", "l2", "mcs", "nocs"]:
    if i == "cores":
      file = open(proc_cores_path, "r")
    if i == "l2":
      file = open(proc_l2_path, "r")
    if i == "mcs":
      file = open(proc_mcs_path, "r")
    if i == "nocs":
      file = open(proc_nocs_path, "r")
  
    reader = csv.reader(file)
    counter = 0
  
    for row in reader:
      if ("Cycle" not in row) and start_int <= int(row[0]):
        if counter == 0:
          metrics[i].append(float(row[5]))
        else:
          metrics[i][len(metrics[i])-1] += float(row[5])
  
        counter += 1
        if counter == 10:
          counter = 0

      if ("Cycle" not in row) and int((finish_int - start_int)/freq) == len(metrics[i]):
        break
    file.close()

  return metrics


def plot_2():

  kernel = 0
  start_int_1 = 5000
  finish_int_1 = 55000
  start_int_2 = 55000
  finish_int_2 = 105000
  start_int_3 = 105000
  finish_int_3 = 155000
  freq = 200
  nofSM = 8
  
  ipc_1 = ipc_col_calc(kernel, start_int_1, finish_int_1, freq, nofSM)
  ipc_2 = ipc_col_calc(kernel, start_int_2, finish_int_2, freq, nofSM)
  ipc_3 = ipc_col_calc(kernel, start_int_3, finish_int_3, freq, nofSM)
  power_metrics_1 = power_col_calc(kernel, start_int_1, finish_int_1, freq)
  power_metrics_2 = power_col_calc(kernel, start_int_2, finish_int_2, freq)
  power_metrics_3 = power_col_calc(kernel, start_int_3, finish_int_3, freq)

  X_1 = np.arange(start = start_int_1, stop = finish_int_1, step = freq)
  X_2 = np.arange(start = start_int_2, stop = finish_int_2, step = freq)
  X_3 = np.arange(start = start_int_3, stop = finish_int_3, step = freq)

  figure, axis = plt.subplots(3, 1)

  axis[0].plot(X_1, power_metrics_1["total"], color='r', label='Total Diss. Power', linewidth = 1)
  axis[0].plot(X_1, power_metrics_1["cores"], color='g', label='Pow on SMs', linewidth = 1)
  axis[0].plot(X_1, power_metrics_1["l2"], color='m',    label='Pow on L2', linewidth = 1)
  axis[0].plot(X_1, power_metrics_1["mcs"], color='y',   label='Pow on Mem. Part', linewidth = 1)
  axis[0].plot(X_1, power_metrics_1["nocs"], color='c',  label='Pow on InterCon. Net.', linewidth = 1)
  axis[0].set_ylabel("Dissipated Power", color="blue", fontsize=10)
  axis[0].set_xlabel("Cycles", fontsize = 10)
  axis[0].legend(loc = 'upper right')
  axis[0].set_title("IPC and Dissipated Power During Runtime [5000, 55000]")

  axis1=axis[0].twinx()
  axis1.plot(X_1, ipc_1, color='b', label='IPC', linewidth = 1.2, ls = 'dashed')
  axis1.set_ylabel("IPC rates", color='b', fontsize=10)
  axis1.legend(loc = 'upper left')

  axis[1].plot(X_2, power_metrics_2["total"], color='r', label='Total Diss. Power', linewidth = 1)
  axis[1].plot(X_2, power_metrics_2["cores"], color='g', label='Pow on SMs', linewidth = 1)
  axis[1].plot(X_2, power_metrics_2["l2"], color='m',    label='Pow on L2', linewidth = 1)
  axis[1].plot(X_2, power_metrics_2["mcs"], color='y',   label='Pow on Mem. Part', linewidth = 1)
  axis[1].plot(X_2, power_metrics_2["nocs"], color='c',  label='Pow on InterCon. Net.', linewidth = 1)
  axis[1].set_ylabel("Dissipated Power", color="blue", fontsize=10)
  axis[1].set_xlabel("Cycles", fontsize = 10)
#  axis[1].legend(loc = 'upper right')
  axis[1].set_title("IPC and Dissipated Power During Runtime [55000, 105000]")

  axis2=axis[1].twinx()
  axis2.plot(X_2, ipc_2, color='b', label='IPC', linewidth = 1.2, ls = 'dashed')
  axis2.set_ylabel("IPC rates", color='b', fontsize=10)
#  axis2.legend(loc = 'upper left')

  axis[2].plot(X_3, power_metrics_3["total"], color='r', label='Total Diss. Power', linewidth = 1)
  axis[2].plot(X_3, power_metrics_3["cores"], color='g', label='Pow on SMs', linewidth = 1)
  axis[2].plot(X_3, power_metrics_3["l2"], color='m',    label='Pow on L2', linewidth = 1)
  axis[2].plot(X_3, power_metrics_3["mcs"], color='y',   label='Pow on Mem. Part', linewidth = 1)
  axis[2].plot(X_3, power_metrics_3["nocs"], color='c',  label='Pow on InterCon. Net.', linewidth = 1)
  axis[2].set_ylabel("Dissipated Power", color="blue", fontsize=10)
  axis[2].set_xlabel("Cycles", fontsize = 10)
#  axis[2].legend(loc = 'upper right')
  axis[2].set_title("IPC and Dissipated Power During Runtime [105000, 155000]")

  axis3=axis[2].twinx()
  axis3.plot(X_3, ipc_3, color='b', label='IPC', linewidth = 1.2, ls = 'dashed')
  axis3.set_ylabel("IPC rates", color='b', fontsize=10)
#  axis3.legend(loc = 'upper left')

  plt.show()

#ipc = ipc_col_calc()
#power_metrics = power_col_calc()
plot_2()

