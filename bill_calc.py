print("Welcome  to the tip calculator")
total_bill = float(input("What was the total bill? "))
tip = float ( input("what percentage tip would you like to give? 10 , 12 or 15?  "))
total_people = float(input("How many people to spilit the bill? "))
each_person= (total_bill/total_people)
answer = (each_person* tip) /100
each_bill = round(answer+each_person,2)
print(f"Each person should pay :{each_bill}")
