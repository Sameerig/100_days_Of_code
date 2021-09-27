import random
from turtle import Turtle, Screen
tim = Turtle()

colours =["Red", "Yellow","Orange", "Pink", "blue"]

tim.shape("turtle")

for i in range(3):
    tim.color(random.choice(colours))
    tim.right(120)
    tim.forward(80)


for i in range(4):
    tim.color(random.choice(colours))
    tim.right(90)
    tim.forward(80)


for i in range(5):
    tim.color(random.choice(colours))
    tim.right(72)
    tim.forward(80)


for i in range (6):
    tim.color(random.choice(colours))
    tim.right(60)
    tim.forward(80)


for i in range(8):
    tim.color(random.choice(colours))
    tim.right(45)
    tim.forward(80)

for i in range(10):
    tim.color(random.choice(colours))
    tim.right(36)
    tim.forward(80)

screen = Screen()
screen.exitonclick()