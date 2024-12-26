# Given list is list=[1,2,3,4] but print 1 and 4 only 

list = [1,2,3,4]
for i in range(0,len(list)):
    if i == 0:
        print(list[i])
        continue
    elif i ==3:
        print(list[i])
  