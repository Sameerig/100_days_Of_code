from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card ={}
to_learn={}
try:
    data =pandas.read_csv("data\Words_to_Learn.csv")
except:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card =random.choice(to_learn)
    # print(current_card["French"])
    canvas.itemconfigure(title_text,text="French",fill ="black")
    canvas.itemconfigure(title_word,text=current_card["French"],fill="black")
    canvas.itemconfigure(card_front,image =fromt_image)
    flip_timer=window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfigure(title_text,text= "English",fill ="white")
    canvas.itemconfigure(title_word,text=current_card["English"],fill="white")
    canvas.itemconfigure(card_front,image=back_image)

def is_known():
    to_learn.remove(current_card)
    next_card()

    data=pandas.DataFrame(to_learn)
    data.to_csv("data/Words_to_Learn.csv",index=False)

window =Tk()
window.title("Flash game")
window.config(padx=50,pady=50 ,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flip_card)
canvas= Canvas(width=800,height=526 ,bg=BACKGROUND_COLOR,highlightthickness=0)
fromt_image=PhotoImage(file="images\card_front.png")

back_image = PhotoImage(file="images\card_back.png")

card_front=canvas.create_image(400,263,image=fromt_image)

title_text =canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))

title_word = canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"))

canvas.grid(row=0,column=0,columnspan=2)

# Buttons
wrong_image = PhotoImage(file="images\wrong.png")
cancel_button = Button(image=wrong_image ,highlightthickness=0,command=next_card)
cancel_button.grid(row=1,column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)

next_card()
window.mainloop()