import os, sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1, curdir + '/../intcode')
import intcode
from itertools import permutations


def ampChainMax(tape, input, inactive):
  if len(inactive) == 0:
    return input
  else:
    hi = 0
    current = inactive.copy()
    for a in current:
      inactive.remove(a)
      prep = intcode.PreparedIO([a, input])
      intcode.oneTimeRun(tape, prep=prep)
      hi = max(hi, ampChainMax(tape, prep.record[0], inactive))
      inactive.add(a)
    return hi

def solve(input):
  inactive = set([0, 1, 2, 3, 4])
  return ampChainMax(input, 0, inactive)

def solve2(input):
  hi = 0
  for perm in permutations(range(5, 10)):
    data = 0
    interfaces = [intcode.PreparedIO([i]) for i in perm]
    insts = [intcode.Instance(input, prep=intcode.PreparedIO([i])) for i in perm]
    while not insts[0].tape.terminated:
      for inst in insts:
        inst.io.input(data)
        inst.sim()
        data = inst.io.output()
    hi = max(hi, data)
  return hi

def execute(prefix):

  # Part 1

  tape = intcode.arrayFromFile(f"{prefix}//input.txt")
  result = solve(tape)
  print(f"Part 1: {result}")

  # Test

  test_tape = intcode.arrayFromFile(f"{prefix}//test.txt")
  result = solve2(test_tape)
  print(f"Test: {result}")

  # Part 2

  result = solve2(tape)
  print(f"Part 2: {result}")


if __name__ == "__main__":
  execute(".")