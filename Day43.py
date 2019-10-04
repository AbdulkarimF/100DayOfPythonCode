# Python Inheritance:
print('Example 1')
class Person:
    def __init__(self, Fname, Lname):
        self.firstname = Fname
        self.lastname = Lname
    def printname(self):
        print(self.firstname, self.lastname)
x = Person("Abdulkarim", "Faqiha")
x.printname()
print('\nExample 2')
class Person:
    def __init__(self, Fname, Lname):
        self.firstname = Fname
        self.lastname = Lname
    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    pass
x = Student("Mike", "Olsen")
x.printname()
print('\nExample 3')
class Person:
    def __init__(self, Fname, Lname):
        self.firstname = Fname
        self.lastname = Lname
    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self, Fname, Lname):
        Person.__init__(self, Fname, Lname)
x = Student("Mike", "Olsen")
x.printname()
