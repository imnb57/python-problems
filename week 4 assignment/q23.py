#  Python program to count the space of a given string

string = "Python is a programming language"
space_count = 0
for i in string:
    if i == " ":
        space_count += 1
    else:
        continue
print(space_count)
