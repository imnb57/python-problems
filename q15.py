a = int(input("Enter the number of students in class 1: \n"))
b = int(input("Enter the number of students in class 2: \n"))
c = int(input("Enter the number of students in class 3: \n"))

desk_a = (a + 1) // 2
desk_b = (b + 1) // 2
desk_c = (c + 1) // 2

total_desks = desk_a + desk_b + desk_c

print("The smallest possible number of desks that can be purchased:", total_desks)
