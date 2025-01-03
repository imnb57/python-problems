# Write a Python program that asks the user to guess a pre-defined secret
#  word (e.g., "python"). Provide feedback like "Incorrect, try again" if the 
# guess is wrong. When the user guesses correctly, print "Congratulations, you
#  guessed the word!" Allow the user to exit the program by typing "quit."

secret_word = "python"

while True:
    guess = input("Guess the secret word (or type 'quit' to exit): ")
    
    if guess == "quit":
        print("You chose to exit the game. Goodbye!")
        break
    elif guess == secret_word:
        print("Congratulations, you guessed the word!")
        break
    else:
        print("Incorrect, try again.")
