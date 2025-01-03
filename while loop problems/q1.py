# 1. Create a Python program that prompts the user to enter their age. 
# If the age is less than 18, print "You are a minor." If the age is 
# between 18 and 60, print "You are an adult." For ages over 60, print 
# "You are a senior citizen." The program should continue until the user 
# inputs "stop."


while True:
    
    input = input("Enter your age (or type 'stop' to quit): ")
    if input.lower() == 'stop':
        print("Program stopped. Goodbye!")
        break
    if input.isdigit():
        age = int(input)
        if age < 18:
            print("You are a minor.")
        elif age <= 60:
            print("You are an adult.")
        else:
            print("You are a senior citizen.")
    else:
        print("Invalid input. Please enter a valid age or type 'stop'.")
