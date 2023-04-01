import numpy as np

from PIL import Image
from PIL import ImageDraw
from GPU_QV100_VOLTA import plot_GV100
from GPU_GTX480_FERMI import plot_GTX480
from GPU_TITAN_KEPLER import plot_TITAN
from GPU_TITANX_PASCAL import plot_TITANX
from GPU_TITANV_VOLTA import plot_TITANV
from GPU_RTX2060_TURING import plot_RTX2060
from GPU_RTX2060S_TURING import plot_RTX2060S
from GPU_RTX3070_AMPERE import plot_RTX3070
from instructionMonitor import plotCTAonSM
from GPUMonitor import plotGPU

def gpu_plot_metrics(l1d, l2, dram, ipc_rate):

  l1d_tot = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
  counter = 0
  for i in range(0, len(l1d)):
    if (np.isnan(l1d[i][0])):
      continue
    else:
      counter += 1
      l1d_tot[0] += l1d[i][0] 
      l1d_tot[1] += l1d[i][1] 
      l1d_tot[2] += l1d[i][2] 
      l1d_tot[3] += l1d[i][3] 
      l1d_tot[4] += l1d[i][4] 
      l1d_tot[5] += l1d[i][5]
  
  if counter != 0:
    l1d_tot[0] = l1d_tot[0]/counter
    l1d_tot[1] = l1d_tot[1]/counter
    l1d_tot[2] = l1d_tot[2]/counter
    l1d_tot[3] = l1d_tot[3]/counter
    l1d_tot[4] = l1d_tot[4]/counter
    l1d_tot[5] = l1d_tot[5]/counter

  l1d_rgb = [0, 0, 0] # = np.zeros(((len(l1d), 3)), dtype = int)
  l1d_rgb[0] += int((l1d_tot[2] + l1d_tot[4]) * 255)
  l1d_rgb[1] += int((l1d_tot[0] + l1d_tot[1]) * 255)
  l1d_rgb[2] += int((l1d_tot[3]) * 255)

  if l1d_rgb[0] > 255:
    l1d_rgb[0] = 255
  if l1d_rgb[1] > 255:
    l1d_rgb[1] = 255
  if l1d_rgb[2] > 255:
    l1d_rgb[2] = 255

  l2_tot = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
  counter = 0
  for i in range(0, len(l2)):
    if (np.isnan(l2[i][0])):
      continue
    else:
      counter += 1
      l2_tot[0] += l2[i][0] 
      l2_tot[1] += l2[i][1] 
      l2_tot[2] += l2[i][2] 
      l2_tot[3] += l2[i][3] 
      l2_tot[4] += l2[i][4] 
      l2_tot[5] += l2[i][5]
  
  if counter != 0:
    l2_tot[0] = l2_tot[0]/counter
    l2_tot[1] = l2_tot[1]/counter
    l2_tot[2] = l2_tot[2]/counter
    l2_tot[3] = l2_tot[3]/counter
    l2_tot[4] = l2_tot[4]/counter
    l2_tot[5] = l2_tot[5]/counter    

  l2_rgb = [0, 0, 0] 
  l2_rgb[0] += int((l2_tot[2] + l2_tot[4]) * 255)
  l2_rgb[1] += int((l2_tot[0] + l2_tot[1]) * 255)
  l2_rgb[2] += int((l2_tot[3]) * 255)

  if l2_rgb[0] > 255:
    l2_rgb[0] = 255
  if l2_rgb[1] > 255:
    l2_rgb[1] = 255
  if l2_rgb[2] > 255:
    l2_rgb[2] = 255

  dram_tot = [0.0, 0.0]
  counter = 0
  for i in range(0, len(dram)):
    if (np.isnan(dram[i][0])):
      continue
    else:
      counter += 1
      dram_tot[0] += dram[i][0]
      dram_tot[1] += dram[i][1]
  
  if counter != 0:
    dram_tot[0] = dram_tot[0]/counter
    dram_tot[1] = dram_tot[1]/counter

  dram_rgb = [50, 50, 200]
  dram_rgb[1] = int(dram_tot[0] * 255) 
  dram_rgb[0] = int(dram_tot[1] * 255) 

  if dram_rgb[0] > 255:
    dram_rgb[0] = 255
  if dram_rgb[1] > 255:
    dram_rgb[1] = 255

  ipc_av = 0.0
  for i in range(0, len(ipc_rate)):
    if ipc_rate[i] != 0:
      ipc_av += ipc_rate[i]

  ipc_av
  return l1d_tot, l1d_rgb, l2_tot, l2_rgb, dram_tot, dram_rgb, ipc_av

