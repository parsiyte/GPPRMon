import csv
import numpy as np

def collect_profiling_metrics(l1d, l2, dram, kernel, frequency, last_point):
#  print(frequency, last_point)
  baseline_path = "../runtime_profiling_metrics/memory_accesses/kernel_" + str(kernel)
  l1d_path = baseline_path + "/l1d"
  l2_path = baseline_path + "/l2"
  dram_path = baseline_path + "/dram"

  last_cycle = 0
  file_sequence = int(last_point / 1000000)

  eof = False

  l1d_array = np.zeros((l1d,6), dtype = int)
  for i in range(0, l1d):
    if file_sequence == 0:
      path = l1d_path + "/l1d_" + str(i) + ".csv" 
    else:
      path = l1d_path + "/l1d_" + str(i) + "_" + str(file_sequence + 1) + ".csv"

    file = open(path, 'r')
    reader = csv.reader(file)
    for row in reader:
      if "cycle" not in row and (int(row[0]) < (frequency + last_point)) and (int(row[0]) >= last_point):
        l1d_array[i][0] += int(row[1])
        l1d_array[i][1] += int(row[2])
        l1d_array[i][2] += int(row[3])
        l1d_array[i][3] += int(row[4])
        l1d_array[i][4] += int(row[5])
        l1d_array[i][5] += int(row[5])
      if row == None:
        eof = True
    file.close()
    
  l2_array = np.zeros((l2,6), dtype = int)
  for i in range(0, l2):
    if file_sequence == 0:
      path = l2_path + "/l2_" + str(i) + ".csv" 
    else:
      path = l2_path + "/l2_" + str(i) + "_" + str(file_sequence + 1) + ".csv"

    file = open(path, 'r')
    reader = csv.reader(file)
    c = 0
    for row in reader:
      if "cycle" not in row and (int(row[0]) < (frequency + last_point)) and (int(row[0]) >= last_point):
        l2_array[i][0] += int(row[1])
        l2_array[i][1] += int(row[2])
        l2_array[i][2] += int(row[3])
        l2_array[i][3] += int(row[4])
        l2_array[i][4] += int(row[5])
        l2_array[i][5] += int(row[5])
      if row == None:
        eof = True
    file.close()

  dram_array = np.zeros((dram, 2), dtype = int)
  for i in range(0, dram):
    if file_sequence == 0:
      path = dram_path + "/dram_" + str(i) + ".csv" 
    else:
      path = dram_path + "/dram_" + str(i) + "_" + str(file_sequence + 1) + ".csv"

    file = open(path, 'r')
    reader = csv.reader(file)
    for row in reader:
      if "cycle" not in row and (int(row[0]) < (frequency + last_point)) and (int(row[0]) >= last_point):
        dram_array[i][0] += int(row[1])
        dram_array[i][1] += int(row[2])
        last_cycle = int(row[0])
    file.close()

  return l1d_array, l2_array, dram_array, last_cycle