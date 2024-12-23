
choice = input('do you want veg or non-veg food?:\n')
if choice == 'veg':
    choice = input('do you want salad or pasta?:\n')
    if choice == 'salad':
        print('salad')
    elif choice == 'pasta':
        print('pasta')
    else:
        print('invalid choice')
elif choice == 'non-veg':
    choice = input('do you want chicken or fish?:\n')
    if choice == 'chicken':
        print('chicken')
    elif choice == 'fish':
        print('fish')
    else:
        print('invalid choice')