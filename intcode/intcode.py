from functools import wraps

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
    return 0, True

  def write(self, output):
    print(output)

  def input(self, input):
    pass

  def terminate(self):
    self.terminated = True

class RealIO(IO):
  def read(self):
    return input("> "), True

class PreparedIO(IO):
  def __init__(self, io):
    super().__init__()
    self.i = 0
    self.io = io
    self.r = 0
    self.record = []

  def read(self):
    if len(self.io) <= self.i:
      return None, False
    result = self.io[self.i]
    self.i += 1
    return result, True

  def write(self, output):
    self.record.append(output)

  def input(self, input):
    self.io.append(input)

  def output(self):
    result = self.record[self.r]
    self.r += 1
    return result

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
  def __init__(self, func, count, *io):
    self.count = count
    self.func = func
    self.io = io

  def compute(self, args):
    if len(args) != self.count:
      raise ValueError("Incorrect argument length")
    return self.func(*self.io, *args)

  def __repr__(self):
    return f"OP {self.func.__name__}"

class Instance:
  def __init__(self, prog, *, noun='-', verb='-', prep=IO()):
    self.tape = TapeIO(prog, noun, verb)
    self.io = prep
    self.ops = compileOps(self.tape, self.io)
    self.mode_stack = []
    self.operation = None
    self.args = []
    self.active = True

  def result(self):
    return self.tape.output()

  def step(self):
    if self.tape.terminated:
      raise Exception("Intcode instance terminated before step")
    if self.active:
      if len(self.mode_stack) == 0:
        if self.operation == None:
          op = str(self.tape.read()[0])
          self.operation = self.ops[int(op[-2:])]
          op = '0' * (self.operation.count + 2 - len(op)) + op
          self.mode_stack = [c for c in op[:-2]]
      else:
        mode = self.mode_stack.pop()
        self.args.append(Argument(self.tape, self.tape.read()[0], mode))

    if not self.active or len(self.mode_stack) == 0:
      self.active = self.operation.compute(self.args)
      if self.active:
        self.args = []
        self.operation = None

  def fullsim(self):
    self.sim()
    if not self.active:
      raise Exception("Code exited active state in full simulation")
    return self.tape.output()

  def sim(self):
    while not self.tape.terminated:
      self.step()
      if not self.active: break

def neverpending(func):
  @wraps(func)
  def decor(*args, **kwargs):
    func(*args, **kwargs)
    return True
  return decor

def compileOps(tape, io):
  ops = dict()

  @neverpending
  def add(io, x, y, i): io[i.val()] = x.get() + y.get()

  @neverpending
  def mul(io, x, y, i): io[i.val()] = x.get() * y.get()

  def inp(tape, io, i):
    val, valid = io.read()
    if valid: tape[i.val()] = val
    return valid

  @neverpending
  def otp(io, i): io.write(i.get())

  @neverpending
  def jit(io, t, a):
    if (t.get() != 0): io.i = a.get()

  @neverpending
  def jif(io, t, a):
    if (t.get() == 0): io.i = a.get()

  @neverpending
  def ltc(io, x, y, a): io[a.val()] = (1 if (x.get() < y.get()) else 0)

  @neverpending
  def eqc(io, x, y, a): io[a.val()] = (1 if (x.get() == y.get()) else 0)

  @neverpending
  def end(io): io.terminate()

  ops[1] =  Opcode(add, 3, tape)
  ops[2] =  Opcode(mul, 3, tape)
  ops[3] =  Opcode(inp, 1, tape, io)
  ops[4] =  Opcode(otp, 1, io)
  ops[5] =  Opcode(jit, 2, tape)
  ops[6] =  Opcode(jif, 2, tape)
  ops[7] =  Opcode(ltc, 3, tape)
  ops[8] =  Opcode(eqc, 3, tape)
  ops[99] = Opcode(end, 0, tape)
  return ops

def arrayFromFile(file):
  with open(file, "r") as f:
    inst = f.read().strip()
  tape = [int(s) for s in inst.split(',')]
  return tape

def oneTimeRun(tape, noun='-', verb='-', prep=IO()):
  return Instance(tape, noun=noun, verb=verb, prep=prep).fullsim()