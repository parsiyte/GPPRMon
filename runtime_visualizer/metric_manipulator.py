import sys
import numpy as np
import time
import cv2
import os
import csv

from os import listdir
from os.path import isfile, join
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from coordinate_generator import plot
from metric_collector import collect_profiling_metrics
from architecture_info import collect_arch_info

args = sys.argv[1:]

def calculate_plot_rates(l1d_array, l2_array, dram_array):
  l1d_total = len(l1d_array)
  l2_total = len(l2_array)
  dram_total = len(dram_array)

  result_l1d = np.zeros((l1d_total, 6), dtype = float)
  for i in range(0, l1d_total):
    total_access = 0
    for j in range(0, 6):
      total_access += l1d_array[i][j]
    for j in range(0, 6):
      result_l1d[i][j] = float(l1d_array[i][j]) / total_access

  result_l2 = np.zeros((l2_total, 6), dtype = float)
  for i in range(0, l2_total):
    total_access = 0
    for j in range(0, 6):
      total_access += l2_array[i][j]
    for j in range(0, 6):
      result_l2[i][j] = float(l2_array[i][j]) / total_access

  result_dram = np.zeros((dram_total, 2), dtype = float)
  for i in range(0, dram_total):
    total_access = 0
    for j in range(0, 2):
      total_access += dram_array[i][j]
    for j in range(0, 2):
      result_dram[i][j] = float(dram_array[i][j]) / total_access
  
  return result_l1d, result_l2, result_dram

def kernel_query():
  path = "../runtime_profiling_metrics/"
  if os.path.exists(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    return len(onlyfiles)
  else:
    print("Profiler directory is not allocated yet")
    return 0

def is_path_exists(path):
  if os.path.exists(path):
    return True
  else:
    return False
  
def last_cycle_check(kernel, last_point):
  fs = int(last_point / 1000000)
  path = ""
  if fs == 0:
    path = "../runtime_profiling_metrics/memory_accesses/kernel_" + str(kernel) + "/l1d/l1d_0.csv"
  if fs != 0:
    path = "../runtime_profiling_metrics/memory_accesses/kernel_" + str(kernel) + "/l1d/l1d_0_" + str(fs + 1) + ".csv"

  file = open(path, 'r')
  reader = csv.reader(file)
  last_cycle = 0
  for row in reader:
    if "cycle" not in row:
      last_cycle = int(row[0])
  return last_cycle

sampling_frequency = int(args[0])
arch_name = args[1]

l1d, l2, dram, prof_dump_per_cyc = collect_arch_info(arch_name)
prof_dump_per_cyc = 20
#print(l1d, l2, dram, prof_dump_per_cyc)
l1d_results = []
l2_results = []
dram_results = []
last_point = 5000

# update the case where sampling frequency is lower than kernel_launch_latency

counter = 0
is_current_kernel_done = False

cur_ker_last_cycle = 5
cycle_check_counter = 0 

kernel = 0
old_kernel = 0
last_cycle = 0

while True:
  if kernel == 0:
    cur_ker_last_cycle = last_cycle_check(kernel, last_point)
  else:
    cur_ker_last_cycle = last_cycle_check(kernel - 1, last_point)

  if cur_ker_last_cycle == last_cycle:
    kernel = kernel_query() 
    if old_kernel == kernel:
      cycle_check_counter += 1
      print(cycle_check_counter)
      time.sleep(1)
      if cycle_check_counter >= 30:
        print("CUDA Application is completely simulated")
        exit(1)                

    else:
      old_kernel = kernel
      cycle_check_counter = 0
      old_last_cycle = 0
      new_ker_path_ex = False
      last_point = 0

  else:
    cycle_check_counter = 0
    if kernel == 0:
      l1d_array, l2_array, dram_array, last_cycle = collect_profiling_metrics(l1d, l2, dram, kernel, sampling_frequency, last_point)
    else :
      l1d_array, l2_array, dram_array, last_cycle = collect_profiling_metrics(l1d, l2, dram, kernel - 1, sampling_frequency, last_point)
    l1d_results, l2_results, dram_results = calculate_plot_rates(l1d_array, l2_array, dram_array)
    
    print(last_cycle + prof_dump_per_cyc, sampling_frequency, prof_dump_per_cyc)
    if (last_cycle + prof_dump_per_cyc) % sampling_frequency == 0:
      image = plot(l1d_results, l2_results, dram_results, None, arch_name, kernel)

      if kernel == 0:
        file_name = "../runtime_profiling_metrics/memory_accesses/kernel_" + str(kernel) + "/"
      else:
        file_name = "../runtime_profiling_metrics/memory_accesses/kernel_" + str(kernel - 1) + "/"

      image.save(file_name + str(last_point) + "_" + str(last_cycle) + ".png")
      image.close()

      img_disp = cv2.imread(file_name + str(last_point) + "_" + str(last_cycle) + ".png", cv2.IMREAD_ANYCOLOR)  
      cv2.imshow(str(last_point) + "_" + str(last_cycle), img_disp)
      cv2.waitKey(10000)
      cv2.destroyWindow(str(last_point) + "_" + str(last_cycle))
      counter = 0

      last_point += sampling_frequency

    else:
      counter += 1
      time.sleep(1)
      print("Waiting to complete the prof interval and Elapsed time = " + str(counter) + 
            " seconds. Also, last_cycle = " + str(last_cycle))
    
    if counter > 100:
      break
#  print("Current, obtained last cycle = " + str(cur_ker_last_cycle))
print("Execution over")




