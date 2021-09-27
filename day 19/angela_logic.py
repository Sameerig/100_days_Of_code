from turtle import Screen, Turtle
# import turtle
import random
import turtle


is_race_on = False

screen = Screen()

screen.setup(width=500, height=400)
user_bet =screen.textinput(title= "Make your bet", prompt="Which turtle will win the race?? Enter a colour: ")

colours =["red","orange","yellow","green","blue","purple","indigo"]
y_position =[-70 ,-40,-10,20,50,80]
all_turtle =[]
for _  in range(6):
    new_turtle=  Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colours[_])
    new_turtle.goto(x=-230 , y= y_position[_])
    all_turtle.append(new_turtle)


if user_bet :
    is_race_on = True
    
while is_race_on:

    for turtle in all_turtle:

        if turtle.xcor()>230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color== user_bet:
                print(f"You have won {wining_color} is the colour of winner")
            else:
                print(f"You have lost the {wining_color} turtle is the winner")
        distance = random.randint(0,10)
        turtle.forward(distance )


# print(user_bet)
screen.exitonclick()