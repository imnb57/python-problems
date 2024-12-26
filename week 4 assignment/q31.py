#  Write a for loop using an if statement, that appends each number to the new list if it's positive. given lst1=[111, 32, -9, -45, -17, 9, 85, -10]a

list1 = [111, 32, -9, -45, -17, 9, 85, -10]
new_list = []
for i in list1:
    if i > 0:
        new_list.append(i)
    else:
        continue
print(new_list)
