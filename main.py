



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

num1 = int(input("What is the first number?: "))
num2 = int(input("What is the second number?: "))

print("What operator would you like to use?: ")
for key in operator:
  print(key)
symbol = input()

function = operator[symbol]
result = function(num1, num2)

print(f"{num1} {symbol} {num2} = {result}")