def memory_plot_metrics(l1d, l2, dram):
  l1d_rgb = np.zeros(((len(l1d), 3)), dtype = int)
  for i in range(0, len(l1d)):
    if (np.isnan(l1d[i][0])):
      l1d_rgb[i][0] = 150
      l1d_rgb[i][1] = 150
      l1d_rgb[i][2] = 150
    else:
      l1d_rgb[i][0] = int((l1d[i][2] + l1d[i][4]) * 255)
      l1d_rgb[i][1] = int((l1d[i][0] + l1d[i][1]) * 255)
      l1d_rgb[i][2] = int((l1d[i][3]) * 255)

  l2_rgb = np.zeros(((len(l2), 3)), dtype = int)
  for i in range(0, len(l2)):
    if (np.isnan(l2[i][0])):
      l2_rgb[i][0] = 100
      l2_rgb[i][1] = 100
      l2_rgb[i][2] = 100
    else:
      l2_rgb[i][1] = int((l2[i][0] + l2[i][1]) * 255)
      l2_rgb[i][0] = int((l2[i][2] + l2[i][4]) * 255)
      l2_rgb[i][2] = int(((l2[i][3])) * 255)

  dram_rgb = np.zeros(((len(dram), 3)), dtype = int)
  for i in range(0, len(dram)):
    if (np.isnan(dram[i][0])):
      dram_rgb[i][0] = 200
      dram_rgb[i][1] = 200
      dram_rgb[i][2] = 200
    else:
      dram_rgb[i][1] = int(dram[i][0] * 255)
      dram_rgb[i][0] = int(dram[i][1] * 255)
      dram_rgb[i][2] = 255
  return l1d_rgb, l2_rgb, dram_rgb

# plot_type determines what you will plot during run-time. 
# core -> Just plot memory profiling metrics with L1D, L2 and DRAM
# memory -> Just plot the SM profiling to monitor instruction ex. with cta_iss and cta_comp
# gpu -> Both. 
#  plot(l1_met, l2_met, dram_met, core_plot_en, mem_hiear_plot_en, gpu_plot_en, arch_name, kernel, issued, completed, cluster_id, cta_id, ipc_rates,
#       core, mem_controller, gpu, start, finalize)

