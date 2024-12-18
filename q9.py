age1 = int(input("Enter the age of person 1: \n"))
age2 = int(input("Enter the age of person 2: \n"))
age3 = int(input("Enter the age of person 3: \n"))
age4 = int(input("Enter the age of person 4: \n"))

oldest = age1

if age2 > oldest:
    oldest = age2
if age3 > oldest:
    oldest = age3
if age4 > oldest:
    oldest = age4

print("The oldest age is:", oldest)

"""
    #Again
    
    age1 = int(input("Enter the age of person 1: \n"))
    age2 = int(input("Enter the age of person 2: \n"))
    age3 = int(input("Enter the age of person 3: \n"))
    age4 = int(input("Enter the age of person 4: \n"))

    agelist = [age1,age2,age3,age4]
    agelist.sort(reverse = True)
    print(agelist[0])

"""