# 5.Write a program to print the following using forloop
# a. first 10 even numbers
# b.first 10 odd numbers

even_number = []
for i in range(1,50):
    if i%2 == 0:
        even_number.append(i)
print(even_number[:10])

odd_number = []
for i in range(1,50):
    if i%2!= 0:
        odd_number.append(i)
print(odd_number[:10])