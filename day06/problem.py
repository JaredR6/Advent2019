import sys

def solve(input):
  system = dict()
  for entry in input:
    base, orbit = entry.split(')')
    if base in system:
      system[base].append(orbit)
    else:
      system[base] = [orbit]
  sum = 0
  step = 1
  search = ['COM']
  while len(search) > 0:
    next = []
    for base in search:
      if base in system:
        next.extend(system[base])
    sum += step * len(next)
    step += 1
    search = next
  return sum

def solve2(input):
  extend = dict()
  for entry in input:
    base, orbit = entry.split(')')
    if base in extend:
      extend[base].append(orbit)
    else:
      extend[base] = [orbit]
    if orbit in extend:
      extend[orbit].append(base)
    else:
      extend[orbit] = [base]
  dist = 0
  last = []
  search = [extend['YOU'][0]]
  final = extend['SAN'][0]
  while final not in search:
    dist += 1
    next = []
    for base in search:
      if base in extend:
        for entry in extend[base]:
          if entry not in last:
            next.append(entry)
    last = search
    search = next
  return dist

def execute(prefix):

  # Part 1

  with open(f"{prefix}//input.txt", "r") as f:
    inst = f.read().strip().split()
    result = solve(inst)
    print(f"Part 1: {result}")

  # Part 2

  with open(f"{prefix}//input.txt", "r") as f:
    inst = f.read().strip().split()
    result = solve2(inst)
    print(f"Part 2: {result}")


if __name__ == "__main__":
  execute(".")