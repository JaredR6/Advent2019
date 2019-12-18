advent_prefix = '.'

def setPrefix(s):
  global advent_prefix
  advent_prefix = s

def readProblem(suffix='', as_int=True, delim=','):
  global advent_prefix
  return readFile(f"{advent_prefix}\\input{suffix}.txt", as_int, delim)

def readTest(suffix='', as_int=True, delim=','):
  global advent_prefix
  return readFile(f"{advent_prefix}\\test{suffix}.txt", as_int, delim)

def readFile(file, as_int=True, delim=','):
  inst = None
  with open(file, "r") as f:
    inst = f.read().strip()
  if delim == '':
    inst = list(inst)
  else:
    if as_int:
      inst = [int(s) for s in inst.split(delim)]
    else:
      inst = inst.split(delim)
  return inst
