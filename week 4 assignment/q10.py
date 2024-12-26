#  Given list is lst=[1,2,3,4] but print 1 2 and 4 only 

list = [1, 2, 3, 4]
for i in range(0, len(list)):
    if i == 0 or i == 1 or i == 3:
        print(list[i])
        continue
    else:
        continue