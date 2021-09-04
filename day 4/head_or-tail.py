import random
user = input("Enter the random number: ")
random.seed(user)

side = random.randint(0,1)

if side==1:
    print("Heads")
else:
    print("Tail")
