# Given list is [1,2,3,"d",4,5,"a"] separate the elements based on their data types

int_list =[]
str_list =[]
list = [1, 2, 3, "d", 4, 5, "a"]
for i in list:
    if type(i) == int:
        int_list.append(i)
    elif type(i) == str:
        str_list.append(i)

print("Integer List: ", int_list)
print("String List: ", str_list)