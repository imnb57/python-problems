#  Using a for loop and .append() method append each item with a Dr. prefix to the lst. Hint a=["ram","shyam"] expected output:  ['Dr.ram', 'Dr.shyam','Dr.1','Dr.2']


a = ["ram", "shyam", 1, 2]
new_list = []
for i in a:
    new_list.append("Dr." + str(i))
    continue
print(new_list)