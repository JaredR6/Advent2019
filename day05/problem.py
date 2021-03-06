import os, sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1, curdir + '\\..')
import adventutil, intcode

def execute(prefix='.'):
  adventutil.setPrefix(prefix)

  # Part 1

  tape = adventutil.readProblem()
  # real = intcode.RealIO()
  prep = intcode.PreparedIO([1])
  intcode.oneTimeRun(tape, prep=prep)
  print(f"Diagnostic: {[prep.output() for i in range(9)]}")
  print(f"Part 1: {prep.output()}")

  # Part 2

  prep = intcode.PreparedIO([5])
  intcode.oneTimeRun(tape, prep=prep)
  print(f"Part 2: {prep.output()}")


if __name__ == "__main__":
  execute()