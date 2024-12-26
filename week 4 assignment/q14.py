# Given list is [1,2,3,4,"a","b"] append each elements datatypes to separate lists.
int_list = []
str_list = []
list = [1, 2, 3, 4, "a", "b"]
for i in list:
    if type(i) == int:
        int_list.append(type(i))
    elif type(i) == str:
        str_list.append(type(i))
print("Integer List: ", int_list,"\n")
print("String List: ", str_list)
