# 4. Create a Python program that asks the user to guess the password.
#  The program should keep asking until the user enters "open sesame."
#  For each incorrect guess, print "Wrong password, try again." 
# When the correct password is entered, print "Access granted!"

while True:
    password = input("Enter the password:\n")
    if password.lower() == 'open sesame':
        print("Access granted!")
        break
    else:
        print("Wrong password, try again")
        continue