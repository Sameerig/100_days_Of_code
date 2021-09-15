import os
from art import logo
data ={}

def highest(record):
    highest_bid = 0
    winner = ""
    data ={}
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in record:
        bid_amount = record[bidder]
        if bid_amount > highest_bid: 
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

any_person=True
while any_person:
    print(logo)    
    name= input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    
    data[name] = bid
    print(data)
    question = input("Any other bidders?:")
    os.system('cls')
    if question=="no":
        highest(data)
        any_person= False
        print("good bye")