import csv
import numpy as np


baseline_path = "../runtime_profiling_metrics/memory_accesses/"

                  # nofL1D, nofL2, nofDRAM, kernel, int_start, int_finish
def collectProfilingMetricsMem(l1d, l2, dram, kernel, start, finish, 
                               l1d_enable, l2_enable, dram_enable):

  l1d_array = []
  l2_array = []
  dram_array = [] 

  if l1d_enable:
    l1d_path = baseline_path + "kernel_" + str(kernel) + "/l1d"
    l1d_array = np.zeros((l1d,6), dtype = int)
    for i in range(0, l1d):
      if start < 1000000:
        path = l1d_path + "/l1d_" + str(i) + ".csv" 
      else:
        rem = int(start / 1000000) 
        path = l1d_path + "/l1d_" + str(i) + "_" + str(rem + 1) + ".csv"

      file = open(path, 'r')
      reader = csv.reader(file)
      for row in reader:
        if "cycle" not in row and (int(row[0]) < finish) and (int(row[0]) >= start):
          l1d_array[i][0] += int(row[1])    # hit accesses
          l1d_array[i][1] += int(row[2])    # hit reserved accesses
          l1d_array[i][2] += int(row[3])    # miss accesses
          l1d_array[i][3] += int(row[4])    # reservation failures
          l1d_array[i][4] += int(row[5])    # sector misses 
          l1d_array[i][5] += int(row[6])    # mshr hits
        if "cycle" not in row and int(row[0]) >= finish:
          break
      file.close()
    
  if l2_enable:
    l2_path = baseline_path + "kernel_" + str(kernel) +  "/l2"
    l2_array = np.zeros((l2,6), dtype = int)
    for i in range(0, l2):
      if start < 1000000:
        path = l2_path + "/l2_" + str(i) + ".csv" 
      else:
        rem = int(start / 1000000) 
        path = l2_path + "/l2_" + str(i) + "_" + str(rem + 1) + ".csv"

      file = open(path, 'r')
      reader = csv.reader(file)
      c = 0
      for row in reader:
        if "cycle" not in row and (int(row[0]) < finish) and (int(row[0]) >= start):
          l2_array[i][0] += int(row[1])     # hit accesses
          l2_array[i][1] += int(row[2])     # hit reserved accesses
          l2_array[i][2] += int(row[3])     # miss accesses
          l2_array[i][3] += int(row[4])     # reservation failures
          l2_array[i][4] += int(row[5])     # sector misses
          l2_array[i][5] += int(row[6])     # mshr hits
        if "cycle" not in row and int(row[0]) >= finish:
          break
      file.close()

  if dram_enable:
    dram_path = baseline_path + "kernel_" + str(kernel) + "/dram"
    dram_array = np.zeros((dram, 2), dtype = int)
    for i in range(0, dram):
      if start < 1000000:
        path = dram_path + "/dram_" + str(i) + ".csv" 
      else:
        rem = int(start / 1000000) 
        path = dram_path + "/dram_" + str(i) + "_" + str(rem + 1) + ".csv"

      file = open(path, 'r')
      reader = csv.reader(file)
      for row in reader:
        if "cycle" not in row and (int(row[0]) < finish) and (int(row[0]) >= start):
          dram_array[i][0] += int(row[1])
          dram_array[i][1] += int(row[2])
        if "cycle" not in row and int(row[0]) >= finish:
          break
      file.close()

  return l1d_array, l2_array, dram_array


def ctaInstructionMonitoringAtIssue(csv_filename, cta_id, start_interval, finish_interval):
  instructions = []
  file = open(csv_filename, 'r')
  reader = csv.reader(file) 
  for row in reader:
    element = {}
