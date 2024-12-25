# Write a Python program to print the odd numbers from a given list. 
# Sample List : [12,13,14,15,16,17,18,19]

list = [12,13,14,15,16,17,18,19]
print("Odd numbers in the list are: ", end="")
for i in list:
    if i % 2 != 0:
        print(i, end=" ")
print()
