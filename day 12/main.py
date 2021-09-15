def level (simplicity,no_of_attempt):
    game_run= True
    while game_run:
        guess = int(input("Enter a number: "))
        if guess==chosen:
            game_run= False
            print(f"You won with {no_of_attempt} attempts left")
        elif guess != chosen:
            no_of_attempt = no_of_attempt-1
            print(f"no of attempt remains {no_of_attempt}")
            if guess> chosen:
                print("TOO HIGH")
            elif guess<chosen:
                print("TOO LOW")

            if no_of_attempt==0:
                game_run= False
                print(f"Sorry you loose the answer was {chosen}")


import random
chosen = random.randint(1,100)

# print(chosen)

question = input("Choose a level hard or easy : ")

if question=="easy":
    no_of_attempt =10
elif question=="hard":
    no_of_attempt= 5
level(question, no_of_attempt)