height = int(input("Enter your height : "))

if height>=120:
    age= int(input("What is your age: "))
    photo = input("DO you want to take the photos: Y or N: ")
    if photo=="N":
        if age <=12:
            print("Child ticket of price 5$")
        elif age<=18:
            print("young ticket of price 7$")
        elif age >= 45 and age<= 55:
            print("Everything is going to be ok , have a free ride with us")
        else:
            print("Adult ticket  of price 12$")
    else:
        if age <=12:
            print("Child ticket of price 8$")
        elif age<=18:
            print("young ticket of price 10$")
        elif age >= 45 and age<= 55:
            print("Everything is going to be ok , kindly pay 3$ ")
        else:
            print("Adult ticket  of price 15$")
else:
    print("Sorry you are shorter ! ")