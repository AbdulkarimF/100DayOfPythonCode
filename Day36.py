# Python Lambda:
print("Example 1")
def myfunc(n):
    return lambda a : a*n
mydoubler = myfunc(2)
print(mydoubler(10))
print("\nExample 2")
def myfunc(n):
    return lambda a : a*n
mytripler = myfunc(3)
print(mytripler(10))
print("\nExample 3")
def myfunc(n):
    return lambda a : a*n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(10))
print(mytripler(10))
