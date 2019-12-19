import os, sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1, curdir + '\\..')
from PIL import Image
import adventutil, intcode

def solve(input):
  grid = {(0, 0): 0}
  coords = (0, 0)
  dir = (0, -1)
  count = 1
  prep = intcode.PreparedIO([0])
  inst = intcode.Instance(input, prep=prep)
  while True:
    inst.sim()
    if coords not in grid:
      count += 1
    grid[coords] = inst.io.output()
    if inst.tape.terminated:
      break
    if inst.io.output() == 0:
      dir = (dir[1], -dir[0])
    else:
      dir = (-dir[1], dir[0])
    coords = (coords[0] + dir[0], coords[1] + dir[1])
    if coords in grid:
      inst.io.input(grid[coords])
    else:
      inst.io.input(0)
  return count


def solve2(input):
  grid = {(0, 0): 1}
  coords = (0, 0)
  dir = (0, -1)
  bounds = ((0, 0), (0, 0))
  prep = intcode.PreparedIO([1])
  inst = intcode.Instance(input, prep=prep)
  while True:
    inst.sim()
    grid[coords] = inst.io.output()
    if inst.tape.terminated:
      break
    if inst.io.output() == 0:
      dir = (dir[1], -dir[0])
    else:
      dir = (-dir[1], dir[0])
    coords = (coords[0] + dir[0], coords[1] + dir[1])
    bounds = ((min(bounds[0][0], coords[0]), min(bounds[0][1], coords[1])),
              (max(bounds[1][0], coords[0]), max(bounds[1][1], coords[1])))
    if coords in grid:
      inst.io.input(grid[coords])
    else:
      inst.io.input(0)
  image_bounds = (bounds[1][0] - bounds[0][0] + 1, bounds[1][1] - bounds[0][1] + 1)
  center = (-bounds[0][0], -bounds[0][1])
  img = Image.new('1', image_bounds, 0)
  px = img.load()
  for coord in grid:
    spot = (coord[0] + center[0], coord[1] + center[1])
    px[spot[0], spot[1]] = grid[coord]
  img.show()

# Read tips:
# csv of numbers: readProblem()
# csv of words: readProblem(as_int=False)
# \n-sep words: readProblem(as_int=False, delim='\n')
# (Further processing may be required)

def execute(prefix='.'):
  adventutil.setPrefix(prefix)

  # Part 1

  inst = adventutil.readProblem()
  result = solve(inst)
  print(f"Part 1: {result}")

  # Part 2

  # inst = adventutil.readProblem('2')
  result = solve2(inst)


if __name__ == "__main__":
  execute()