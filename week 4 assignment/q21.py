#  Python program to calculate the sum of all the odd numbers within the given range.

odd_sum = 0
for i in range(1,9):
    if i%2 !=0:
        odd_sum += i
    
print(odd_sum)