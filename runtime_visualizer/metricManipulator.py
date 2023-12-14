import sys
import numpy as np
import time
import cv2
import csv

from os import listdir
from os.path import isfile, join
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def calculatePlotRatesMetricsMem(l1d_array, l2_array, dram_array):
  l1d_total = len(l1d_array)
  l2_total = len(l2_array)
  dram_total = len(dram_array)

  result_l1d = np.zeros((l1d_total, 6), dtype = float)
  for i in range(0, l1d_total):
    total_access = 0
    total_misses = 0
    for j in range(0, 6): # hit, hit_res, miss, res_fail, sec_miss, mshr_hit.
      if j in [0,1,2,3,4]:
        total_access += l1d_array[i][j]
      if j in [2,4]:
        total_misses += l1d_array[i][j]
    for j in range(0, 6):
      if j != 5:
        result_l1d[i][j] = float(l1d_array[i][j]) / total_access
      else:
        result_l1d[i][j] = float(l1d_array[i][j]) / total_misses

  result_l2 = np.zeros((l2_total, 6), dtype = float)
  for i in range(0, l2_total):
    total_access = 0
    total_misses = 0
    for j in range(0, 6): # hit, hit_res, miss, res_fail, sec_miss, mshr_hit.
      if j in [0,1,2,3,4]:
        total_access += l2_array[i][j]
      if j in [2,4]:
        total_misses += l2_array[i][j]
    for j in range(0, 6):
      if j != 5:
        result_l2[i][j] = float(l2_array[i][j]) / total_access
      else:
        result_l2[i][j] = float(l2_array[i][j]) / total_misses

  result_dram = np.zeros((dram_total, 2), dtype = float)
  for i in range(0, dram_total):
    total_access = 0
    for j in range(0, 2):
      total_access += dram_array[i][j]
    for j in range(0, 2):
      result_dram[i][j] = float(dram_array[i][j]) / total_access
  return result_l1d, result_l2, result_dram

def calculatePlotRatesMetricsPower(metrics, core, mem, gpu):
  mem_controller_items = ['mc_fee', 'mc_phy', 'mc_te', 'mc_total']
  gpu_component = ['proc_total', 'proc_cores', 'proc_l2', 'proc_mcs', 'proc_nocs']
  core_items = ['eu_core', 'inst_fu_core', 'idle_core', 'ldst_core', 'total_core']

  last_res = {}
  if core == True:
    for i in core_items:
      data = {}
      if i == 'eu_core':
        data = {"PeakDynamic(W)": 0.0,	"PeakDynamicEnergy(W)": 0.0, "SubthresholdLeakage(W)": 0.0, "GateLeakage(W)": 0.0, "RunTimeDynamic(W)": 0.0}
        for j in range(0, len(metrics[i]["PeakDynamic(W)"])):
          data["PeakDynamic(W)"] += metrics[i]["PeakDynamic(W)"][j]
          data["PeakDynamicEnergy(W)"] +=  metrics[i]["PeakDynamicEnergy(W)"][j]
          data["SubthresholdLeakage(W)"] += metrics[i]["SubthresholdLeakage(W)"][j]
          data["GateLeakage(W)"] += metrics[i]["GateLeakage(W)"][j]
          data["RunTimeDynamic(W)"] += metrics[i]["RunTimeDynamic(W)"][j]

      elif i == 'inst_fu_core' or i == 'ldst_core' or i == 'total_core':
        data = {"PeakDynamic(W)": 0.0,	"SubthresholdLeakage(W)": 0.0, "GateLeakage(W)": 0.0,	"RunTimeDynamic(W)": 0.0}
        for j in range(0, len(metrics[i]["PeakDynamic(W)"])):
          data["PeakDynamic(W)"] += metrics[i]["PeakDynamic(W)"][j]
          data["SubthresholdLeakage(W)"] += metrics[i]["SubthresholdLeakage(W)"][j]
          data["GateLeakage(W)"] += metrics[i]["GateLeakage(W)"][j]
          data["RunTimeDynamic(W)"] += metrics[i]["RunTimeDynamic(W)"][j]

      elif i == 'idle_core':
        data = {"RunTimeDynamic(W)": 0.0}
        for j in range(0, len(metrics[i]["RunTimeDynamic(W)"])):
          data["RunTimeDynamic(W)"] += metrics[i]["RunTimeDynamic(W)"][j]
      last_res[i] = data

#  mem_controller_items = ['mc_fee', 'mc_phy', 'mc_te', 'mc_total']
  elif mem == True:
    for i in mem_controller_items:
      data = {"PeakDynamic(W)": 0.0, "SubthresholdLeakage(W)": 0.0, "GateLeakage(W)": 0.0,	"RunTimeDynamic(W)": 0.0}
      for j in range(0, len(metrics[i]["Cycle"])):
        data["PeakDynamic(W)"] += metrics[i]["PeakDynamic(W)"][j]
        data["SubthresholdLeakage(W)"] += metrics[i]["SubthresholdLeakage(W)"][j]
        data["GateLeakage(W)"] += metrics[i]["GateLeakage(W)"][j]
        data["RunTimeDynamic(W)"] += metrics[i]["RunTimeDynamic(W)"][j]
      last_res[i] = data

  elif gpu == True:
    for i in gpu_component:
      data = {}
      if i == 'proc_total':
        data = {"PeakPower(W)": 0.0, "TotalLeakage(W)": 0.0, "PeakDynamic(W)": 0.0,	
                "SubthresholdLeakage(W)": 0.0, "GateLeakage(W)": 0.0,	"RunTimeDynamic(W)": 0.0}
        for j in range(0, len(metrics[i]["Cycle"])):
          data["PeakPower(W)"] += metrics[i]["PeakPower(W)"][j]
          data["TotalLeakage(W)"] += metrics[i]["TotalLeakage(W)"][j]
          data["PeakDynamic(W)"] += metrics[i]["PeakDynamic(W)"][j]
          data["SubthresholdLeakage(W)"] += metrics[i]["SubthresholdLeakage(W)"][j]
          data["GateLeakage(W)"] += metrics[i]["GateLeakage(W)"][j]
          data["RunTimeDynamic(W)"] += metrics[i]["RunTimeDynamic(W)"][j]
      elif i == 'proc_cores' or i == 'proc_nocs' or i == 'proc_l2' or i == 'proc_mcs':
        data = {"PeakDynamic(W)": 0.0, "SubthresholdLeakage(W)": 0.0, "GateLeakage(W)": 0.0, "RunTimeDynamic(W)": 0.0}
        for j in range(0, len(metrics[i]["Cycle"])):
          data["PeakDynamic(W)"] += metrics[i]["PeakDynamic(W)"][j]
          data["SubthresholdLeakage(W)"] += metrics[i]["SubthresholdLeakage(W)"][j]
          data["GateLeakage(W)"] += metrics[i]["GateLeakage(W)"][j]
          data["RunTimeDynamic(W)"] += metrics[i]["RunTimeDynamic(W)"][j]
      last_res[i] = data
  
  return last_res


def lastCycleCheck(kernel, last_point):
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
