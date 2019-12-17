import os, sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1, curdir + '/../intcode')
import intcode

def execute(prefix):

  with open(f"{prefix}//input.txt", "r") as f:
    inst = f.read().strip()
    tape = [int(s) for s in inst.split(',')]
    real = intcode.RealIO()
    auto = intcode.PreparedIO([1])
    intcode.compute(tape, io=auto)
    print(f"Diagnostic: {auto.record[:-2]}")
    print(f"Part 1: {auto.record[-1]}")
    auto = intcode.PreparedIO([5])
    intcode.compute(tape, io=auto)
    print(f"Part 2: {auto.record[-1]}")


if __name__ == "__main__":
  execute(".")