import os, sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1, curdir + '/../intcode')
import intcode

def execute(prefix):
  tape = intcode.arrayFromFile(f"{prefix}//input.txt")
  # real = intcode.RealIO()
  prep = intcode.PreparedIO([1])
  intcode.oneTimeRun(tape, prep=prep)
  print(f"Diagnostic: {prep.record[:-2]}")
  print(f"Part 1: {prep.record[-1]}")
  prep = intcode.PreparedIO([5])
  intcode.oneTimeRun(tape, prep=prep)
  print(f"Part 2: {prep.record[-1]}")


if __name__ == "__main__":
  execute(".")