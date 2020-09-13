# Python Class attributes
# https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide#so-when-would-you-use-them
# class attributes - static values in other OOP languages
# https://en.wikipedia.org/wiki/Indiana_Pi_Bill

class Circle:
    PI = 3.14159


# we can use class attributes before making any objects from the class
print(Circle.PI)
indiana = Circle()
newyork = Circle()
# this will be attribute for newyork object
print(indiana.PI)
print(newyork.PI)
indiana.PI = 3.2  # !!!
print(Circle.PI)
print(indiana.PI)
print(newyork.PI)
newyork.PI = 3.1416
print(Circle.PI)
print(indiana.PI)
print(newyork.PI)
Circle.PI = 3.1415926
print(Circle.PI)
print(indiana.PI)
print(newyork.PI)
riga = Circle()
print(Circle.PI)
print(indiana.PI)
print(newyork.PI)
print(riga.PI)
