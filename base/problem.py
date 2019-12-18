import os, sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1, curdir + '\\..')
import adventutil

def solve(input):
  return 42

def solve2(input):
  return 42

# Read tips:
# csv of numbers: readProblem()
# csv of words: readProblem(as_int=False)
# \n-sep words: readProblem(as_int=False, delim='\n')
# (Further processing may be required)

def execute(prefix='.'):
  adventutil.setPrefix(prefix)

  # Test

  test_inst = adventutil.readTest()
  test_result = solve(test_inst)
  print(f"Test: {test_result}")

  # Part 1

  inst = adventutil.readProblem()
  result = solve(inst)
  print(f"Part 1: {result}")

  # Part 2

  # inst = adventutil.readProblem('2')
  result = solve2(inst)
  print(f"Part 2: {result}")


if __name__ == "__main__":
  execute()