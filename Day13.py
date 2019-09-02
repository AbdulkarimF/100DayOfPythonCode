# Python Lists
# create a List
print('Example 1')
s = []
print(s)
print('Example 2')
Numbers = [1, 2, 3, 4, 5]
print(Numbers)
print('Example 3')
thislist = ['apple', 'banana', 'cherry']
print(thislist)
print('Example 4')
thislist = ['apple', 'banana', 'cherry', 1, 2, 3]
print(thislist)
# Access Items
print('Example 5')
thislist = ['apple', 'banana', 'cherry']
print(thislist[-1])
# Loop Through a List
print('Example 6')
thislist = [1, 2, 2.0]
for x in thislist:
    print(x)
# Change Item Value
print('Example 7')
thislist = ['apple', 'banana', 'cherry']
thislist[2]= 'orange'
print(thislist)
print('Example 8')
thislist = ['apple', 'banana', 'cherry']
del thislist[-1]
print(thislist)
print('Example 9')
thislist = ['apple', 'orange', 'cherry']
print('Error because there is not a list')
# del this list