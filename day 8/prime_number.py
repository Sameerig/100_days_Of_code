def prime_check(number):
    prime = True
    for i in range(2,number -1):
        if number%i==0:
            prime=False
    if prime:
        print("It is a prime number")
    else:
        print("It is not a prime number")
n = int(input("Enter a number you want to check:"))

prime_check(number=n)