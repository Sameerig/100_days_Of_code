from typing import cast


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
    
def coin():

    print("Please insert the coin")
    quarters =int(input("How many quarters?: "))
    dimes  = int(input("How many dimes?: "))
    nickles = int(input("How many nickels? :"))
    pennies = int(input("How many pennies? :"))
    total = 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies 
    return total

def calc(user):
    required_water = MENU[user]["ingredients"]["water"]
    required_milk = MENU[user]["ingredients"]["milk"]
    required_coffee = MENU[user]["ingredients"]["coffee"]

    if required_water> resources["water"] or required_milk> resources["milk"] or required_coffee> resources["coffee"]:
        return False
    else:
        resources["water"] = resources["water"]- required_water
        resources["milk"] = resources["milk"]- required_milk
        resources["coffee"] = resources["coffee"]- required_coffee
        return True


machine_work= True
while machine_work:
    user = input("What do you like to have ('espresso','latte', 'cappuccino'): ")
    if user =="off":
        machine_work = False
    elif user=="espresso":
        if calc(user):
            amount=coin()
            if amount>= MENU[user]["cost"]:
                in_return=round(amount- MENU["espresso"]["cost"],2)
                print(f"Here is your change {in_return}")
                calc(user)
            else:
                print("Not enough Money")
        else:
            print(f"sorry not enough resources to make {user}")
    elif user=="latte":
        if calc(user):
            amount=coin()
            if amount>= MENU[user]["cost"]:
                in_return=round(amount-MENU["latte"]["cost"],2)
                print(f"Here is your change {in_return}")
                calc(user)
            else:
                print("Not enough money")
        else:
            print(f"Sorry not enough item to make {user}")
    elif user=="cappuccino":
        if calc(user):
            amount = coin()
            if amount>= MENU[user]["cost"]:
                in_return= round(amount-MENU["cappuccino"]["cost"],2)
                print(f"Here is your change {in_return}")
                calc(user)
            else:
                print("Not enough money")
        else:
            print(f"Sorry not enough item to make {user} ")
    elif user=="report":
        print(f'Water : {resources["water"]}')
        print(f'Milk : {resources["milk"]}')
        print(f'Coffee : {resources["coffee"]}')