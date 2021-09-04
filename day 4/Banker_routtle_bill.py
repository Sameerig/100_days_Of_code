import random

number = int(input("Enter a random number : "))

names = input("Enter the names : ")
name_list= names.split(',')
length = len(name_list)

r_number =random.randint(0,length-1) 
person =name_list[r_number]

print(f"{person} will have to pay for the everybody's food bill")