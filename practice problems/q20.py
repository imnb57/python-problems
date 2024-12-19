num1 = int(input("Enter First Number: \n"))
num2 = int(input("Enter Second Number: \n"))
operator = input("Enter operator (+, -, *, /): \n")

if operator == '+':
    print("Your Answer is:", num1 + num2)
elif operator == '-':
    print("Your Answer is:", num1 - num2)
elif operator == '*':
    print("Your Answer is:", num1 * num2)
elif operator == '/':
    if num2 != 0:
        print("Your Answer is:", num1 / num2)
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid operator.")
