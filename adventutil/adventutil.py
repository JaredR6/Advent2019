def readProblem(file, delim=','):
  with open(file, "r") as f:
    inst = f.read().strip()
  tape = [int(s) for s in inst.split(delim)]
  return tape

def readProblemStr(file):
  with open(file, "r") as f:
    inst = f.read().strip()
  return inst
