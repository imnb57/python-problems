# Accept string from the user and display only those characters which are 
# present at an even index.

s = input("Enter a string: ")
print("Characters at even index are: ", end="")
for i in range(0, len(s), 2):
    print(s[i], end=" ")
print()
