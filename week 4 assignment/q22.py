#  Python program to calculate the sum of all the even numbers within the given range.

even_sum = 0
for i in range(1,9):
    if i%2 == 0:
        even_sum += i
    
print(even_sum)