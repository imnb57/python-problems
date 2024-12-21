weather = input("Enter the current weather (sunny/rainy): ").strip().lower()

if weather == "sunny":
    print("It's a great day for outdoor activities like hiking or a picnic!")
elif weather == "rainy":
    rain_gear = input("Do you have a raincoat or umbrella? (yes/no): ").strip().lower()
    if rain_gear == "yes":
        print("Consider going to a nearby mall or museum.")
    else:
        print("It's better to stay home and watch a movie.")
else:
    print("Invalid weather input. Please enter 'sunny' or 'rainy'.")
