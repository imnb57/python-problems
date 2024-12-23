age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
experience = int(input("Enter your experience (years): "))

if age >= 21 and age <= 35:
    if gender == 'M':
        if experience >= 5:
            role = "Senior Developer"
        else:
            role = "Junior Developer"
    elif gender == 'F':
        if experience >= 5:
            role = "Senior Analyst"
        else:
            role = "Junior Analyst"
    else:
        role = "Invalid gender entered"
elif age > 35:
    role = "Manager Role"
else:
    role = "Not eligible due to age"

print(role)
