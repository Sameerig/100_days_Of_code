row1 = ["🍕","🍕","🍕"]
row2 = ["🍕","🍕","🍕"]
row3 = ["🍕","🍕","🍕"]
map =[row1, row2, row3]
# My code
print(f"{row1}\n{row2}\n{row3}\n")

user= input("enter the position: ")
row = int(user[0])
coloumn = int(user[1])

map[row-1][coloumn-1] ="X"
print(f"{row1}\n{row2}\n{row3}\n")