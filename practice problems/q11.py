serviceYears = int(input("Enter the number of years of service: \n"))

if serviceYears > 10:
    bonus = 10
elif serviceYears >= 6 and serviceYears <= 10:
    bonus = 8
else:
    bonus = 5

print("The bonus percentage is:", bonus, "%")
