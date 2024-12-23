
print("Welcome to the Haunted Castle")
choice = input("enter the castle or run away: ")
if choice == "enter the castle":
    choice = input("red, green or black: ")
    if choice == "red":
        print("You entered a room full of flames. Game Over.")
    elif choice == "green":
        print("You found the treasure. You Win!")
    elif choice == "black":
        print("You were captured by ghosts. Game Over.")
    else:
        print("Invalid choice")
elif choice == "run away":
    print("You escaped safely.")
else:
    print("Invalid choice")
