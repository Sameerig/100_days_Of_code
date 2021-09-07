# Dont change the code below

students_heights = input("Input a list of student height : ").split()


for n in range(0,len(students_heights)):
    students_heights[n] = int(students_heights[n])
print(students_heights)
total_height =0
for height in students_heights:
    total_height=total_height+height
print(total_height)

no_of_student =0
for student in students_heights:
    no_of_student= no_of_student+1
print(f"The number of students are {no_of_student}")

avg_height = total_height/no_of_student
print(round(avg_height))