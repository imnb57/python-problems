# Python program to count the number of even and odd numbers from a series of numbers.  

even_count = 0
odd_count = 0
for i in range(1,9):
    if i%2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(even_count)
print(odd_count)