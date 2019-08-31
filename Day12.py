# Problem
a = 'Please, I want {} sandwishes and {} donuts'
print('#1st Required')
print(a.replace('I', 'We'))
print('#2nd Required')
print(a.replace('I', 'We').format(5, 7))
print('#3rd Required')
print(a.replace('a', 'A').replace('I', 'We').format(5, 7))
