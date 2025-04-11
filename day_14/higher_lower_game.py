'''
The goal is to build a game that asks the user to guess who has more followers on Instagram.
'''

import random
from art import logo, vs
from game_data import data

def get_competitor():
  return random.choice(data)

def format_data(person):
  name = person["name"]
  person_desc = person["description"]
  person_country = person ["country"]

  return f"{name}, {person_desc} from {person_country}"

def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "A"
  else:
    return guess == "B"

print(logo)

def game():
  score = 0
  game_should_continue = True
  person_a = get_competitor()
  person_b = get_competitor()

  while game_should_continue:
    person_a = person_b
    person_b = get_competitor()
    while person_a == person_b:
      person_b = get_competitor()

    print(f"Compare A: {format_data(person_a)}.\n{vs}\nB: {format_data(person_b)}.")

    guess = input("Guess who has more followers? Type 'A' or 'B': ").lower

    a_followers = person_a["follower_count"]
    b_followers = person_b["follower_count"]

    is_correct = check_answer(guess, a_followers, b_followers)

    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()
