# Python Modules:
print("Example 1")
import mymodule as mx
a = mx.person1["age"]
print(a)
print("\nExample 2")
import platform
x = platform.system()
print(x)
print("\nExample 3")
import platform
print(platform.python_version())
print("\nExample 4")
import platform
x = dir(platform)
print(x)
print("\nExample 5")
from mymodule import person1
print(person1["name"])
