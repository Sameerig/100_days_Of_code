import random
number = int(input("Enter a random number :"))
random.seed(number)

toss=random.randint(0,1)
if toss ==1:
    print("Head")
else:
    print("Tail")