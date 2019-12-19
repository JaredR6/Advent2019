import os, sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1, curdir + '\\..')
import adventutil

import math

class Asteroid:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def angle(self):
    return (-math.pi/2 - math.atan2(self.x, self.y))

  def mag(self):
    return (self.x ** 2 + self.y**2)**.5

  def __repr__(self):
    return f"#({self.x},{self.y})"

  def __hash__(self):
    return hash(self.angle())

  def __eq__(self, other):
    return self.angle() == other.angle()

  def __lt__(self, other):
    if self.angle() == other.angle():
      return self.mag() < other.mag()
    return self.angle() < other.angle()

  def from_origin(self, other):
    return Asteroid(other.x + self.x, other.y + self.y)

  def view(self, other):
    return Asteroid(other.x - self.x, other.y - self.y)

def solve(input):
  x, y = 0, 0
  roids = []
  for row in input:
    x = 0
    for char in row:
      if char == '#':
        roids.append(Asteroid(x, y))
      x += 1
    y += 1
  hi = 0
  point = None
  for roid in roids:
    prsp = set()
    for roid2 in roids:
      if roid == roid2: continue
      prsp.add(roid.view(roid2))
    total = len(prsp)
    if hi < total:
      hi = total
      point = roid
  return hi, point, roids

def solve2(input):
  count, base, roids = input
  x = base.x
  y = base.y
  roids_rel = sorted([base.view(r) for r in roids])
  roids_rel.remove(Asteroid(0,0))
  roids_sorted = [[roids_rel[0]]]
  last = roids_rel[0]
  for roid in roids_rel[1:]:
    if roid == last:
      roids_sorted[-1].append(roid)
    else:
      roids_sorted.append([roid])
    last = roid
  count = 0
  index = 0
  while count < 199:
    del roids_sorted[index][0]
    if len(roids_sorted[index]) == 0:
      del roids_sorted[index]
    else:
      index += 1
    if index >= len(roids_sorted):
      index = 0
    count += 1
  final = base.from_origin(roids_sorted[index][0])
  return final.x * 100 + final.y

# Read tips:
# csv of numbers: readProblem()
# csv of words: readProblem(as_int=False)
# \n-sep words: readProblem(as_int=False, delim='\n')
# (Further processing may be required)

def execute(prefix='.'):
  adventutil.setPrefix(prefix)

  # Test

  test_inst = adventutil.readTest(as_int=False, delim='\n')
  result = solve(test_inst)
  print(f"Test: {result[0]}")

  # Part 1

  inst = adventutil.readProblem(as_int=False, delim='\n')
  result = solve(inst)
  print(f"Part 1: {result[0]}")

  # Part 2

  # inst = adventutil.readProblem('2')
  result2 = solve2(result)
  print(f"Part 2: {result2}")


if __name__ == "__main__":
  execute()