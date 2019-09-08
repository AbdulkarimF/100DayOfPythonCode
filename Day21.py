# Python Sets
print('Example 1')
set = {'python', 'java', 'c++'}
print(len(set))
print('Example 2')
set = {'python', 'java', 'c++'}
set.remove('c++')
print(set)
print('Example 3')
set = {'python', 'java', 'c++'}
set.discard('c++')
print(set)
print('Example 4')
set = {"python", "java", "c++"}
x = set.pop()
print(x)
print(set)
print('Example 5')
set = {'python', 'java', 'c++'}
set.clear()
print(set)
print('Example 6: to delete a set we write (del set)')
set = {'python', 'java', 'c++'}
del set
# print(set)
print('Example 7')
set = set(("python", "java", "c++"))
print(set)
