# Write a Python program that simulates waiting for a 
# specific vehicle, such as a "bus". The program should 
# repeatedly prompt the user to input the name of a vehicle. 
# If the input is not "bus", the program should print 
# "waiting" and continue. Once the user inputs "bus", the 
# program should print "finally the wait is over" and terminate the loop.

while True:
    vehicle = input("Enter the name of vehicle:\n")
    if vehicle.lower() == 'bus':
        print("finally the wait is over")
        break
    else:
        print("waiting")
        continue