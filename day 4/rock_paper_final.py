import random

Rock= """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper= """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors= """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
user =int(input("Enter a number 0 for Rock ,1 for paper and 2 for scissors: "))
if user==0:
    print(Rock)
elif user==1:
    print(Paper)
elif user==2:
    print(Scissors)

computer = random.randint(0,2)

if computer==0:
    print(Rock)
elif computer==1:
    print(Paper)
elif computer==2:
    print(Scissors)

if user==0 and computer==2 :
    print("You win!")
elif user==1 and computer==0:
    print("You win !")
elif user==2 and computer==1:
    print("You Win")
elif computer== user:
    print("Match tie! play again!")
else:
    print("You lose")