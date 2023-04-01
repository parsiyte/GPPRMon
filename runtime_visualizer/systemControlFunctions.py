import os
from os import listdir
from os.path import isfile, join

def newKernelQuery():
  path = "../runtime_profiling_metrics/"
  if os.path.exists(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    return len(onlyfiles)
  else:
    print("Profiler directory is not allocated yet")
    return 0

def isPathExists(path):
  if os.path.exists(path):
    return True
  else:
    return False
  