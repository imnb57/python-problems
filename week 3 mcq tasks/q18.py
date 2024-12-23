
temperature = int(input("Enter temperature in Celsius: "))
if temperature > 40:
    print("Hot")
elif temperature >= 20 and temperature <= 39:
    print("Warm")
else:
    print("Cold")
