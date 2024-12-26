# Given list is lst=[1,2,3,4] but print 1 and 2 only

list = [1, 2, 3, 4]
for i in range(0, len(list)):
    if i == 0 or i == 1:
        print(list[i])
        continue
    else:
        continue
    