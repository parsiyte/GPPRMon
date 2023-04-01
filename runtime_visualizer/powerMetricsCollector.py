import csv
### Power consumption metric collection files ###
'''
1)  Execution units of core.
    Cycle	  Area(mm^2)	PeakDynamic(W)	PeakDynamicEnergy(W)	clockRate(MHz)	SubthresholdLeakage(W)	GateLeakage(W)	RunTimeDynamic(W)
    20	    13.0892	    0.726309	      0	                    700000000	      0.432316	              0.001509	      0
2)  Core at idle times.
    Cycle	  RunTimeDynamic(W)
    20	    22.623333
3)  Inst functional unit.
    Cycle	  Area(mm^2)	PeakDynamic(W)	SubthresholdLeakage(W)	GateLeakage(W)	RunTimeDynamic(W)
    20	    1.3415	    0.039994	      0.023482	              0.00297	        0
4)  Load store units of the core.
    Cycle	  Area(mm^2)	PeakDynamic(W)	SubthresholdLeakage(W)	GateLeakage(W)	RunTimeDynamic(W)
    20	    8.644	      0.261844	      0.058609	              0.079322	      0
5)  Total core
    Cycle	  Area(mm^2)	PeakDynamic(W)	SubthresholdLeakage(W)	GateLeakage(W)	RunTimeDynamic(W)
    20	    23.8212	    1.028147	      0.538949	              0.08672	        22.623333         '''

baseline_path = "../runtime_profiling_metrics/energy_consumption/kernel_"


#1)  Execution units of core.
#    20	    13.0892	    0.726309	      0	                    700000000	      0.432316	              0.001509	      0

## I must convert E notation (scientific notation) to the 
## decimal notation. For some of the power metrics, results are represented
## in scientific format. 

def collectPowerMetricsCore(start_c, finish_c, kid, type):

  seq = int(start_c / 1000000)
  csv_filename = ""
  metrics = {}

  core_items = ['eu_core', 'inst_fu_core', 'idle_core', 'ldst_core', 'total_core']

  if type == 'eu_core':
    csv_filename = baseline_path + str(kid) + "/f_core_eu_0"
    metrics = {"Cycle": [], "Area(mm^2)": [],	"PeakDynamic(W)": [],	"PeakDynamicEnergy(W)": [],
               "SubthresholdLeakage(W)": [], "GateLeakage(W)": [],	"RunTimeDynamic(W)": []}

  elif type == 'inst_fu_core':
    csv_filename = baseline_path + str(kid) + "/f_core_inst_fu_0" 
    metrics = {"Cycle": [], "Area(mm^2)": [],	"PeakDynamic(W)": [],	
               "SubthresholdLeakage(W)": [], "GateLeakage(W)": [],	"RunTimeDynamic(W)": []}

  elif type == 'idle_core':
    csv_filename = baseline_path + str(kid) + "/f_core_idle_0" 
    metrics = {"Cycle": [], "RunTimeDynamic(W)": []}

  elif type == 'ldst_core':
    csv_filename = baseline_path + str(kid) + "/f_core_ldst_u_0" 
    metrics = {"Cycle": [], "Area(mm^2)": [],	"PeakDynamic(W)": [],	
               "SubthresholdLeakage(W)": [], "GateLeakage(W)": [],	"RunTimeDynamic(W)": []}

  elif type == 'total_core':
    csv_filename = baseline_path + str(kid) + "/f_p_total_cores"
    metrics = {"Cycle": [], "Area(mm^2)": [],	"PeakDynamic(W)": [],	
               "SubthresholdLeakage(W)": [], "GateLeakage(W)": [],	"RunTimeDynamic(W)": []}

  if seq >= 1:
    csv_filename += "_" + str(seq + 1) + ".csv"

  else:
    csv_filename += ".csv"

  file = open(csv_filename, 'r')
  reader = csv.reader(file) 
  for row in reader:
    if ("Cycle" not in row) and (start_c <= int(row[0]) and finish_c > int(row[0])):      
      metrics["Cycle"].append(int(row[0]))
      if type == 'eu_core':
        metrics["Area(mm^2)"].append(float(row[1]))
        metrics["PeakDynamic(W)"].append(float(row[2]))
        metrics["PeakDynamicEnergy(W)"].append(float(row[3]))
        metrics["SubthresholdLeakage(W)"].append(float(row[5]))
        metrics["GateLeakage(W)"].append(float(row[6]))
        metrics["RunTimeDynamic(W)"].append(float(row[7]))

      elif type == 'inst_fu_core':
        metrics["Area(mm^2)"].append(float(row[1]))
        metrics["PeakDynamic(W)"].append(float(row[2]))
        metrics["SubthresholdLeakage(W)"].append(float(row[3]))
        metrics["GateLeakage(W)"].append(float(row[4]))
        metrics["RunTimeDynamic(W)"].append(float(row[5]))

      elif type == 'idle_core':
        metrics["RunTimeDynamic(W)"].append(float(row[1]))

      elif type == 'ldst_core':
        metrics["Area(mm^2)"].append(float(row[1]))
        metrics["PeakDynamic(W)"].append(float(row[2]))
        metrics["SubthresholdLeakage(W)"].append(float(row[3]))
        metrics["GateLeakage(W)"].append(float(row[4]))
        metrics["RunTimeDynamic(W)"].append(float(row[5]))

      elif type == 'total_core':
        metrics["Area(mm^2)"].append(float(row[1]))
        metrics["PeakDynamic(W)"].append(float(row[2]))
        metrics["SubthresholdLeakage(W)"].append(float(row[3]))
        metrics["GateLeakage(W)"].append(float(row[4]))
        metrics["RunTimeDynamic(W)"].append(float(row[5]))
    if ("Cycle" not in row) and int(row[0]) >= finish_c:
      break      

  file.close()
  return metrics

