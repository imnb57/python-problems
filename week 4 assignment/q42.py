#  Write a for loop that removes all vowels (a, e, i, o, u) from a string.

a = 'string'
vowels = ['a', 'e', 'i', 'o', 'u']
for i in a:
    if i in vowels:
        a = a.replace(i, '')
        continue
    else:
        continue
print(a)
