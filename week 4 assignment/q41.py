# . program to check given number is armstrong or not

num = 153
temp = num
sum = 0
while num > 0:
    dig = num % 10
    sum += dig ** 3
    num = num // 10

if temp == sum:
    print("The number is Armstrong!")
else:
    print("The number isn't Armstrong!")
    