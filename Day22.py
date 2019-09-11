# Python Dictionaries
print('Example 1')
dict = {}
print(dict)
print('Example 2')
dict = {
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
print(dict)
print('Example 3')
dict = {
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
x = dict["year"]
print(x)
print('Example 4')
dict = {
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
x = dict.get("model")
print(x)
print('Example 5')
dict = {
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
dict["year"] = 2019
print(dict)
print('Example 6')
dict = {
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
for x in dict:
    print(x)
print('Example 7')
dict = {
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
for x in dict:
    print(dict[x])
print('Example 8')
dict = {
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
for x, y in dict.items():
    print(x ,y)
print('Example 9')
dict = {
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
print(dict.items())