import os
import time
def clear():
  os.system("clear")
global SayVar
line = 0
item1 = ""
item = 0
var4 = ""
with open("./main.Cb", "r") as file:
  commands = file.readlines()
  for x in commands:
    line += 1
    if "Say: " in x:
      print(x.replace("Say: ", "").strip())
      continue
    if "SaveVar: " in x:
      varname = x.replace("SaveVar: ", "").strip()
      exec(f"{varname} = input()", globals())
      continue
    if "SayVar" in x:
      SayVar = x.replace("SayVar: ", "")
      try:
          exec(f"print({SayVar})")
      except:
        print(f"\nError in line {line}:")
        print(f"The variable requested does not exist please check your spelling")
      continue
    if "Clear" in x:
      clear()
      continue
    if "Wait: " in x:
      wait = x.replace("Wait: ", "")
      time.sleep(int(wait))
      continue
    if "SayTextandVar" in x:
      import os
  def clear():
    os.system("clear")
  item = 0
  var4 = ""
  var = x
  item1 = ""
  for x in var:
    var1 = var[item]
    if var1 == "+":
      var3 = var1.replace("SayTextandVar: ", "")
      print(var3)
      break
    else:
      item1 = item1 + var1
    item += 1
  clear()
  item1 = item1.replace("SayTextandVar: ", "")
  var = var.replace("SayTextandVar: ", "")
  var = var.replace(item1, "")
  var = var.replace("+", "")
  var = var.replace(" ", "")
  var = var.replace(" ", "")
  exec(f"print(item1, {var})")