def plot(l1d, l2, dram, core, mem, gpu, arch, kernel, cta_iss, cta_comp, cluster_id, cta_id, ipc_rate,
         power_core, power_mem, power_total, int_start, int_finish, nof_active_SMs, grid_size, cta_size):

  if core == True:
    l1d_rgb = np.zeros(((len(l1d), 3)), dtype = int)
    for i in range(0, len(l1d)):
      if (np.isnan(l1d[i][0])):
        l1d_rgb[i][0] = 150
        l1d_rgb[i][1] = 150
        l1d_rgb[i][2] = 150
      else:
        l1d_rgb[i][0] = int((l1d[i][2] + l1d[i][4]) * 255)
        l1d_rgb[i][1] = int((l1d[i][0] + l1d[i][1]) * 255)
        l1d_rgb[i][2] = int((l1d[i][3]) * 255)

    image_core = Image.new(mode = "RGBA", size = (1920, 1080), color=(100, 100, 100))
    image_draw_core = ImageDraw.Draw(image_core)
    plotCTAonSM(image_draw_core, cta_id, cluster_id, kernel, cta_iss, cta_comp,
                l1d[cluster_id], l1d_rgb[cluster_id], ipc_rate[cluster_id],
                power_core, int_start, int_finish)
    image_core.save("plot_results/SMs/KID=" + str(kernel) + "_onSM=" + str(cluster_id) + "_withCTA=" + str(cta_id) + "_interval=" + str(int_start) + "_" + str(int_finish) + ".png")

  if mem == True:
    image_memory = Image.new(mode = "RGBA", size = (1920, 1080), color=(100, 100, 100))
    image_draw_memory = ImageDraw.Draw(image_memory)
    l1d_rgb, l2_rgb, dram_rgb = memory_plot_metrics(l1d, l2, dram)

    if arch == 'GTX480': #fermi
      image_draw_memory = plot_GTX480(image_draw_memory, l1d, l2, dram, kernel, int_start, int_finish, l1d_rgb, l2_rgb, dram_rgb, power_mem)
    elif arch == 'TITAN': #kepler
      image_draw_memory = plot_TITAN(image_draw_memory, l1d, l2, dram, kernel, int_start, int_finish, l1d_rgb, l2_rgb, dram_rgb, power_mem)
    elif arch == 'TITANX': #pascal
      image_draw_memory = plot_TITANX(image_draw_memory, l1d, l2, dram, kernel, int_start, int_finish, l1d_rgb, l2_rgb, dram_rgb, power_mem)
    elif arch == 'TITANV': #volta
      image_draw_memory = plot_TITANV(image_draw_memory, l1d, l2, dram, kernel, int_start, int_finish, l1d_rgb, l2_rgb, dram_rgb, power_mem)
    elif arch == 'GV100': #volta
      image_draw_memory = plot_GV100(image_draw_memory, l1d, l2, dram, kernel, int_start, int_finish, l1d_rgb, l2_rgb, dram_rgb, power_mem)
    elif arch == 'RTX2060': # turing
      image_draw_memory = plot_RTX2060(image_draw_memory, l1d, l2, dram, kernel, int_start, int_finish, l1d_rgb, l2_rgb, dram_rgb, power_mem)
    elif arch == 'RTX2060S': #turing
      image_draw_memory = plot_RTX2060S(image_draw_memory, l1d, l2, dram, kernel, int_start, int_finish, l1d_rgb, l2_rgb, dram_rgb, power_mem)
    elif arch == 'RTX3070': #ampere
      image_draw_memory = plot_RTX3070(image_draw_memory, l1d, l2, dram, kernel, int_start, int_finish, l1d_rgb, l2_rgb, dram_rgb, power_mem)

    image_memory.save("plot_results/memory/KID=" + str(kernel) + "_memStatsForInterval=" + str(int_start) + "_" + str(int_finish) + ".png")

  if gpu == True:

    image_gpu = Image.new(mode = "RGBA", size = (1280, 720), color=(100, 100, 100))
    image_draw_gpu = ImageDraw.Draw(image_gpu)
    l1d_av, l1d_rgb_av, l2_av, l2_rgb_av, dram_av, dram_rgb_av, ipc_av = \
        gpu_plot_metrics(l1d, l2, dram, ipc_rate)
    
    plotGPU(image_draw_gpu, kernel, ipc_av, l1d_av, l1d_rgb_av, l2_av, l2_rgb_av, dram_av, dram_rgb_av,
            power_total, int_start, int_finish, nof_active_SMs, grid_size, cta_size, len(l1d), len(l2), len(dram))
    image_gpu.save("plot_results/gpu_average/KID=" + str(kernel) + "_gpuAverageStatsForInterval=" + str(int_start) + "_" + str(int_finish) + ".png")

