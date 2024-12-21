num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(f"The greater number is: {num1}")
elif num1 < num2:
    print(f"The greater number is: {num2}")
else:
    if num1 > 0:
        print("The numbers are equal and positive.")
    elif num1 < 0:
        print("The numbers are equal and negative.")
    else:
        print("The numbers are equal and zero.")
