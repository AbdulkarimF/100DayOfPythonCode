# Python Tuples
# Check if Item Exists
print('Example 1')
thistuple = ('apple', 'banana', 'cherry')
if 'apple' in thistuple:
    print("yes, 'apple' is in the tuple")
# Repeat Item
print('Example 2')
thistuple = ('python',) *5
print(thistuple)
# + Operator in Tuple
print('Example 3')
tuple1 = (1, 2, 3, 4)
tuple2 = (5, 6)
tuple = tuple1 + tuple2
print(tuple)
print('Example 4')
x = (3, 4, 5, 6)
x = x + (1, 2, 3)
print(x)
# Tuple Length
print('Example 5')
tuple = (1, 'apple', 2.0)
print(len(tuple))
# The tuple() Constructor
print('Example 6')
thistuple = ("apple", "banana", "cherry")
tuplelist = tuple(thistuple)
print(tuplelist)