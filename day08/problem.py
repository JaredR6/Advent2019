import os, sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1, curdir + '/..')
import adventutil.adventutil as util
from PIL import Image, ImageColor

def solve(input):
  img, x, y = input
  layer_size = x * y
  layers = [img[i:i+150] for i in range(0, len(img), layer_size)]
  hi = layer_size
  result = 0
  for layer in layers:
    count = layer.count('0')
    if count < hi:
      hi = count
      result = layer.count('1') * layer.count('2')
  return result

def solve2(input):
  img, x, y = input
  drawn = Image.new('RGBA', (x, y), ImageColor.colormap['gray'])
  px = drawn.load()
  layer_size = x * y
  layers = [img[i:i+150] for i in range(0, len(img), layer_size)]
  for j in range(y):
    for i in range(x):
      color = 2
      loc = j * x + i
      for layer in layers:
        if layer[loc] != '2':
          color = layer[loc]
          break
      if color == '0':
        px[i, j] = (0, 0, 0)
      elif color == '1':
        px[i, j] = (255, 255, 255)
  return drawn

def execute(prefix):

  # Part 1

  inst = util.readProblemStr(f"{prefix}//input.txt")
  x, y = [int(i) for i in util.readProblem(f"{prefix}//input2.txt")]
  result = solve((inst, x, y))
  print(f"Part 1: {result}")

  # Part 2

  result = solve2((inst, x, y))
  result.show()

if __name__ == "__main__":
  execute(".")