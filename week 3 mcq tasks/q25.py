age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
show_type = input("Enter show type (Matinee/Evening): ").capitalize()

if age < 12:
    if show_type == "Matinee":
        ticket = 500
    else:
        ticket = 700
elif age >= 12 and age < 60:
    if gender == 'M':
        if show_type == "Matinee":
            ticket = 800
        else:
            ticket = 100
    else:
        if show_type == "Matinee":
            ticket = 700
        else:
            ticket = 900
else:
    ticket = 600

print(f"Ticket price: Rs{ticket}")
