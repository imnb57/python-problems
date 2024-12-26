# . Write a program to determine whether a given number is a prime number.

num = 11
flag = 0
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        flag = 1 
        break
if flag == 0:
    print("Prime")
else:
    print("Not Prime")
