import random

from art import logo
print(logo)

from game_data import data

game_play= True

first= random.choice(data)
print(f"{first['name'] ,first['description'] ,first['country'] , }")
A= first["follower_count"] 
# print(A)
score= 0

while game_play:
    from art import vs
    print(vs)

    second= random.choice(data)
    print(f"{second['name'] ,second['description'] ,second['country'] }")
    B = second["follower_count"]
    # print(B)

    user =input("Which one has more Follower: A or B: ")
    if user =="A" and A>B:
        score=score+1
        A=B
        print(f"Your score is {score}")
    elif user=="B" and B>A:
        score=score+1
        A=B
        print(f"Your score is {score}")
    else:
        game_play = False
        print(f"You lose with score :{score}")