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

while True:
  first_number = float(input("What is the first number?"))

  while True:
    chosen_operation = input("Pick an operation: \n+\n-\n*\n/")
    if chosen_operation not in operations:
      print("Invalid operator. Please try again.")
      continue

    second_number = float(input("What is the second number?"))

    if chosen_operation in operations:
      result = (operations[chosen_operation](first_number, second_number))
      print(result)

    else:
      print("invalid value")

    continue_calculating_or_new = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation (or 'q' to quit): ").lower()

    if continue_calculating_or_new == "y":
      first_number = result

    elif continue_calculating_or_new == "n":
      break  # Начинаем новый цикл с нового числа

    elif continue_calculating_or_new == "q":
      print("Goodbye!")
      exit()  # Полностью завершает программу

    else:
      start_again_after_fail = input("Invalid value\n Do you want to start again? Type 'y' for start again, type 'n' for end calculating").lower()
      if start_again_after_fail == 'y':
        break
      else:
        print("Goodbye!")
        exit()