#    print(row)
    if ("cycle" not in row) and (int(row[2]) == cta_id) and \
       (start_interval <= int(row[0]) and finish_interval > int(row[0])):
      instruction = row[1]

      counter = 0
      pc = ''
      for i in range(6, len(instruction)):
        if instruction[i] != ' ':
          pc += instruction[i]
        else:
          counter = i
          break
      for i in range(counter, len(instruction)):
        if instruction[i] == ')':
          counter = i + 2
          break
      instruction_opcode = '' 
      for i in range(counter, len(instruction)):
        if instruction[i] != ' ':
          instruction_opcode += instruction[i]
        else:
          counter = i + 1
          break
      instruction_operand = instruction[counter:]

      instructionExist = False
      for i in range(0, len(instructions)):
        if instruction_opcode == instructions[i]['opcode'] and \
           int(pc, 16) == instructions[i]['pc'] and \
           instruction_operand == instructions[i]['operand']: 

          instructionExist = True
          instructions[i]['cycle'].append(int(row[0]))
          instructions[i]['warps'].append(int(row[4]))

      if instructionExist == False:
        element['opcode'] = instruction_opcode
        element['operand'] = instruction_operand
        element['pc'] = int(pc, 16)
        warps = [int(row[4])]
        element['warps'] = warps
        cycle = [int(row[0])]
        element['cycle'] = cycle
        instructions.append(element)
    if ("cycle" not in row) and int(row[0]) >= finish_interval:
      break

  file.close()
  return instructions

# instruction[0][pc]
# instruction[0][opcode]
# instruction[0][operand]
# instruction[0][warps][0][0] ->warp_id
# instruction[0][warps][1][1] ->cycle

#cycle	pc	cta_id	cluster_id	warp_id	tid
#5005	  0	  0	      0	          1   	  ffffffff
#5006	  0	  0	      0	          2   	  ffffffff
# 0 -> cycle,     # 1 -> instruction # 2 -> cta_id
# 3 -> cluster_id # 4 -> warp_id     # 5 -> tid

def ctaInstructionMonitoringAtCompletion(csv_filename, cta_id, start_interval, finish_interval):
  instructions = []
  file = open(csv_filename, 'r')
  reader = csv.reader(file) 
  for row in reader:
    element = {}

    if ("cycle" not in row) and (int(row[2]) == cta_id) and \
       (start_interval <= int(row[0]) and finish_interval > int(row[0])):

      instructionExist = False
      idx = 0
      for i in range(0, len(instructions)):
        if instructions[i]['pc'] == int(row[1], 16):
          instructionExist = True
          idx = i
          break

      if instructionExist == True:
        instructions[idx]['warps'].append(int(row[4]))
        instructions[idx]['cycle'].append(int(row[0]))

      else:
        element['pc'] = int(row[1], 16)
        warps = [int(row[4])]
        element['warps'] = warps
        cycle = [int(row[0])]
        element['cycle'] = cycle
        instructions.append(element)
    if ("cycle" not in row) and int(row[0]) >= finish_interval:
      break

  file.close()
  return instructions

def IPC(nof_sm, start_interval, finish_interval, kernel):

  path = "../runtime_profiling_metrics/memory_accesses/kernel_" + str(kernel) + \
                  "/ipc/"

  if start_interval < 1000000:
    path = path + "ipc.csv" 

  else:
    rem = int(start_interval / 1000000) 
    path = path + "ipc_" + str(rem + 1) + ".csv" 

  ipc_rates = np.zeros(nof_sm, dtype = float)
  file = open(path, 'r')
  reader = csv.reader(file) 

  counter = 0
  for row in reader:
    if "cycle" not in row and int(row[0]) >= start_interval and int(row[0]) < finish_interval:
      counter += 1
      for j in range(0, 7):
        if row[j+1] == '':
          print(row)        
        ipc_rates[j] += float(row[j+1])
    
    if "cycle" not in row and finish_interval < int(row[0]):
      break
  file.close()
  
  for j in range(0, nof_sm):
    ipc_rates[j] = ipc_rates[j]/counter

  return ipc_rates