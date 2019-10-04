# Python Inheritance:
print('Example 1')
class Person:
    def __init__(self, Fname, Lname):
        self.firstname = Fname
        self.lastname = Lname
    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self, Fname, Lname):
        super().__init__(Fname, Lname)
x = Student("Abdulkarim", "Faqiha")
x.printname()
print('\nExample 2')
class Person:
    def __init__(self, Fname, Lname):
        self.firstname = Fname
        self.lastname = Lname
    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self, Fname, Lname):
        super().__init__(Fname, Lname)
        self.graduationyear = 2021
x = Student("Abdulkarim", "Faqiha")
print(x.graduationyear)
print('\nExample 3')
class Person:
    def __init__(self, Fname, Lname):
        self.firstname = Fname
        self.lastname = Lname
    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self, Fname, Lname, year):
        super().__init__(Fname, Lname)
        self.graduationyear = year
x = Student("Abdulkarim", "Faqiha", 2021)
print(x.graduationyear)
print('\nExample 4')
class Person:
    def __init__(self, Fname, Lname):
        self.firstname = Fname
        self.lastname = Lname
    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self, Fname, Lname, year):
        super().__init__(Fname, Lname)
        self.graduationyear = year
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x = Student("Abdulkarim", "Faqiha", 2019)
x.welcome()
