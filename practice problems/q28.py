score = float(input("Enter your subject score: "))

if score > 90:
    print("Congratulations on your excellent performance!")
elif 50 <= score <= 90:
    print("Good effort! You can improve further.")
else:
    print("You should retake the course and work harder.")
