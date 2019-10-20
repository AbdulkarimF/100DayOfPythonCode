print("Problem 1")
import json
tuple = ("Sun", "Mon", "Tues", "Wed", "Thrus", "Fri", "Stur")
print(json.dumps(tuple))
print("\nProblem 2")
import re
str = "Data is the new oil"
x = re.search(r"\bD\w+", str)
print(x.span())
print(x.group())