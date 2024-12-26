# Given list is [1,2,3,4,5] separate the elements into odd and even categories.

list = [1, 2, 3, 4, 5]
odd =[]
even =[]

for i in range(0, len(list)):
    if list[i] % 2 == 0:
        even.append(list[i])
    else:
        odd.append(list[i])
print("Even numbers are: ", even)
print("Odd numbers are: ", odd)