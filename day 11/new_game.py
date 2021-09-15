import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
def calc():    
    user_1 = random.choice(cards)
    user_2 = random.choice(cards)
    comp = random.choice(cards)
    total = user_1+user_2
    print(f"your cards are  [{user_1},{user_2}] and score is = {total}")
    print(f"Dealer cards are {comp} and score is: {comp}")
    ask = input("Do you want to hit card: ")
    if ask =="y":
        user_3 =random.choice(cards)
        total_2 = total+user_3
        comp2 =random.choice(cards)
        comp_total =comp+comp2
        print(f"your cards are  [{total},{user_3}] and score is = {total_2}")
        print(f"Dealer cards are [{comp}, {comp}] and score is: {comp_total}")

        if comp_total<=21 and total_2<=21:
            if comp_total>total_2:
                print(f"Dealer wins with {comp_total} score")
            elif total_2>comp_total:
                print(f"CONGRATULATION😁😁 You win with {total_2} score")
        else :
            if comp_total>21:
                print(f"CONGRATULATION😁😁 You win with {total_2} score")
            elif total_2>21:
                print(f"Dealer wins with {comp_total} score")
    else:
        if total>comp:
            print(f"CONGRATULATION😁😁 You win with {total} score")
        elif comp>total:
            print(f"Dealer wins with {comp} score")

calc()