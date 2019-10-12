# Python Datetime:
print("Example 1")
import datetime
x = datetime.datetime.now()
print(x)
print("\nExample 2")
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
print("\nExample 3")
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)
print("\nExample 4")
import datetime
x = datetime.datetime(2019, 10, 13)
print(x.strftime("%B"))
