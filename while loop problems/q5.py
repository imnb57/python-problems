# 5. Write a Python program that keeps asking the user to enter a 
# day of the week. If the input is not "Sunday," print "It's not 
# the weekend yet." The loop should break and print "Enjoy your weekend!"
#  when the input is "Sunday."


while True:
    day = input("Enter a day of the week:\n")
    if day.lower() == 'sunday':
        print("Enjoy your weekend!")
        break
    else:
        print("It's not the weekend yet.")
        continue