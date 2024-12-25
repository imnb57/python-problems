#  Write a Python program to print the even numbers from a given list. 
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Even numbers in the list are: ", end="")
for i in list:
    if i % 2 == 0:
        print(i, end=" ")
print()