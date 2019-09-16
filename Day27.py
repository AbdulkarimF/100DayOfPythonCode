# Conditional Statements
print('Example 1')
a = 10
b = 200
if b > a:
    print("b is greater than a")
# print('Example 1.1')
# a = 10
# b = 200
# if b > a:
# print("b is greater than a")
print('Example 2')
a = 10
b = 10
if b > a:
    print("b is greater than a")
elif a==b:
    print("a & b are equal")
print('Example 3')
a = 10
b = 5
if b > a:
    print("b is greater than a")
elif a==b:
    print("a & b are equal")
else:
    print("a is greater than b")
print('Example 4')
a = 10
b = 5
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
print('Example 5')
a = 10
b = 50
if b > a: print("b is greater than a")
print('Example 6')
a = 10
b = 50
print("A") if a > b else print("B")
print("Example 7")
a = 10
b = 10
print("A") if a > b else print("B") if b > a else print("=")
print("Example 8")
a = 100
b = 20
c = 200
if a > b and c > a:
    print("Both conditions are True")
print("Example 9")
a = 100
b = 20
c = 200
if a > b or a > c:
    print("At least one of the conditions is True")
print("Example 10")
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
