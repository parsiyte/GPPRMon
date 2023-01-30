
def collect_arch_info(arch):

  profiler_dump_freq = 0
  path = ""
  if arch == "GTX480":
    path = "SM2_GTX480"

  elif arch == "TITAN":
    path = "SM3_KEPLER_TITAN"

  elif arch == "TITANX":
    path = "SM6_TITANX"

  elif arch == "RTX2060":
    path = "SM75_RTX2060"

  elif arch == "RTX2060S":
    path = "SM75_RTX2060_S"

  elif arch == "TITANV":
    path = "SM7_TITANV"

  elif arch == "QV100":
    path = "SM7_QV100"
              
  elif arch == "RTX3070":
    path = "SM86_RTX3070"

  file = open("../configs/tested-cfgs/"+ path + "/gpgpusim.config", 'r')
  lines = len(file.readlines())
  file.close()

  num_of_cluster = 0
  num_of_core_per_cluster = 0
  num_of_mem = 0
  sub_part_per_channel = 0

  file = open("../configs/tested-cfgs/"+ path + "/gpgpusim.config", 'r')
  for i in range(0, lines):
    line = file.readline()

    if "gpgpu_n_clusters" in line:
      num_of_cluster = int(line[len("-gpgpu_n_clusters"):])

    if "gpgpu_n_cores_per_cluster" in line:
      num_of_core_per_cluster = int(line[len("-gpgpu_n_cores_per_cluster"):])

    if "gpgpu_n_mem" in line and "gpgpu_n_mem_per_ctrlr" not in line:
      num_of_mem = int(line[len("-gpgpu_n_mem"):])

    if "gpgpu_n_sub_partition_per_mchannel" in line:
      sub_part_per_channel = int(line[len("-gpgpu_n_sub_partition_per_mchannel"):])

    if "mem_runtime_stat" in line:
      profiler_dump_freq = int(line[len("-mem_runtime_stat"):])
      break

  file.close()

  l1d = num_of_cluster * num_of_core_per_cluster
  l2 = num_of_mem * sub_part_per_channel
  dram = num_of_mem
  return l1d, l2, dram, profiler_dump_freq


  