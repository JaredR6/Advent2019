import os, sys

curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1, curdir + '/../intcode')
import intcode

def execute(prefix):

    test_tape = intcode.arrayFromFile(f"{prefix}//test.txt")
    test_result = intcode.oneTimeRun(test_tape)
    print(f"Test: {test_result}")

    tape = intcode.arrayFromFile(f"{prefix}//input.txt")
    result = intcode.oneTimeRun(tape)
    print(f"Part 1: {result}")

    with open(f"{prefix}//input2.txt", "r") as f:
        target = int(f.read().strip())

    # lazy bruteforce
    found = False
    for i in range(100):
        for j in range(100):
            if intcode.oneTimeRun(tape, noun=i, verb=j) == target:
                found = True
                print(f"Part 2: {i} {j}")
                break
        if found: break

if __name__ == "__main__":
    execute(".")