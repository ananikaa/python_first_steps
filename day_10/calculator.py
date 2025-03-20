import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
  if n2 == 0:
    return "Cannot divide by zero"
  return n1 / n2

operations = {'+' : add,
              '-' : subtract,
              '*' : multiply,
              '/' : divide
}


continue_to_ask_questions = True

while continue_to_ask_questions:
  first_number = float(input("What is the first number?"))

  while True:
    chosen_operation = input("Pick an operation: \n+\n-\n*\n/")
    if chosen_operation not in operations:
      print("Invalid operator. Please try again.")
      continue
    break

  second_number = float(input("What is the second number?"))

  result = (operations[chosen_operation](first_number, second_number))
  print(result)

  # while to ensure that y or q is pressed
  while True:
    continue_calculating_or_new = input(f"Type 'y' to continue calculating or 'q' to quit: ").lower()
    if continue_calculating_or_new == "y":
      break
    elif continue_calculating_or_new == "q":
      print("Bye bye!")
      continue_to_ask_questions = False
      break  # Начинаем новый цикл с нового числа
    else: 
      print("Wrong input put either 'y' or 'q'")