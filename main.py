line = 0
with open("./main.Cb", "r") as file:
  commands = file.readlines()
  for x in commands:
    line += 1
    if "Word: " in x:
      print(x.replace("Word: ", "").strip())
      continue
    if "InputVar: " in x:
      varname = x.replace("InputVar: ", "").strip()
      exec(f"{varname} = input()", globals())
      continue
    if "Var: " in x:
      Var = x.replace("Var: ", "")
      try:
          exec(f"print({Var})")
      except:
        print(f"\nError in line {line}:")
        print(f"The variable requested does not exist please check your spelling")
      continue
    if "Word+Var: " in x:
      print("hi")