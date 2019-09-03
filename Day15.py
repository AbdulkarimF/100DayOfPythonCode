# Python Lists
# List Length
print('Example 1')
thislist = ['apple', 'banana', 'cherry']
print(len(thislist))
# Add Items
print('Example 2')
thislist = ['apple', 'banana', 'cherry']
thislist.append('orange')
print(thislist)
print('Example 3')
thislist = ['apple', 'banana', 'cherry']
thislist.insert(1, 'orange')
print(thislist)
# Remove Item
print('Example 4')
thislist = ['apple', 'banana', 'cherry']
thislist.remove('cherry')
print(thislist)
print('Example 5')
thislist = ['apple', 'banana', 'cherry']
thislist.pop(1)
print(thislist)
print('Example 6')
thislist = ['apple', 'banana', 'cherry']
thislist.clear()
print(thislist)
# Copy a List
print('Example 7')
thislist = ['apple', 'banana', 'cherry']
mylist = thislist.copy()
print(mylist)
print('Example 8')
thislist = ['apple', 'banana', 'cherry']
mylist = thislist.copy()
thislist.pop(0)
print(mylist)
print(thislist)
print('Example 9')
thislist = ['apple', 'banana', 'cherry']
mylist = thislist
thislist.pop(0)
print(mylist)
print(thislist)
print('Example 10')
thislist = ['apple', 'banana', 'cherry']
mylist = list(thislist)
print(mylist)
# The list() Constructor
print('Example 11')
thislist = list(('apple', 'banana', 'cherry'))
print(thislist)
