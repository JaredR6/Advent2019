import os, sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1, curdir + '\\..')

import adventutil, intcode

def solve(input):
  return 42

def execute(prefix='.'):
  adventutil.setPrefix(prefix)

  # Part 1

  tape = adventutil.readProblem()
  prep = intcode.PreparedIO([1])
  intcode.oneTimeRun(tape, prep=prep)
  print(f"Part 1: {prep.record}")

  # Part 2

  prep = intcode.PreparedIO([2])
  intcode.oneTimeRun(tape, prep=prep)
  print(f"Part 2: {prep.record}")


if __name__ == "__main__":
  execute()