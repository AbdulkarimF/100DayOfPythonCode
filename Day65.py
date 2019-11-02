#Python String Formatting:
print("Example 1")
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
print("\nExample 2")
price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))
print("\nExample 3")
price = 49
quantity = 3
itemno = 567
txt = "I want {} pieces of item number {} for {:.2f} dollars"
print(txt.format(quantity, itemno, price))

