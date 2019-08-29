# Python operators
# Python Logical Operators
print('Example 1 (Python Logical Operators)')
x = 5
print(x > 3 or x < 4)
# Python Identity Operators
print('Example 2 (Python Identity Operators)')
x = ['apple', 'banana']
y = ['apple', 'banana']
z = x
print(x is not z)   # False, because z = x
print(x is not y)   # True, because x not y
print(x != y)       # False, because this operator compare the value of y and x
# Python Membership Operators
print('Example 3 (Python Membership Operators)')
x = ['apple', 'banana']
print('banana' in x) # True, because "banana" is in the list of x
# Python Bitwise Operators