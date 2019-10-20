print("Example 1")
import re
str = "The rain in Spain"
x= re.findall("ai", str)
print(x)
print("\nExample 2")
import re
str = "The rain in Spain"
x = re.findall("KSA", str)
print(x)
if x:
    print("Yes, there is at least on match!")
else:
    print("No match")
print("\nExample 3")
import re
str = "The rain in Spain"
x = re.search("\s", str)
print("The first white-space character is located in position:", x.start())
print("\nExample 4")
import re
str = "The rain in Spain"
x = re.search("KSA", str)
print(x)
print("\nExample 5")
import re
str = "The rain in Spain"
x = re.split("\s", str)
print(x)
