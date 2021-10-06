from turtle import Turtle,Screen

from pandas._libs import missing
screen = Screen()
import pandas

image ="blank_states_img.gif"
screen.addshape(image)
screen.title("US STATES BY SAM")
kalu = Turtle()
kalu.shape(image)

data =pandas.read_csv("50_states.csv")
all_state=data["state"].to_list()

guessed_state =[]

while len(guessed_state)<50:

    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 states correct", prompt="What's the state name").title()
    guessed_state.append(answer_state)

    if answer_state=="Exit":
        missing_states=[states for states in all_state if states not in guessed_state]
        
        new_data = pandas.DataFrame(missing_states) 
        new_data.to_csv("state_data.csv")                       

        break

    if answer_state in all_state:
        t= Turtle()
        t.hideturtle()
        t.penup()

        state_data=data[data["state"]==answer_state]

        t.goto(int(state_data["x"]),int(state_data["y"]))

        t.write(answer_state)




screen.mainloop()