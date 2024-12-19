percentage = float(input("Enter the percentage: \n"))

if percentage < 40:
    print("Category: Failed")
elif percentage >= 40 and percentage < 55:
    print("Category: Fair")
elif percentage >= 55 and percentage < 65:
    print("Category: Good")
else:
    print("Category: Excellent")
