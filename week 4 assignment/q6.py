# 6. multiplication table of a given number

num = int(input("Enter a number:\n"))

for i in range(1,11):
    print(f"{num} x {i} = {num*i}")