import os, sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1, curdir + '\\..')
import adventutil, intcode

def execute(prefix='.'):
  adventutil.setPrefix(prefix)

  # Test

  test_tape = adventutil.readTest()
  test_result = intcode.oneTimeRun(test_tape)
  print(f"Test: {test_result}")

  # Part 1

  tape = adventutil.readProblem()
  result = intcode.oneTimeRun(tape)
  print(f"Part 1: {result}")

  # Part 2

  target = adventutil.readProblem('2')[0]
  for i in range(100):
    for j in range(100):
      if intcode.oneTimeRun(tape, noun=i, verb=j) == target:
        print(f"Part 2: {i} {j}")
        return

if __name__ == "__main__":
  execute()