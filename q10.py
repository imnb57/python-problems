grade = int(input("Enter the grade: "))

if grade < 25:
    result = "D"
elif grade >= 25 and grade < 45:
    result = "C"
elif grade >= 45 and grade < 50:
    result = "B"
elif grade >= 50 and grade < 60:
    result = "B+"
elif grade >= 60 and grade < 80:
    result = "A"
else:
    result = "A+"

print("The grade is:", result)
