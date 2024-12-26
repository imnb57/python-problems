# . Python program that accepts a string and calculate the number of digits and letters and space

string = input("Enter a string: \n")
digit = 0
letter =0
space = 0
for i in string:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        letter += 1
    elif i.isspace():
        space += 1
print("Number of digits: ", digit)
print("Number of letters: ", letter)
print("Number of spaces: ", space)
