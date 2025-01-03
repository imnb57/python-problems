# Write a Python program that simulates a login system. The program 
# should prompt the user to enter a username and password. If both are 
# correct (e.g., username is "admin" and password is "1234"), 
# print "Login successful" and exit. If either is incorrect, 
# print "Invalid credentials, try again." Allow the user up to 
# 3 attempts before locking them out with the message "Too many failed attempts."

username = 'admin'
password = '1234'
attempt = 0
while attempt<3:
    user = input("Enter your username:\n")
    pwd =  input("Enter password:\n")
    if user == username and pwd == password:
        print("Login Successful!")
        break
    elif attempt ==2:
        print('Too many failed attempts')
        break
    else:
        print("Invalid credentials")
        attempt+=1
