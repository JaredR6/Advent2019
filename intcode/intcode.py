class Argument:
  def __init__(self, io, value, mode):
    self.io = io
    self.value = int(value)
    self.mode = mode

  def get(self):
    if self.mode == '0':
      return self.io[self.value]
    elif self.mode == '1':
      return self.value
    else:
      raise ValueError("Invalid mode within argument get")

  def val(self):
    return self.value

  def __repr__(self):
    return f"{self.value} [{self.mode}]"

class IO:
  def __init__(self):
    self.terminated = False

  def read(self):
    return 0

  def write(self, output):
    print(output)

  def terminate(self):
    self.terminated = True

class PreparedIO(IO):
  def __init__(self, io):
    super().__init__()
    self.i = 0
    self.io = io
    self.record = []

  def read(self):
    result = self.io[self.i]
    self.i += 1
    return result

  def write(self, output):
    self.record.append(output)

class RealIO(IO):
  def read(self):
    return input("> ")

class TapeIO(PreparedIO):
  def __init__(self, io, noun='-', verb='-'):
    super().__init__(io.copy())
    if noun != '-':
      self.io[1] = noun
    if verb != '-':
      self.io[2] = verb

  def memread(self):
    return self.io[self.read()]

  def __getitem__(self, key):
    return self.io[key]

  def write(self, output, index):
    self.io[index] = output

  def __setitem__(self, key, value):
    self.write(value, key)

  def output(self):
    return self.io[0]

class Opcode:
  def __init__(self, count, io, func):
    self.count = count
    self.func = func
    self.io = io

  def compute(self, args):
    if len(args) != self.count:
      raise ValueError("Incorrect argument length")
    self.func(self.io, *args)

  def __repr__(self):
    return f"{self.func.__name__}"

class DualOpcode(Opcode):
  def __init__(self, count, tape, io, func):
    super().__init__(count, io, func)
    self.tape = tape

  def compute(self, args):
    if len(args) != self.count:
      raise ValueError("Incorrect argument length")
    self.func(self.tape, self.io, *args)

def compileOps(tape, io):
  ops = dict()
  def add(io, x, y, i): io[i.val()] = x.get() + y.get()
  def sub(io, x, y, i): io[i.val()] = x.get() * y.get()
  def inp(tape, io, i): tape[i.val()] = io.read()
  def otp(tape, io, i): io.write(i.get())
  def jit(io, t, a):
    if (t.get() != 0): io.i = a.get()
  def jif(io, t, a):
    if (t.get() == 0): io.i = a.get()
  def ltc(io, x, y, a): io[a.val()] = (1 if (x.get() < y.get()) else 0)
  def eqc(io, x, y, a): io[a.val()] = (1 if (x.get() == y.get()) else 0)
  def end(io): io.terminate()
  ops[1] =  Opcode(3, tape, add)
  ops[2] =  Opcode(3, tape, sub)
  ops[3] =  DualOpcode(1, tape, io, inp)
  ops[4] =  DualOpcode(1, tape, io, otp)
  ops[5] =  Opcode(2, tape, jit)
  ops[6] =  Opcode(2, tape, jif)
  ops[7] =  Opcode(3, tape, ltc)
  ops[8] =  Opcode(3, tape, eqc)
  ops[99] = Opcode(0, tape, end)
  return ops

def compute(prog, noun='-', verb='-', io=IO()):
  tape = TapeIO(prog, noun, verb)
  ops = compileOps(tape, io)
  mode_stack = []
  operation = None
  args = []
  while not tape.terminated:
    if len(mode_stack) == 0:
      if operation == None:
        op = str(tape.read())
        operation = ops[int(op[-2:])]
        op = '0' * (operation.count + 2 - len(op)) + op
        mode_stack = [c for c in op[:-2]]
    else:
      mode = mode_stack.pop()
      args.append(Argument(tape, tape.read(), mode))
    if len(mode_stack) == 0:
      operation.compute(args)
      args = []
      operation = None
  return tape.output()