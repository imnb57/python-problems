
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
if number1 % 2 == 0 and number2 % 2 == 0:
    print(number1 + number2)
elif number1 % 2 == 0 or number2 % 2 == 0:
    print(number1 - number2)
else:
    print(number1 * number2)

