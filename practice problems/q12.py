days = int(input("Enter the number of days: \n"))

if days <= 5:
    charge = days * 2
elif days >= 6 and days <= 10:
    charge = days * 3
elif days >= 11 and days <= 15:
    charge = days * 4
else:
    charge = days * 5

print("The total charge for the library is:", charge, "Rs")
