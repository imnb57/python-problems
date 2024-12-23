
print("Welcome to the Pirate Ship Adventure")
choice = input("search for treasure or battle enemy ships: ")
if choice == "search for treasure":
    choice = input("dig on the island or explore the cave: ")
    if choice == "dig on the island":
        print("You found a hidden treasure chest. You Win!")
    elif choice == "explore the cave":
        print("You were trapped inside. Game Over.")
    else:
        print("Invalid choice")
elif choice == "battle enemy ships":
    choice = input("attack or defend: ")
    if choice == "attack":
        print("You won the battle. You Win!")
    elif choice == "defend":
        print("You were outnumbered. Game Over.")
    else:
        print("Invalid choice")
else:
    print("Invalid choice")
