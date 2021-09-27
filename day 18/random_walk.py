import random
from turtle import Screen, Turtle, left, right
import turtle

tim = Turtle()
tim.shape("turtle")
tim.pensize(13)
tim.speed("fastest")

turtle.colormode(255)

def random_colour():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)

    colours =(r,g,b)
    return colours

direction =[0,90,180,270]

def random_walk():
    tim.color(random_colour())
    walk=random.choice(direction)
    tim.forward(30)
    tim.setheading(walk)


for i in range(200):
    random_walk()


screen = Screen()
screen.exitonclick()