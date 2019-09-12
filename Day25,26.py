# Problem
print("Problem 1")
set = {1, 3, 5, 7, 8}
print(set)
print("1st")
set.update([4, 8, 12])
print(set)
print('2nd')
set.remove(8)
print(set)
print("3rd")
set.clear()
print(set)
print()
print('Problem 2')
dictionary = {
    "Name": "pigeon",
    "Type": "bird",
    "Skin cover": "feathers"
}
print(dictionary)
print("1st")
x = dictionary.get("Type")
print(x)
print("2nd")
dictionary["Skin cover"] = "leather"
print(dictionary)