# Python Sets
print('Example 1')
set = {}
print(set)
print('Example 2')
set = {'apple', 'banana', 'cherry'}
print(set)
print('Example 3')
set = {'Abdu', 'Abdu', 1, 2, 1, 6}
print(set)
print('Example 4')
set = {"apple", "banana", "cherry"}
for x in set:
    print(x)
print('Example 5')
set = {"apple", "banana", "cherry"}
print("apple" in set)
print('Example 6')
set = {"apple", "banana", "cherry"}
set.add('orange')
print(set)
print('Example 7')
set = {"apple", "banana", "cherry"}
set.update(["orange", "mango"])
print(set)