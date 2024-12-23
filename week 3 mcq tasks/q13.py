
print("Welcome to the Wizarding World")
choice = input("choose a subject: spells or potions: ")
if choice == "spells":
    choice = input("practice magic or compete in duels: ")
    if choice == "practice magic":
        print("You mastered a powerful spell. You Win!")
    elif choice == "compete in duels":
        print("You lost to a rival wizard. Game Over.")
    else:
        print("Invalid choice")
elif choice == "potions":
    choice = input("brew an elixir or create poison: ")
    if choice == "brew an elixir":
        print("You healed a village. You Win!")
    elif choice == "create poison":
        print("Your potion backfired. Game Over.")
    else:
        print("Invalid choice")
else:
    print("Invalid choice")
