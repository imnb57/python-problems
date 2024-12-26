#  Print multiplication table of  1,2,3,4,5,6,7,8

for i in range(1, 9):
    print("Multiplication table of ", i)
    for j in range(1, 11):
        print(i, "*", j, "=", i*j)
    print()
    