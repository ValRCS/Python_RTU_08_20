# Boolean logic
# Thank you George Boole from 19th century
is_sunny = True
print(is_sunny)
negated_sunny = not is_sunny # so called unary - one variable
print(is_sunny, negated_sunny)
# i could use negation for toggle
my_toggle = False
print("my_toggle is", my_toggle)
my_toggle = not my_toggle
print("my_toggle is", my_toggle)
my_toggle = not my_toggle
print("my_toggle is", my_toggle)

# logical conjunction BOTH sides have to be True
# Python uses and (not && as many other languages do)
print(True and True) # True
print(True and False)# False
print(False and True) # False
print(False and False)  # False

# i can create a longer chain
# all have to be True
print(10 > 5 and 3 < 4 and 7 == 7 and 3*3 == 9)
# one drop of oil spoils the honey here 2<0 spoils it
print(10 > 5 and 2 < 0 and 3 < 4 and 7 == 7 and 3*3 == 9)
# Python lets us compare numbers in a row
a = 2
b = 4
print(0 < a < 3 < b < 10)

# Finally we have logical disjunction - logical or
# only one side has to be True
print("Logical or in Python uses or")
print(True or True) # True
print(True or False)# True
print(False or True) # True
print(False or False)  # False

# I can chain multiple or operators
# Just one True is enought to turn everything True
print(2 < 0 or 100 < 99 or 300 < 299)
print(2 < 0 or 100 < 99 or 300 < 299 or 10 > 5)

# Technical detail:
# As soon as Python determines the chain to be True, False
# it stops calculating rest of terms

# without parenthesis
# precedence ir not and or
# https://docs.python.org/3/reference/expressions.html
# could use parenthesis if you are not sure
print((True or not True) and (False or not False))
