import sys

def solve(tape, noun=-1, verb=-1):
    if noun == -1: noun = tape[1]
    if verb == -1: verb = tape[2]
    tape = tape.copy()
    tape[1] = noun
    tape[2] = verb
    max = len(tape)
    head = 0
    try:
        while True:
            if tape[head] == 1:
                i = tape[tape[head + 1]]
                j = tape[tape[head + 2]]
                tape[tape[head + 3]] = i + j
                head += 4
            elif tape[head] == 2:
                i = tape[tape[head + 1]]
                j = tape[tape[head + 2]]
                tape[tape[head + 3]] = i * j
                head += 4
            elif tape[head] == 99:
                break
            else:
                print(f"Error: undefined code at position {head}: [{tape[head]}]")
                break
    except IndexError:
        print("Error: tape length exceeded")
    return tape[0]

def execute(prefix):
    with open(f"{prefix}//test.txt", "r") as f:
        test_inst = f.read().strip()
        test_tape = [int(s) for s in test_inst.split(',')]
        test_result = solve(test_tape)
        print(f"Test: {test_result}")

    with open(f"{prefix}//input.txt", "r") as f:
        inst = f.read().strip()
        tape = [int(s) for s in inst.split(',')]
        result = solve(tape)
        print(f"Part 1: {result}")

    with open(f"{prefix}//input2.txt", "r") as f:
        target = int(f.read().strip())

    # lazy bruteforce
    found = False
    for i in range(100):
        for j in range(100):
            if solve(tape, i, j) == target:
                found = True
                print(f"Part 2: {i} {j}")
                break
        if found: break

if __name__ == "__main__":
    execute(".")