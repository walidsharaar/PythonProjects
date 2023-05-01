#todo import the os library for clearing terminal
import os

#todo print the ASCII message to the user
from asciis import welcome_massege
print(welcome_massege)
print("Welcome to the secret auction program.")

#todo clear the terminal

def clear():
    os.system('cls')

#todo create function to find highest bidder
bids={}
bidding_closed = False

def find_bidder(biddin_record):
    highest_amount=0
    winner = ""
    #biddings={"a":123,"b":321}

    for bidder in biddin_record:
        amount= biddin_record[bidder]
        if amount > highest_amount:
            highest_amount = amount
            winner = bidder
    print(f"This winner for this bidding is {winner} with a bid of $ {amount}")


#todo create a empty dictory and while loop to get user input


while not bidding_closed:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_closed = True
        find_bidder(bids)
    elif should_continue == "yes":
        clear()




