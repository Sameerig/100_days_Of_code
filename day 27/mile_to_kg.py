from tkinter import*
window = Tk()
window.minsize(width=300, height=100)
is_equal = Label(text="is equal to",font=("Arial",14,"bold"))
is_equal.grid(column=0 ,row=1)

value = Entry(width=10)
value.grid(column=1,row=0)

def solution():
    sol = float(value.get())
    km_result = round(sol*1.689)
    result.config(text=f"{km_result}")


Miles =Label(text="Miles",font=("Arial",14,"bold"))
Miles.grid(column=2,row=0)


km = Label(text="Km" ,font=("Arial",14,"bold"))
km.grid(column=3 , row=1)

result =Label(text="0" ,font=("Arial",14,"bold"))
result.grid(column=1 , row=1)

calculate = Button(text="Calculate",command=solution)
calculate.grid(row=2,column=1)

window.mainloop()