from turtle import Turtle,Screen

new_turtle = Turtle()
new_turtle.shape("turtle")

def move_forward():
    new_turtle.forward(10)

def move_backward():
    new_turtle.backward(10)

def move_left():
    new_turtle.left(10)

def move_right():
    new_turtle.right(10)

def clear():
    new_turtle.clear()
    new_turtle.home()
    new_turtle.pendown()


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()