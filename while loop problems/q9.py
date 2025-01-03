# 9. Write a Python program that prompts the user to enter a number. 
# The program should determine whether the number is prime or not. 
# If the number is prime, print "The number is prime." Otherwise, print
#  "The number is not prime." Continue prompting the user until they enter "exit."

while True:
   num = input("Enter a number:\n")
   
   if num == 'exit':
       print('Exiting')
       break
   
   num = int(num)
   if num < 2:
       print("Number is not prime")
       continue
       
   is_prime = True
   for i in range(2, int(num ** 0.5) + 1):
       if num % i == 0:
           is_prime = False
           break
           
   if is_prime:
       print("The number is prime")
   else:
       print("The number is not prime")