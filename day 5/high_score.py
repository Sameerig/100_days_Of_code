student_score = input("Enter the students score: ").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

max =0

for score in student_score:
    if score> max:
        max = score
print(f"The highest score is: {max}")