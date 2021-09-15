# Addition
from art import logo
def add(n1,n2):
    return n1+n2

# Subtraction
def sub(n1,n2):
    return n1-n2

# Multiplication
def multiply(n1,n2):
    return n1*n2

# divide
def Divide(n1,n2):
    return n1/n2

operations={
    "+" : add,
    "-" : sub,
    "*" : multiply,
    "/" : Divide
}
def calculator():
    print(logo)
    num1 = float(input("Enter the first number: "))
    for operation in operations:
        print(operation)

    calc_run = True
    while calc_run:
        symbol = input("Pick a symbol from the operation given above: ")

        num2 = float(input("Enter the second number: "))

        calculation_function =operations[symbol]
        answer = calculation_function(num1,num2)
        print(f"{num1} {symbol} {num2} = {answer}")

        question =input("do you want to run with the same output y for yes , n for new : ")
        if question=="y":
            num1= answer
        else:
            calculator()
calculator()