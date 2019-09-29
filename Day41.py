# Python Classes and Objects:
print('Example 1')
class Myclass:
    x=5
print(Myclass)
print('\nExample 2')
class Myclass:
    x=5
p1= Myclass()
print(p1.x)
print('\nExample 3')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1=Person("John", 36)
p2=Person("Mark", 40)
print(p1.name)
print(p2.age)
print('\nExample 4')
class Person:
    def __init__(itself, name, age):
        itself.name = name
        itself.age = age
    def function(abc):
        print("Hello my name is "+abc.name)
p1=Person("John", 36)
p1.function()
