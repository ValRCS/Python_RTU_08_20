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



