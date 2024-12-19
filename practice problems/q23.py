age = int(input("Enter the age: \n"))
gender = input("Enter gender (M/F): \n")
num_days = int(input("Enter the number of working days: \n"))

if age >= 18 and age < 30:
    if gender == "M":
        print("Wage/day: 700")
    elif gender == "F":
        print("Wage/day: 750")
elif age >= 30 and age <= 40:
    if gender == "M":
        print("Wage/day: 800")
    elif gender == "F":
        print("Wage/day: 850")
else:
    print("No wage information available.")
