# Problem:
print("Problem 1")
import Module
Module.sum()
Module.sub()
Module.mul()
Module.div()
print("\nProblem 2")
import datetime
x = datetime.datetime.now()
print(x.year)
print(x)
print(x.strftime("%B"))
print(x.strftime("%A"))
print("\nProblem 3")
import datetime
Yesterday = datetime.date(2019, 10, 12)
Tomorrow = datetime.date(2019, 10, 14)
print("Yesterday: ", Yesterday)
print("Tomorow: ", Tomorrow)