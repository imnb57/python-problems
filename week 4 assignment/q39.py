# Write a for loop to find the sum of even and odd numbers separately in a range from 1 to 100.

even_sum = 0
odd_sum = 0
for i in range(1,101):
    if i%2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(even_sum)
print(odd_sum)
