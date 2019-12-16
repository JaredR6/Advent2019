import importlib, os, shutil, sys

def error_exit(err):
  print(err)
  sys.exit(1)

def help_exit():
  error_exit(f"Usage: {sys.argv[0]} [-c] <day #>")

def get_day(daystr):
  try:
    day = int(daystr)
  except:
    help_exit()
  if day < 1 or day > 25:
    error_exit("Day out of bounds for advent calendar")

  dayname = str(day)
  if day < 10:
    dayname = 'day0' + dayname
  else:
    dayname = 'day' + dayname
  return day, dayname

# Basic single flag interpreter
if len(sys.argv) < 2:
  help_exit()

elif len(sys.argv) > 2:
  if sys.argv[1] != '-c':
    help_exit()

  day, dayname = get_day(sys.argv[2])

  if not os.path.isdir(dayname):
    os.mkdir(dayname)
  else:
    print("Skipping creating folder")
  if not os.path.exists(f"{dayname}//problem.py"):
    shutil.copyfile("base//problem.py", f"{dayname}//problem.py")
  else:
    print("Skipping copying base problem")
  if not os.path.exists(f"{dayname}//input2.txt"):
    shutil.copyfile("base//input2.txt", f"{dayname}//input2.txt")
  else:
    print("Skipping copying empty stage 2 input")
  if not os.path.exists(f"{dayname}//test.txt"):
    shutil.copyfile("base//test.txt", f"{dayname}//test.txt")
  else:
    print("Skipping copying empty test input")

  print(f"Folder \"{dayname}\" created and populated")

else:
  day, dayname = get_day(sys.argv[1])

  if not os.path.isdir(dayname):
    error_exit(f"Folder \"{dayname}\" does not exist")
  else:
    problem = importlib.import_module(f"{dayname}.problem")
    problem.execute(dayname)


