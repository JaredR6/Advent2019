import sys

def solve(input):
  return 42

def execute(prefix):

  # Test

  with open(f"{prefix}//test.txt", "r") as f:
    test_inst = f.read().strip()
    test_result = solve(test_inst)
    print(f"Test: {test_result}")

  # Part 1

  with open(f"{prefix}//input.txt", "r") as f:
    inst = f.read().strip()
    result = solve(inst)
    print(f"Part 1: {result}")

  # Part 2

  with open(f"{prefix}//input2.txt", "r") as f:
    target = f.read().strip()
    result = solve(inst)
    print(f"Part 2: {result}")


if __name__ == "__main__":
  execute(".")