import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

game_run = True

user1 = random.choice(cards)
user2 = random.choice(cards)

computer1 = random.choice(cards)
computer2 = random.choice(cards)

while game_run:

    user_total =user1+user2
    print(f"your cards are [{user1},{user2}] and your score is {user_total}")
    computer_total = computer1+computer2
    print(f"computer card is {computer1}")
    if computer_total==21:
        print("You win")
    elif computer_total<17:
        computer1 = computer_total
    elif computer_total>21:
        game_run= False
        print("computer Lose ")
        
    if user_total==21:
        print("You win")

    elif user_total>21:
        print("You lose")
    else:
        question =input("do you want to draw any card: ")
        if question =="yes":
            user1 = user_total
        elif question=="no":
            game_run=False
            print(f"computer chosses [{computer1},{computer2}] and his score is {computer_total} \nyou chosses [{user1},{user2}] and your score is {user_total}")

            if computer_total>user_total:
                print("Computer win")
            elif computer_total== user_total:
                print("Draw")
            else:
                print("You win")