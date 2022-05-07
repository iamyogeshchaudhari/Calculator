#Logo
from art import logo


#Calculation Function
def calculation(a, b, c):
  if c == "+":
    return a + b
  elif c == "-":
    return a - b
  elif c == "*":
    return a * b
  elif c == "/":
    return a / b
  else:
    return "Error. Please choose a valid operation."


def start_fresh():
  print(logo)
  first_num = float(input("What's the first number?: "))
  
  should_continue = True
  
  while should_continue == True:
    operation = input("What's the operation?: ")
    other_num = float(input("What's the other number?: "))
    
    #Result
    result = calculation(first_num, other_num, operation)
    print(f"{first_num} {operation} {other_num} = {result}")
    
    # Ask if further operation on result
    further_operation = input(f"Do you want to continue operating on {result}? Type 'y' for yes, 'n' to start a new calculation.: ")
  
    if further_operation == "y":
      should_continue = True
      first_num = result
  
    elif further_operation == "n":
      start_fresh()
      


start_fresh()