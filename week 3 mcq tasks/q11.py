
print("Welcome to the Underwater World")
choice = input("dive deeper or surface: ")
if choice == "dive deeper":
    choice = input("search for pearls or chase the fish: ")
    if choice == "search for pearls":
        print("You found a rare pearl. You Win!")
    elif choice == "chase the fish":
        print("You got lost underwater. Game Over.")
    else:
        print("Invalid choice")
elif choice == "surface":
    print("You returned safely.")
else:
    print("Invalid choice")
