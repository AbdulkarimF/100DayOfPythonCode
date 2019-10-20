print("Example 1")
import re
str = "The rain in Spain"
x = re.sub("\s", "9", str)
print(x)
print("\nExample 2")
import re
str = "The rain in Spain"
x = re.sub("\s", "9", str, 2)
print(x)
print("\nExample 3")
import re
str = "The rain in Spain"
x = re.search("ai", str)
print(x)
print("\nExample 4")
import re
str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.span())
print("\nExample 5")
import re
str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.string)
print("\nExample 6")
import re
str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.group())