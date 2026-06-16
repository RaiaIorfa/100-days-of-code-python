from ascii import *
from os import system

print(art)
print("^^^^^^^^^^^WELCOME TO THE AUCTION PROGRAM^^^^^^^^^^^")

auction_bids = {}

key = 0
highest_bid = 0
highest_bidder = ""

continue_bid = True
while continue_bid:
    name = input("What's your name? ")
    bid_amount = int(input("What's your bid? $"))
    new_bidders = input("Are there any other bidders? Type 'Yes' or 'No': ").lower() 

    auction_bids[f"bidder{key}"] =  {
        "name": name,
        "bid": bid_amount
    }

    if new_bidders == "yes":
        system("cls")
    else:
        continue_bid = False
        system("cls")

    key += 1
    for val in auction_bids.values():
        if val["bid"] > highest_bid:
            highest_bid = val["bid"]
            highest_bidder = val["name"]

print(auction_bids)
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
