



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
print("What operator would you like to use?: ")
for key in operator:
  print(key)
symbol = input()
num2 = int(input("What is the second number?: "))
function = operator[symbol]
result = function(num1, num2)

print(f"{num1} {symbol} {num2} = {result}")

symbol2 = input("Select another operator: ")
num3 = int(input("Whats the next number?: "))
function = operator[symbol2]
result2 = function(result, num3)

print(f"{result} {symbol2} {num3} = {result2}")