'''
1)  Front end engine of the memory controller
    Cycle	  Area(mm^2)	PeakDynamic(W)	SubthresholdLeakage(W)	GateLeakage(W)	RunTimeDynamic(W)
    20	    0.2191	    0.065854	      0.000377	              3.4E-05	        0.039512
2)  PHY of the memory controller
    Cycle	  Area(mm^2)	PeakDynamic(W)	SubthresholdLeakage(W)	GateLeakage(W)	RunTimeDynamic(W)
    20	    1.6202	    0.544831	      0.005673	              0.000697	      0.326899
3)  Transaction engine of the memory controller
    Cycle	  Area(mm^2)	PeakDynamic(W)	SubthresholdLeakage(W)	GateLeakage(W)	RunTimeDynamic(W)
    20	    0.7779	    0.306348	      0.002724	              0.000334	      0.183809
4)  Total memory controller
    Cycle 	Area(mm^2)	PeakDynamic(W)	SubthresholdLeakage(W)	GateLeakage(W)	RunTimeDynamic(W)
    20  	  15.7031	    5.502199	      0.052647	              0.006391	      0.55022
'''
def collectPowerMetricsMemoryController(start_c, finish_c, kid, type):

  seq = int(start_c / 1000000)
  csv_filename = ""
  metrics = {"Cycle": [], "Area(mm^2)": [],	"PeakDynamic(W)": [],
             "SubthresholdLeakage(W)": [], "GateLeakage(W)": [],	"RunTimeDynamic(W)": []}
  if type == 'mc_fee':
    csv_filename = baseline_path + str(kid) + "/f_mc_front_end_engine"
  elif type == 'mc_phy':
    csv_filename = baseline_path + str(kid) + "/f_mc_phy" 
  elif type == 'mc_te':
    csv_filename = baseline_path + str(kid) + "/f_mc_transaction_engine" 
  elif type == 'mc_total':
    csv_filename = baseline_path + str(kid) + "/f_p_total_mcs" 

  if seq >= 1:
    csv_filename += "_" + str(seq + 1) + ".csv"

  else:
    csv_filename += ".csv"

  file = open(csv_filename, 'r')
  reader = csv.reader(file) 
  for row in reader:
    if ("Cycle" not in row) and (start_c <= int(row[0]) and finish_c > int(row[0])):      
      metrics["Cycle"].append(int(row[0]))
      metrics["Area(mm^2)"].append(float(row[1]))
      metrics["PeakDynamic(W)"].append(float(row[2]))
      metrics["SubthresholdLeakage(W)"].append(float(row[3]))
      metrics["GateLeakage(W)"].append(float(row[4]))
      metrics["RunTimeDynamic(W)"].append(float(row[5]))
    if ("Cycle" not in row) and int(row[0]) >= finish_c:
      break      
  file.close()
  return metrics

