
print("Welcome to the Forest Adventure")
path = input("Choose a path: left or right: ")
if path == "left":
    choice = input("Pick between explore or rest: ")
    if choice == "explore":
        print("You found treasure!")
    elif choice == "rest":
        print("You were attacked by wild animals. Game Over.")
    else:
        print("Invalid choice")
elif path == "right":
    print("You fell into a trap. Game Over.")
else:
    print("Invalid choice")
