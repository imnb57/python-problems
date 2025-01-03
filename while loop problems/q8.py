# 8. Write a Python program that simulates a basic arithmetic quiz. 
# Generate two random numbers between 1 and 30 and ask the user to 
# provide the result of their multiplication. If the answer is correct, 
# print "Correct!" and generate a new question. If the answer is wrong, 
# print "Incorrect, try again." Allow the user to stop the quiz when the 
# user enters "exit"

from random import randint

while True:
    a = randint(1,30)
    b = randint(1,30)
    guess = input("Enter the guess:\n")
    if guess == 'exit':
        print("exiting the game")
        break
    elif int(guess) == a*b:
        print('correct')
    elif guess!= a*b:
        print("Incorrect, try again or type \'exit\' to exit")