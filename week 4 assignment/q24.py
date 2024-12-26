# given list is [1,2,3,4] but expected output is [1,8,27,64]

list = [1, 2, 3, 4]
new_list = []
for i in list:
    new_list.append(i**3)
    continue
print(new_list)