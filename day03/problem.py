import sys

# Postmortem: "begin -> next" and "start -> end" are very confusing

def get_next(start, inst):
  drt = inst[0]
  dist = int(inst[1:])
  final = list(start)
  if drt == 'R':
    final[0] += dist
  elif drt == 'L':
    final[0] -= dist
  elif drt == 'U':
    final[1] += dist
  elif drt == 'D':
    final[1] -= dist
  return tuple(final)

class Line:
  def __init__(self, start, inst):
    self.dist = int(inst[1:])
    self.begin = start
    self.next = get_next(start, inst)
    if inst[0] == 'D' or inst[0] == 'L':
      self.end = start
      self.start = self.next
    else:
      self.start = start
      self.end = self.next
    if inst[0] == 'U' or inst[0] == 'D':
      self.drt = 'V'
    else:
      self.drt = 'H'

  def __repr__(self):
    return f"({self.begin[0]}, {self.begin[1]}) -> ({self.next[0]}, {self.next[1]})"

  def between(self, loc):
    return abs(self.begin[0] - loc[0]) + abs(self.begin[1] - loc[1])

  def intersects(self, other):
    if self.drt == other.drt:
      if self.drt == 'H':
        if self.start[1] != other.start[1]:
          return False, None
        elif (other.start[0] <= self.start[0] and self.start[0] <= other.end[0]):
          return True, self.start
        elif (self.start[0] <= other.start[0] and other.start[0] <= self.end[0]):
          return True, other.start
        else:
          return False, None
      if self.drt == 'V':
        if self.start[0] != other.start[0]:
          return False, None
        elif (other.start[1] <= self.start[1] and self.start[1] <= other.end[1]):
          return True, self.start
        elif (self.start[1] <= other.start[1] and other.start[1] <= self.end[1]):
          return True, other.start
        else:
          return False, None
    else:
      if self.drt == 'H':
        vrt, hrz = other, self
      else:
        vrt, hrz = self, other
      if vrt.start[0] < hrz.start[0] or hrz.end[0] < vrt.start[0]:
        return False, None
      if hrz.start[1] < vrt.start[1] or vrt.end[1] < hrz.start[1]:
        return False, None
      return True, (vrt.start[0], hrz.start[1])

def solve(input):
  wires0, wires1 = [], []
  x, y = 0, 0
  for path in input[0]:
    line = Line((x, y), path)
    x, y = line.next
    wires0.append(line)

  x, y = 0, 0
  for path in input[1]:
    line = Line((x, y), path)
    x, y = line.next
    wires1.append(line)

  minmat, minwalk = None, None
  walk0 = 0
  for l in wires0:
    walk1 = 0
    for m in wires1:
      result, loc = l.intersects(m)
      if result:
        distmat = abs(loc[0]) + abs(loc[1])
        distwalk = walk0 + walk1 + l.between(loc) + m.between(loc)
        if distmat != 0:
          if minmat == None or minmat > distmat:
            minmat = distmat
          if minwalk == None or minwalk > distwalk:
            minwalk = distwalk
      walk1 += m.dist
    walk0 += l.dist

  return minmat, minwalk

def execute(prefix):

  # Test

  with open(f"{prefix}//test.txt", "r") as f:
    test_inst = f.read().strip()
    test_wires = test_inst.split('\n')
    test_wires[0] = test_wires[0].split(',')
    test_wires[1] = test_wires[1].split(',')
    test_result = solve(test_wires)
    print(f"Test: {test_result}")

  # Unique

  with open(f"{prefix}//input.txt", "r") as f:
    inst = f.read().strip()
    wires = inst.split('\n')
    wires[0] = wires[0].split(',')
    wires[1] = wires[1].split(',')
    result = solve(wires)
    print(f"Result: {result}")


if __name__ == "__main__":
  execute(".")