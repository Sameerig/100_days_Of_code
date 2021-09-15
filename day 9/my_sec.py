import os

game_play =True
data={}

def highest(record):
    highest_bid=0
    winner =""
    for bidders in record:
       bid_amount = record[bidders]
       if bid_amount>highest_bid:
           highest_bid=bid_amount
           winner= bidders
           print(f"the highest bid is {highest_bid} by {winner}")
while game_play:
    name = input("What is your name? : ")
    bid = int(input("What's your bidding amount: $"))
    data[name] = bid
    print(data)

    question = input("Any otherr bidders?:")
    os.system('cls')
    if question=="no":
        game_play=False
        highest(data)
        print("Goodbye")