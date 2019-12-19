import os, sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1, curdir + '\\..')
import adventutil
import math

## NAIVE SOLUTION

class Moon:
  def __init__(self, x, y, z):
    self.pos = [x, y, z]
    self.vel = [0, 0, 0]

  def pair_update(self, other):
    for i in range(3):
      if self.pos[i] > other.pos[i]:
        self.vel[i] -= 1
        other.vel[i] += 1
      elif self.pos[i] < other.pos[i]:
        self.vel[i] += 1
        other.vel[i] -= 1

  def step(self):
    for i in range(3):
      self.pos[i] += self.vel[i]

  def energy(self):
    pot, kin = 0, 0
    for i in range(3):
      pot += abs(self.pos[i])
      kin += abs(self.vel[i])
    return pot * kin

def solve(input):
  moons = []
  for line in input:
    vars = line.split(', ')
    x = int(vars[0][3:])
    y = int(vars[1][2:])
    z = int(vars[2][2:-1])
    moons.append(Moon(x, y, z))
  for _ in range(1000):
    for i in range(len(moons)):
      for j in range(i+1, len(moons)):
        moons[i].pair_update(moons[j])
    for moon in moons:
      moon.step()
  energy = 0
  for moon in moons:
    energy += moon.energy()
  return energy

##

def find_loop(pos):
  vel = [0, 0, 0, 0]
  orig = ((tuple(pos), tuple(vel)))
  count = 0
  while True:
    for i in range(4):
      for j in range(i+1, 4):
        if pos[i] > pos[j]:
          vel[i] -= 1
          vel[j] += 1
        elif pos[i] < pos[j]:
          vel[i] += 1
          vel[j] -= 1
    for i in range(4):
      pos[i] += vel[i]
    count += 1
    key = (tuple(pos), tuple(vel))
    if key == orig:
      return count


def solve2(input):
  x = []
  y = []
  z = []
  for line in input:
    vars = line.split(', ')
    x.append(int(vars[0][3:]))
    y.append(int(vars[1][2:]))
    z.append(int(vars[2][2:-1]))
  xloop = find_loop(x)
  yloop = find_loop(y)
  zloop = find_loop(z)
  tmp = xloop // math.gcd(xloop, yloop) * yloop
  return tmp // math.gcd(tmp, zloop) * zloop

# Read tips:
# csv of numbers: readProblem()
# csv of words: readProblem(as_int=False)
# \n-sep words: readProblem(as_int=False, delim='\n')
# (Further processing may be required)

def execute(prefix='.'):
  adventutil.setPrefix(prefix)

  # Part 1

  inst = adventutil.readProblem(as_int=False, delim='\n')
  result = solve(inst)
  print(f"Part 1: {result}")

  # Test

  test_inst = adventutil.readTest(as_int=False, delim='\n')
  result = solve2(test_inst)
  print(f"Test: {result}")

  # Part 2

  # inst = adventutil.readProblem('2')
  result = solve2(inst)
  print(f"Part 2: {result}")


if __name__ == "__main__":
  execute()