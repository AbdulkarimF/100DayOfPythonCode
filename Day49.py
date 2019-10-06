# Python Scope:
print("Example 1")
x = 300
def myfunc():
    x = 200
    print(x)
myfunc()
print(x)
print("\nExample 2")
def myfunc():
    global y
    y = 300
myfunc()
print(y)
print("\nExample 3")
z = 300
def myfunc():
    global z
    z = 20
myfunc()
print(z)
