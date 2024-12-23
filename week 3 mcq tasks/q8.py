
print("Welcome to the Jungle Survival Challenge")
choice = input("search for food or build a shelter: ")
if choice == "search for food":
    choice = input("hunt or gather: ")
    if choice == "hunt":
        print("You were attacked by a wild animal. Game Over.")
    elif choice == "gather":
        print("You found enough food. You Win!")
    else:
        print("Invalid choice")
elif choice == "build a shelter":
    print("Your shelter collapsed in the rain. Game Over.")
else:
    print("Invalid choice")
