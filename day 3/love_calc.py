# Dont change the code below:
name_1 = input("Enter your name: ")
name_2 = input("Enter their name: ")

your = name_1.lower()
their = name_2.lower()

a=your.count("t")
b=your.count("r")
c=your.count("u")
d=your.count("e")
e=your.count("l")
f=your.count("o")
g=your.count("v")
h=your.count("e")

your_add= (a+b+c+d+e+f+g+h)

i=their.count("t")
j=their.count("r")
k=their.count("u")
l=their.count("e")
m=their.count("l")
n=their.count("o")
o=their.count("v")
p=their.count("e")

their_add= (i+j+k+l+m+n+o+p)

percentage =(str(your_add)+ str(their_add))

love = int(percentage)


if love>10 or love<90:
    print(f"Your score is {love} % you go together like coke and mentos")
elif love>= 40 and love<=50:
    print(f"Your score is {love} % , you are allright together")
else:
    print(f"Your score is {love} %")