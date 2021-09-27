from turtle import Screen, Turtle
import random
import turtle

turtle.colormode(255)

timmy = Turtle()
timmy.pensize(2)
timmy.speed("fastest")

timmy.shape("turtle")

def random_colour():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)

    colours = (r, g, b)
    return colours

for i in range (53):
    timmy.color(random_colour())
    timmy.circle(100)
    timmy.left(7)









screen =Screen()

screen.exitonclick()