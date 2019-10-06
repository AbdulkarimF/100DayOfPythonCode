# Python Scope:
print("Example 1")
def myfunc():
    x = 300
    print(x)
myfunc()
print("\nExample 2")
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()
print("\nExample 3")
x = 300
def myfunc():
    print(x)
myfunc()
print(x)
