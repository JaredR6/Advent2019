import os, sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1, curdir + '\\..')
import adventutil

def has_double(s):
  for i in range(len(s)-1):
    if s[i] == s[i+1]:
      return True
  return False

def has_strict_double(s):
  dub, strict = False, False
  for i in range(len(s)-1):
    if s[i] == s[i+1]:
      strict = not dub
      dub = True
    else:
      if strict:
        return True
      dub = False
  return strict


def increasing(s):
  for i in range(len(s)-1):
    if int(s[i]) > int(s[i+1]):
      return False
  return True

def solve(input):
  counta, countb = 0, 0
  for i in range(int(input[0]), int(input[1])+1):
    s = str(i)
    if has_double(s) and increasing(s):
      counta += 1
    if has_strict_double(s) and increasing(s):
      countb += 1
  return counta, countb

def execute(prefix='.'):
  adventutil.setPrefix(prefix)

  # Part 1

  inst = adventutil.readProblem(delim='-')
  result = solve(inst)
  print(f"Result: {result}")


if __name__ == "__main__":
  execute()