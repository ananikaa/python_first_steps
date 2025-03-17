# Functionality
# Each person writes their name and bid.
# The program asks if there are others who need to bid. If so, then the computer clears the output (prints several blank lines) then loops back to asking name and bid.
# Each person's name and bid are saved to a dictionary.
# Once all participants have placed their bid, the program works out who has the highest bid and prints it.

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)

name_price = {}

while True:
    key = input("What is your name?: ")
    value = int(input(f"What is your bid?: $"))
    bidders = input("Are there any other bidders? Type 'Yes' or 'No': ")
    name_price[key] = value
    if bidders.lower() == 'yes':
        print("\n" * 20)
    else:
        break

max_value = max(name_price.values())
winner = [key for key, value in name_price.items() if value == max_value][0]

print(f"The winner is {winner} with a bid of ${max_value}")





