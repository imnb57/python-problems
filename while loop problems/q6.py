# 6. Write a Python program that generates a random number 
# between 1 and 10 and prompts the user to guess the number. 
# The program should provide hints such as "guess higher" or 
# "guess lower" based on the user's input. Once the user guesses
# the correct number, the program should display the number of 
# attempts it took to guess the correct number.

from random import randint
a = randint(1,10)
attempt = 1
while True:
    guess = int(input('guess the number:\n'))
    if guess<a:
        print('guess higher')
        attempt+=1
    elif guess > a:
        print('guess lower')
        attempt+=1
    elif guess == a:
        print("It took you ",attempt,"attempt's.")
        break