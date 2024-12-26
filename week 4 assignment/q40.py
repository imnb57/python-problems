# program to check given number is palindrome or not

num = 121
temp = num
rev = 0
while num > 0:
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
if temp == rev:
    print("The number is palindrome!")
else:
    print("The number isn't palindrome!")
    