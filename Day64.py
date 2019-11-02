#Python Try-Except:
print("Example 1")
try:
    print(x)
except:
    print("An exception occurred")
print("\nExample 2")
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
print("\nExample 3")
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
print("\nExample 4")
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")
