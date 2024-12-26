lst = [1, 2, 3, 4]
result = []

# Loop through the original list
for item in lst:
    if item == 2:
        result.append("a")  # Replace 2 with "a"
    elif item == 3:
        result.append(2)  # Replace 3 with 2
    else:
        result.append(item)  # Keep other items as they are

print(result)
