# 9. Write a program to find the largest number in a list: [3, 7, 2, 8, 5].

list = [3, 7, 2, 8, 5]
max = list[0]
for i in list:
    if i > max:
        max = i
print("The largest number in the list is", max)
