#  Write a for loop which appends the type of each element in the first list to the second list.

a = [1, 2, 3, 4, 5, "hello", "world", 1.2, 3.4]
type_list = []
for i in a:
    type_list.append(type(i))
print(type_list)