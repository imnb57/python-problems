# Accept string from the user and display only those characters which are 
# present at an odd index.

s = input("Enter a string: ")
print("Characters at odd index are: ", end="")
for i in range(1, len(s), 2):
    print(s[i], end=" ")
print()
