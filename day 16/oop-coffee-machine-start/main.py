from os import chmod
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine =MoneyMachine()
my_money_machine.report()

coffe_maker = CoffeeMaker()
coffe_maker.report()
is_on= True
menu = Menu()
while is_on:
    options = menu.get_items()
    choice = input("What do you like?({option}): ")

    if choice=="off":
        is_on= False
    elif choice =="report":
        coffe_maker.report()
        my_money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink):
            if my_money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)