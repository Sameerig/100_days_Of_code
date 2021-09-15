def highest():
    A=start["follower_count"]
    print(A)
    B = another["follower_count"]
    print(B)
    game_end=False
    while not game_end:
        user = input("Which has more followers A or B? : ")
        
        if user=="A" and A>B:
            print("You win")
            A=B
        elif user=="B" and B>A:
            print("You win")
            A=B
        else:
            game_end= True
            print("You Lose")
import random
from art import logo
print(logo)

from game_data import data
start =random.choice(data)
print(start)

from art import vs

print(vs)

another = random.choice(data)

print(another)

highest()

