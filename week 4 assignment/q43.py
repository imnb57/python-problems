#  python program to check a number is perfect number

num = 28
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum +=i
if sum == num:
    print("The number is a Perfect number!")
else:
    print("The number isn't a Perfect number!")
    
