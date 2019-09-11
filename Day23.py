# Python Dictionaries
print('Example 1')
dict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
if "Model" in dict:
    print("Yes, 'Model is a key in dict")
print('Example 2')
dict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
print(len(dict))
print('Example 3')
dict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
dict["color"] = "Blue"
print(dict)
print('Example 4')
dict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
dict.pop("Model")
print(dict)
print('Example 5')
dict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
dict.popitem()
print(dict)
print('Example 6')
dict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
del dict["Model"]
print(dict)
print('Example 7')
dict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
dict.clear()
print(dict)
