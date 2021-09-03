print("Welcome to the rollercoaster ! ")
height = int (input("What is your height in cm? "))

if height>= 120 :
    print("You are eligible for riding the rollercoaster! ")
    
    age = int(input("Now tell me your age:"))

    if age<=12:
        print("Your price for the ticket is 5 $")
    elif 12<age<=18:
        print("Your price for the ticket is 7 $")
    else:
         print("Your ticket price is 12$")
        
else:
    print("sorry you are not eligible!!")