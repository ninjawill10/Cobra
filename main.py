line = 0
variables = {}

with open("./main.Cb", "r") as file:
  commands = file.readlines()
  for command in commands:
    line += 1
    tokens = command.strip().split()

    if len(tokens) == 0:
      continue

    if tokens[0].lower() == "write":
      if len(tokens) == 1:
        print(f"Invalid syntax of '{' '.join(tokens)}' on line {line}")
      elif len(tokens) > 1:
        output_values = []
        for token in tokens[1:]:
          if token.startswith("$"):
            var_name = token[1:]
            if var_name in variables:
              output_values.append(variables[var_name])
            else:
              output_values.append(
                f"Error: Variable {var_name} is not defined")
          else:
            output_values.append(token)
        print(" ".join(output_values))
      else:
        print(f"Syntax error on line {line}")
    elif len(tokens) > 1 and tokens[1].lower() == "=":
      if len(tokens) < 3 or tokens[1].lower() != "=":
        print(f"Invalid syntax of '{' '.join(tokens)}' on line {line}")
      else:
        if tokens[2] == "input()":
          var_name = tokens[0]
          var_value = input()
          variables[var_name] = var_value
        else:
          var_name = tokens[0]
          var_value = " ".join(tokens[2:])
          variables[var_name] = var_value
    elif tokens[0].lower() == "maths":
      expression = " ".join(tokens[1:])
      result = eval(expression)
      print(result)
    elif tokens[0].lower() == "#":
      continue
    elif tokens[0].lower() == "clear":
      variables = {}
    else:
      print(f"Undefined command {tokens[0]} on line {line}")
