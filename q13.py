salary = float(input("Enter the salary: \n"))
serviceYears = int(input("Enter the number of years of service: \n"))

if serviceYears > 5:
    bonus = salary * 0.05
else:
    bonus = 0

net_bonus = bonus

print("The net bonus amount is:", net_bonus, "Rs")
