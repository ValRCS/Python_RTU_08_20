## Let's talk about boolean data types

# Boolean data types are either True or False

is_spring = True
is_raining = False
# it is a good practice to use descriptive variable names
# for booleans is_ prefix is used

# we can get boolean types from comparison operators
# >, <, >=, <=, ==, !=
# these operators return True or False

# let's compare some numbers

print("5 > 3", 5 > 3)
print("5 < 3", 5 < 3)
print("5 == 3", 5 == 3) # == is used to check if two values are equal
print("5 != 3", 5 != 3) # != is used to check if two values are not equal
print("5 >= 3", 5 >= 3)
print("5 <= 3", 5 <= 3)

# typically there will be at least one variable in the comparison
# but we can also compare two variables
a = 5
b = 3
print(f"{a} > {b}", a > b)
print(f"{a} < {b}", a < b)
print(f"{a} == {b}", a == b)
print(f"{a} != {b}", a != b)
print(f"{a} >= {b}", a >= b)
print(f"{a} <= {b}", a <= b)

# we can also compare strings
name = "Valdis"
neighbor = "Voldemārs"
print(f"{name} < {neighbor}", name < neighbor)
# why is this True?
# because strings are compared by their unicode values
# and unicode values are compared by their numerical values
# so we can compare strings by their unicode values
# in this case 2nd letter of Voldemārs is unicode 111
# and 2nd letter of Valdis is unicode 97
print(ord("a"), ord("o"), ord("a") < ord("v"))
# link to ascii table https://www.ascii-code.com/

# if we want to compare by length we can use len() function
print(f"Length of {name} {len(name)} < {len(neighbor)} {neighbor}", len(name) < len(neighbor))

# we can also compare memory using is operator
# this is not very useful in our current context
# will be useful when we use complex data structures

## Boolean Logic
# Named after George Boole - wikipedia: https://en.wikipedia.org/wiki/George_Boole

# Boolean logic is used to combine multiple boolean values

# simplest is negation using not
# not True is False
# not False is True
print("not True is", not True) # in Python we use English not instead of !
print("not False is", not False)
# we can create a toggle with not
is_spring = not is_spring # so reverse of itself
print("is_spring is now", is_spring)
is_spring = not is_spring
print("is_spring is now", is_spring)
is_spring = not is_spring
print("is_spring is now", is_spring)
is_spring = not is_spring
print("is_spring is now", is_spring)

# we can have a conjunction using and
# True and True is True
# True and False is False
# False and True is False
# False and False is False
print("True and True is", True and True)
print("True and False is", True and False)
print("False and True is", False and True)
print("False and False is", False and False)
print("is_spring and is_raining", is_spring and is_raining)
# we can have longer chains of and
print("True and True and True is", True and True and True)
# but one False will make the whole thing False
print("True and True and False is", True and True and False)

# Finally we have disjunction using or
# True or True is True
# True or False is True
# False or True is True
# False or False is False
print("True or True is", True or True)
print("True or False is", True or False)
print("False or True is", False or True)
print("False or False is", False or False)
print("is_spring or is_raining", is_spring or is_raining)




