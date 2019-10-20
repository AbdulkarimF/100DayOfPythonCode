# Python JSON:
print("Example 1")
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
# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))
print("\nExample 2")
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
print(json.dumps(x, indent=4, separators=(". ", " = ")))
print("\nExample 3")
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
print(json.dumps(x, indent=4, sort_keys=True))