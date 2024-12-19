age1 = int(input("Enter the age of person 1: \n"))
age2 = int(input("Enter the age of person 2: \n"))
age3 = int(input("Enter the age of person 3: \n"))
age4 = int(input("Enter the age of person 4: \n"))

youngest = age1

if age2 < youngest:
    youngest = age2
if age3 < youngest:
    youngest = age3
if age4 < youngest:
    youngest = age4

print("The youngest age is:", youngest)

"""
    #Alternatively

    age1 = int(input("Enter the age of person 1: \n"))
    age2 = int(input("Enter the age of person 2: \n"))
    age3 = int(input("Enter the age of person 3: \n"))
    age4 = int(input("Enter the age of person 4: \n"))

    agelist = [age1,age2,age3,age4]
    agelist.sort()
    print(agelist[0])

"""