# You have two lists of numbers, and you need to find out which numbers appear in both lists.

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_numbers = []

for num in list1:
    if num in list2:
        common_numbers.append(num)
    else:
        pass

print(common_numbers)
