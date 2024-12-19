total_days = int(input("Enter the total number of days: \n"))
absent_days = int(input("Enter the total number of days absent: \n"))

present_days = total_days - absent_days
percentage = (present_days / total_days) * 100

print("Attendance Percentage:", percentage)

if percentage < 75:
    print("Student will not be able to sit in the exam.")
else:
    print("Student is eligible to sit in the exam.")
