# Take a number as input. Check if it is divisible by 2. If yes, further check if it is 
# divisible by 5. Print appropriate messages for each condition. 

num = int(input("Enter a number: "))
if num % 2 == 0:
    if num % 5 == 0:
        print("Divisible by 2 and 5")
    else:
        print("Divisible by 2 but not by 5")
else:
    print("Not divisible by 2")
    