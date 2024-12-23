age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
score = float(input("Enter your academic score (out of 100): "))

if age >= 18 and age <= 25:
    if gender == 'M':
        if score >= 85:
            result = "Full Scholarship"
        elif score >= 70:
            result = "Partial Scholarship"
        else:
            result = "No Scholarship"
    elif gender == 'F':
        if score >= 80:
            result = "Full Scholarship"
        elif score >= 65:
            result = "Partial Scholarship"
        else:
            result = "No Scholarship"
    else:
        result = "Invalid gender entered"
else:
    result = "Not eligible due to age"

print(result)
