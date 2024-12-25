# 9. Write a program that prompts the user to input an integer and then outputs the number 
# with the digits reversed. For example, if the input is 12345, the output should be 54321.

num = int(input("Enter a number:\n"))
rev = 0
while num>0:
    rem = num%10
    rev = rev*10 + rem
    num = num//10
print(rev)


