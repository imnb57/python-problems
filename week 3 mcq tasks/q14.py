
print("Welcome to the Cybersecurity Mission")
choice = input("trace the hacker or secure the system: ")
if choice == "trace the hacker":
    choice = input("track their IP or decode their message: ")
    if choice == "track their IP":
        print("You caught the hacker. You Win!")
    elif choice == "decode their message":
        print("The message was a trap. Game Over.")
    else:
        print("Invalid choice")
elif choice == "secure the system":
    choice = input("shut down the server or upgrade the firewall: ")
    if choice == "shut down the server":
        print("The attack was stopped. You Win!")
    elif choice == "upgrade the firewall":
        print("The hacker bypassed it. Game Over.")
    else:
        print("Invalid choice")
else:
    print("Invalid choice")
