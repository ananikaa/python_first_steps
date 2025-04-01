import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")
guessed_number = random.randint(1, 100)

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

while difficulty_level != 'easy' and difficulty_level != 'hard':
  difficulty_level = input("Invalid input. Type 'easy' or 'hard': ").lower()

attempts = 10 if difficulty_level == "easy" else 5
print(f"You have {attempts} attempts remaining to guess the number")

while attempts > 0:
  user_assumes = int(input("Make a guess: "))

  if user_assumes < guessed_number:
    attempts -= 1
    print(f"Too low.\nYou have {attempts} attempts remaining to guess the number\nGuess again.")

  elif user_assumes > guessed_number:
    attempts -= 1
    print(f"Too high.\nYou have {attempts} attempts remaining to guess the number\nGuess again.")

  else:
    print(f"You guessed the number correctly! The number was: {guessed_number}")
    break

if attempts == 0:
  print(f"Sorry, you've run out of attempts. The number was: {guessed_number}.")