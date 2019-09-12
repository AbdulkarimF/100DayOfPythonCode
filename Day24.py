# Python Dictionaries:
print('Example 1')
dict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
mydict = dict.copy()
print(mydict)
print('Example 2')
thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
#mydict = dict(thisdict)
print(mydict)
print('Example 3')
myfamily = {
    "child1": {
        "Abdu": "Email",
        "Year": 2004
    },
    "child2": {
        "Omar": "Tobies",
        "Year": 2007
    },
    "child3": {
        "Ahmad": "Linus",
        "Year": 2011
    }
}
print(myfamily)
print('Example 4')
child1 = {
        "Abdu": "Email",
        "Year": 2004
 }
child2 = {
        "Omar": "Tobies",
        "Year": 2007
}
child3 = {
        "Ahmad": "Linus",
        "Year": 2011
}
myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily)
print('Example 5')
#thisdictionary = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)