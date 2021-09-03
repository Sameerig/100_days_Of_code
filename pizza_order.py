print("Welcome to the Python Pizza deliveres")
size = input("What size Pizza do you want? S, M, L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# My code:
Small_pizza = 15
Medium_pizza = 20
Large_pizza = 25
pepperoni_s= 2
pepperoni_l =3
cheese= 1

if size=="S":
    if add_pepperoni=="Y":
        if extra_cheese =="Y":
            print(f"the price for the pizza is {Small_pizza+pepperoni_s+cheese} with pepperoni and cheese")
        else:
            print(f"The price for the pizza is {Small_pizza+pepperoni_s} with pepperoni and NO cheese")
    else:
        print(f"The price for the pizza is {Small_pizza} with No pepperoni and No cheese")

elif size=="M":
    if add_pepperoni=="Y":
        if extra_cheese=="Y":
            print(f"the price for the pizza is {Medium_pizza+pepperoni_l+ cheese} with pepperoni and chesse")
        else:
            print(f"the price for the pizza is {Medium_pizza+pepperoni_l} with pepperoni and NO chesse")
    else:
        print(f"the price for the pizza is {Medium_pizza} with  NO pepperoni and No chesse")
        
else :
    if add_pepperoni=="Y":
        if extra_cheese=="Y":
            print(f"the price for the pizza is {Large_pizza+pepperoni_l+ cheese} with pepperoni and chesse")
        else:
            print(f"the price for the pizza is {Large_pizza+pepperoni_l} with pepperoni and NO chesse")
    else:
        print(f"the price for the pizza is {Large_pizza} with NO pepperoni and NO chesse")