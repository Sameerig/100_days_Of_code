from turtle import Screen, Turtle
# import turtle

screen = Screen()

screen.setup(width=500, height=400)
user_bet =screen.textinput(title= "Make your bet", prompt="Which turtle will win the race?? Enter a colour: ")

colours =["red","orange","yellow","green","blue","purple","indigo"]

new_turtle=  Turtle(shape="turtle")
rimyy=  Turtle(shape="turtle")
jimyy=  Turtle(shape="turtle")
simyy=  Turtle(shape="turtle")
tinyy=  Turtle(shape="turtle")
silyy=  Turtle(shape="turtle")
minyy=  Turtle(shape="turtle")

new_turtle.color(colours[0])
new_turtle.penup()
new_turtle.goto(x=-230,y=-100)

rimyy.color(colours[1])
rimyy.penup()
rimyy.goto(x=-230,y=100)

jimyy.color(colours[2])
jimyy.penup()
jimyy.goto(x=-230,y=-150)

simyy.color(colours[3])
simyy.penup()
simyy.goto(x=-230,y=150)

tinyy.color(colours[4])
tinyy.penup()
tinyy.goto(x=-230,y=50)

silyy.color(colours[5])
silyy.penup()
silyy.goto(x=-230,y=0)

minyy.color(colours[6])
minyy.penup()
minyy.goto(x=-230,y=-50)



print(user_bet)
screen.exitonclick()