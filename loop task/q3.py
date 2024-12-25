# 3.Write a python program to print a multiplication table of any number using for loop. 

num = int(input("Enter a number:\n"))
for i in range(1,11):
    print( num, "x" ,i ,"=",num*i,"\n")