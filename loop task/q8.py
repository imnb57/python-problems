# 8. Write a program to print the factorial of a number accepted from user.

num = int(input("Enter a number:\n"))
fact = 1
for i in range(1,num+1):
    fact = fact * i
print(fact)
