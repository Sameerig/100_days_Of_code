from tkinter import *

def mouse_click():
    my_label ["text"] = input.get()

window = Tk()
window.title("My first GUI programme")
window.minsize(width=500,height=300)


my_label = Label(text="I am a lebel",font=("Arial",24,"bold"))
my_label.grid(row=1,column=1)

my_label["text"] ="New_Text"
my_label.config(text="New text")

button = Button(text="Click me",command=mouse_click)
button.grid(row=2,column=
2)
new_button = Button(text ="iam button")
new_button.grid(row=1, column=3)

input = Entry(width=10)
input.grid(row=3,column=4)

window.mainloop()