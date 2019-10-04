# Python Classes and Objects:
print('Example 1')
class Person:
    def __init__(self, name, age):
        self.name= name
        self.age= age
    def myfunc(self):
        print("Hello my name is "+self.name)
p1= Person("Abdulkarim", 36)
p1.myfunc()
print('\nExample 2')
class Person:
    def __init__(self, name, age):
        self.name= name
        self.age= age
    def myfunc(self):
        print("Hello my name is "+self.name)
p1= Person("Abdulkarim", 36)
p1.age = 40
print(p1.age)
# print('\nExample 3')
class Person:
    def __init__(self, name, age):
        self.name= name
        self.age= age
    def myfunc(self):
        print("Hello my name is "+self.name)
p1= Person("Abdulkarim", 36)
del p1.age
# print(p1.age)
# print('\nExample 4')
class Person:
    def __init__(self, name, age):
        self.name= name
        self.age= age
    def myfunc(self):
        print("Hello my name is "+self.name)
p1= Person("Abdulkarim", 36)
del p1
# print(p1)
