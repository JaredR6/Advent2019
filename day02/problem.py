import os, sys

curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1, curdir + '/../intcode')
import intcode

def execute(prefix):

    with open(f"{prefix}//test.txt", "r") as f:
        test_inst = f.read().strip()
        test_tape = [int(s) for s in test_inst.split(',')]
        test_result = intcode.compute(test_tape)
        print(f"Test: {test_result}")

    with open(f"{prefix}//input.txt", "r") as f:
        inst = f.read().strip()
        tape = [int(s) for s in inst.split(',')]
        result = intcode.compute(tape)
        print(f"Part 1: {result}")

    with open(f"{prefix}//input2.txt", "r") as f:
        target = int(f.read().strip())

    # lazy bruteforce
    found = False
    for i in range(100):
        for j in range(100):
            if intcode.compute(tape, i, j) == target:
                found = True
                print(f"Part 2: {i} {j}")
                break
        if found: break

if __name__ == "__main__":
    execute(".")