MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

def is_resource_sufficient(order_ingrident):
    '''Returns true when order can be made , false if ingridents are insufficient'''
    for item in order_ingrident:
        if order_ingrident[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        return True

def process_coin():
    '''Return the total calculated from coin inserted'''
    print("Please insert the coin")
    quarters =int(input("How many quarters?: "))
    dimes  = int(input("How many dimes?: "))
    nickles = int(input("How many nickels? :"))
    pennies = int(input("How many pennies? :"))
    total = 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies 
    return total


def is_transaction_successful(money_recieved , drink_cost):
    '''return true when the payment is accepted or False if money is insufficient'''
    if money_recieved>= drink_cost:
        change = round(money_recieved - drink_cost ,2)
        print(f"Here is {change} in change")
        global Money
        Money+= drink_cost
        
        return True
    else:
        print("Sorry thats not enough money  Money refunded")
        return False

def make_coffee(drink_name,order_ingredients):
    '''deducts the required from the resources'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} 🍵")
coffee_run = True
Money =0
while coffee_run:
    choise = input("What would you like to have ('espresso ', 'latte', 'cappuccino'): ")
    if choise=="off":
        coffee_run = False
        print("Good Bye")
    if choise=="report":
        print(f"Water : {resources['water']}")
        print(f"Milk : {resources['milk']}")
        print(f"Coffee : {resources['coffee']}")
        print(f"Money : {Money}")
    
    else:
        drink = MENU[choise]
        if is_resource_sufficient(drink["ingredients"]):
            payment =process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choise, drink["ingredients"])