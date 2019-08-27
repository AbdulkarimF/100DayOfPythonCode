# String Format
print("Example 1")
#  age = 21
#  txt = "My name is Abdulkarim, I am" + age
#  print(txt) #Error, we can't combine strings and numbers by this way
print("Error output, we can't combine strings and numbers without format() function")
print('Example 2')
age = 21
txt = "My name is Abdulkarim, and I am {}"
print(txt.format(age))
print('Example 3')
quantity = 3
itemno = 567
price = 49.95
myorder = 'I want {} pieces of item {} for {} dollars'
print(myorder.format(quantity, itemno, price))
print('Example 4')
quantity = 3
itemno = 567
price = 49.95
myorder = 'I want to pay {2} dollars for {0} pieces of item {1}'
print(myorder.format(quantity, itemno, price))
