from turtle import Screen, Turtle
import turtle

tim = Turtle()

tim.shape("turtle")
for i in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(5)
    tim.pendown()




screen = Screen()
screen.exitonclick()