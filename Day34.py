# Python Functions:
print("Example 1")
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "orange", "banana"]
my_function(fruits)
print("\nExample 2")
def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(2))
print(my_function(10))
print("\nExample 3")
def my_function(child3, child2, child1):
    print("The youngest child is "+child3)
my_function(child1="Emil", child2="Tobias", child3="Linus")
print("\nExample 4")
def my_function(*kids):
    print("The youngest kid is "+kids[1])
my_function("Emil", "Tobias", "Linus")
print("\nExample 5")
def tri_recursion(k):
    if (k>0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result=0
    return result
print("Recursion Example Results")
tri_recursion(6)