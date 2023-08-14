from art import logo



#Calculator
def add(n1, n2):
  return(n1 + n2)

def subtract(n1, n2):
  return(n1 - n2)

def multiply(n1, n2):
  return(n1 * n2)

def divide(n1, n2):
  return(n1 / n2)

operator = {"+": add, "-": subtract, "*": multiply, "/": divide}
cont = True
def calculator():
  print(logo)

calculator()
num1 = float(input("What is the first number?: "))
print("What operator would you like to use?: ")
for key in operator:
  print(key)
symbol = input()
num2 = float(input("What is the second number?: "))
function = operator[symbol]
result = function(num1, num2)

print(f"{num1} {symbol} {num2} = {result}")

keep_going = input(f"'y' to continue with {result}, or 'n' to exit  ")
if keep_going == "n":
  cont = False
while cont:
  calculator
  symbol = input("Pick another operator: ")
  num3 = float(input("What is the next number?: "))
  function = operator[symbol]
  new_result = function(result, num3)

  print(f"{result} {symbol} {num3} = {new_result}")
  result = new_result

  keep_going = input(f"'y' to continue with {result}, or 'n' to exit  ")
  if keep_going == "n":
    cont = False