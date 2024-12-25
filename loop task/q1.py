# 1. Write a python program to reverse a given list using for loop. 
# a=[1,2,3,4]

a = [1,2,3,4]
for i in range(len(a)-1, -1,-1):
    print(a[i])