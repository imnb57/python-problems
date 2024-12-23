 
print("Welcome to the Space Adventure")
choice = input("land on Mars or fly to Jupiter: ")
if choice == "land on Mars":
    choice = input("explore or build a base: ")
    if choice == "explore":
        print("You found alien artifacts. You Win!")
    elif choice == "build a base":
        print("You ran out of resources. Game Over.")
    else:
        print("Invalid choice")
elif choice == "fly to Jupiter":
    print("Your spaceship crashed. Game Over.")
else:
    print("Invalid choice")
