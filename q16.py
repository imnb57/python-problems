n = int(input("Enter the number of students: \n"))
k = int(input("Enter the number of apples: \n"))

apples_for_student = k // n
remaining_apples = k % n

print("Each student gets:", apples_for_student, "apples")
print("Apples remaining in the basket:", remaining_apples)
