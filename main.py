from tkinter import *
from tkinter import messagebox
import random

# generating password
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_letter =[random.choice(letters) for _ in range(random.randint(8,10))]

    password_symbols =[random.choice(symbols) for _ in range(random.randint(2,4))]

    password_number =[random.choice(letters) for _ in range(random.randint(2,4))]


    password_list = password_letter+password_number+password_symbols

    # print(password_list)
    random.shuffle(password_list)
    # print(password_list)

    password ="".join(password_list)
    password_entry.insert(0,password)


# saving in files
def save():
    website = webiste_entry.get()
    email = email_entry.get()
    password =password_entry.get()

    if len(website)>0 and len(email)>0 and len(password)>0:

        is_ok = messagebox.askokcancel(title=website, message=f"Theese are the details entered:\n Email:{email}\n Password: {password}\n is it okey to save?")

        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                webiste_entry.delete(0,END)
                password_entry.delete(0,END)
    else:
        messagebox.showinfo(title="OOPS", message="Please don't left any field empty")


window = Tk()
window.title("Sameer's app")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
lock_image =PhotoImage(file="logo.png")
canvas.create_image(100,100,image = lock_image)
canvas.grid(row=0,column=1)


#LEBEl


website_label = Label(text="Webiste: ")
website_label.grid(row=1,column=0)


emial_gmail = Label(text="Email/Username: ")
emial_gmail.grid(row=2,column=0)

password_lebel =Label(text="Password: ")
password_lebel.grid(row=3,column=0)


website_label = Label(text="Webiste: ")
website_label.grid(row=1,column=0)

# Entry

webiste_entry = Entry(width=36)
webiste_entry.grid(row=1,column=1,columnspan=2)
webiste_entry.focus()

email_entry = Entry(width=36)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"xyz@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

# Button
generate_password =Button(text="Generate Password" ,command=generate_password)
generate_password.grid(row=3,column=2)

add_button = Button(text="Add" , width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()