age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
membership_type = input("Enter membership type (Monthly/Yearly): ").capitalize()

if age >= 18 and age < 30:
    if gender == 'M':
        if membership_type == "Monthly":
            fee = 50
        else:
            fee = 500
    else:
        if membership_type == "Monthly":
            fee = 45
        else:
            fee = 450
elif age >= 30 and age <= 50:
    if membership_type == "Monthly":
        fee = 60
    else:
        fee = 600
else:
    if membership_type == "Monthly":
        fee = 40
    else:
        fee = 400

print(f"Membership fee: Rs{fee}")
