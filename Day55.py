#Python JSON:
print("Example 1")
import json
# some JSON:
x = '{"name":"John", "age":30,"city":"NYC"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])
print("\nExample 2")
import json
# a Python object (dict):
x = {
    "name":"john",
    "age":30,
    "city":"NYC"
}
# convert into JSON:
y= json.dumps(x)
# the result is a JSON string:
print(y)
print("\nExample 3")
import json
print(json.dumps({"name":"ali","age":20}))
print(json.dumps(["apple","banana"]))
print(json.dumps(("apple", "banana")))
print(json.dumps("Hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
print("\nExample 4")
import json
x = {
    "name":"ali",
    "age":40,
    "married":True,
    "devorced": False,
    "cheldren": ("Ann", "Billy"),
    "pets":None,
    "cars":[
        {"model":"BMW 230", "mpg": 27.5},
        {"model":"Ford Edge", "mpg":24.1}
    ]
}
# convert into JSON:
y = json.dumps(x)
#the result is a JSON string:
print(y)