'''
1)  Total cores
    Cycle	  Area(mm^2)	PeakDynamic(W)	SubthresholdLeakage(W)	GateLeakage(W)	RunTimeDynamic(W)
    20	    23.8212	    1.028147	      0.538949	              0.08672	        22.623333
2)  Total memory controller
    Cycle	  Area(mm^2)	PeakDynamic(W)	SubthresholdLeakage(W)	GateLeakage(W)	RunTimeDynamic(W)
    20	    15.7031	    5.502199	      0.052647	              0.006391    	  0.55022
3)  GPU
    Cycle	  Area(mm^2)	PeakPower(W)	  TotalLeakage(W)	  PeakDynamic(W)	SubthresholdLeakage(W)	GateLeakage(W)	RunTimeDynamic(W)
    20	    40.6137	    7.425191	      0.693847	        6.731343	      0.599781	              0.094066	      23.173553

4)  Total L2
    Cycle	  Area(mm^2)	PeakDynamic(W)	SubthresholdLeakage(W)	GateLeakage(W)	RunTimeDynamic(W)
    20	    1.057	      0.187474	      0.005507	              0.000525	      0

5)  Total NoCs
    Cycle	  Area(mm^2)	PeakDynamic(W)	SubthresholdLeakage(W)	GateLeakage(W)	RunTimeDynamic(W)
    20	    0.0324	    0.013523	      0.002678	              0.000431	      0
'''

def collectPowerMetricsGPUComponents(start_c, finish_c, kid, type):
  seq = int(start_c / 1000000)
  csv_filename = ""
  metrics = {}
  if type == 'proc_total':
    csv_filename = baseline_path + str(kid) + "/f_processor"
    metrics = {"Cycle": [], "Area(mm^2)": [], "PeakPower(W)": [], "TotalLeakage(W)": [],	"PeakDynamic(W)": [],	
               "SubthresholdLeakage(W)": [], "GateLeakage(W)": [],	"RunTimeDynamic(W)": []}
  elif type == 'proc_cores':
    csv_filename = baseline_path + str(kid) + "/f_p_total_cores" 
    metrics = {"Cycle": [], "Area(mm^2)": [],	"PeakDynamic(W)": [],
               "SubthresholdLeakage(W)": [], "GateLeakage(W)": [],	"RunTimeDynamic(W)": []}
  elif type == 'proc_l2':
    csv_filename = baseline_path + str(kid) + "/f_p_total_l2" 
    metrics = {"Cycle": [], "Area(mm^2)": [],	"PeakDynamic(W)": [],
               "SubthresholdLeakage(W)": [], "GateLeakage(W)": [],	"RunTimeDynamic(W)": []}
  elif type == 'proc_mcs':
    csv_filename = baseline_path + str(kid) + "/f_p_total_mcs" 
    metrics = {"Cycle": [], "Area(mm^2)": [],	"PeakDynamic(W)": [],
               "SubthresholdLeakage(W)": [], "GateLeakage(W)": [],	"RunTimeDynamic(W)": []}
  elif type == 'proc_nocs':
    csv_filename = baseline_path + str(kid) + "/f_p_total_nocs" 
    metrics = {"Cycle": [], "Area(mm^2)": [],	"PeakDynamic(W)": [],
               "SubthresholdLeakage(W)": [], "GateLeakage(W)": [],	"RunTimeDynamic(W)": []}

  if seq >= 1:
    csv_filename += "_" + str(seq + 1) + ".csv"

  else:
    csv_filename += ".csv"
  
  file = open(csv_filename, 'r')
  reader = csv.reader(file) 
  for row in reader:
    if ("Cycle" not in row) and (start_c <= int(row[0]) and finish_c > int(row[0])):
      metrics["Cycle"].append(int(row[0]))
      if type == 'proc_total': 
        metrics["Area(mm^2)"].append(float(row[1]))
        metrics["PeakPower(W)"].append(float(row[2]))
        metrics["TotalLeakage(W)"].append(float(row[3]))
        metrics["PeakDynamic(W)"].append(float(row[4]))
        metrics["SubthresholdLeakage(W)"].append(float(row[5]))
        metrics["GateLeakage(W)"].append(float(row[6]))
        metrics["RunTimeDynamic(W)"].append(float(row[7]))
      elif type == 'proc_cores' or type == 'proc_l2' or type == 'proc_mcs' or type == 'proc_nocs':
        metrics["Area(mm^2)"].append(float(row[1]))
        metrics["PeakDynamic(W)"].append(float(row[2]))
        metrics["SubthresholdLeakage(W)"].append(float(row[3]))
        metrics["GateLeakage(W)"].append(float(row[4]))
        metrics["RunTimeDynamic(W)"].append(float(row[5]))
    if ("Cycle" not in row) and int(row[0]) >= finish_c:
      break      
  file.close()
  return metrics

