#  write a program to display integer from of a list. given list=[1,"a","c",2,3,4]

list=[1,"a","c",2,3,4]

for i in list:
    if isinstance(i,int):
        print(i)