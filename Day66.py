#Python String Formatting:
print("Example 1")
price = 49
quantity = 3
itemno = 567
txt = "I want {0} pieces of item number {1} for {2:.2f} dollars"
print(txt.format(quantity, itemno, price))
print("\nExample 2")
age = 50
name = "ali"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
print("\nExample 3")
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford", model = "Mustang"))
