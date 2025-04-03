''' Our Blackjack Game House Rules
The deck is unlimited in size.
There are no jokers.
The Jack/Queen/King all count as 10.
The Ace can count as 11 or 1.
Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

The cards in the list have equal probability of being drawn.
Cards are not removed from the deck as they are drawn.
The computer is the dealer.
'''

import random
from art import logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and cards > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

def compare(u_score,c_score):
  if u_score == c_score:
    return "Draw!"
  elif u_score == 0:
    return "Win with a Blackjack "
  elif c_score == 0:
    return "Lose, opponent has Blackjack"
  elif u_score > 21:
    return "You went over. You lose"
  elif c_score > 21:
    return "Opponent went over. You win!"
  elif u_score > c_score:
    return "You win!"
  else:
    return "You lose!"

def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}. Current score is: {user_score}.\nOpponent's first card is: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()

      if user_should_deal == 'y':
        user_cards.append(deal_card())
      elif user_should_deal != 'n':
        print("You typped an invalid input")
        continue
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hand: {user_cards}, final score: {user_score}\nComputer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while True:
  play_game()
  start_again = input("To play again type 'y': ").lower()
  if start_again != 'y':
    print("Thanks for the game!")
    break