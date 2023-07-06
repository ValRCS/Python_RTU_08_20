# Booleans and comparison operators
# simplest data type 0 or 1, true or false
# in Python we use True and False for boolean values
# style wise good practice is to preface
# boolean values with is_something or are_something
is_sunny = False
is_raining = False
is_summer = True
is_warm = True

# since Python 3.8 we have = syntax inside f-strings
# prints variable name AND value - good for debuggin
print(f"{is_sunny=} {is_raining=} {is_summer=}")

# simplest comparison operator would be equality
print(3*3==9)

# usually at least one side of comparision will have a variable
a = 2
b = 4
print(f"{a}*{a} == {b} ??", a*a==b)

# we can save result of our comparison
is_math_correct = a*3 == b+2  # we start from right side and end with assignment
# if you are not sure you could use parenthesis
# operator precedence: https://docs.python.org/3/reference/expressions.html#operator-precedence
print("a*3 == b+2 ?", is_math_correct)

# inequality
print("b != 4", b != 4) # False statement because b == 4 !!!
print("b != 5", b != 5) # True

# greater and greater or equal
print("b > a", b > a)
print("b >= 4?", b >= 4)

# we can chain multiple comparisons
c = 50
d = 1_000 # _ is cosmetic for numbers, just for humans
print("d > c > b > a > 0", d > c > b > a > 0) # we have 4 comparisons
print("d >= 1000 > c > b > a >= 2", d >= 1000 > c > b > a >= 2)

# similarly we have less than and less or equal
print("b < a", b < a) # False
print("b <= 4?", b <= 4)

# i can chain < and <= as well

# less used is is - which compares objects by their memory id
# essentially id(a) == id(b)
# we use it for comparing complex objects
capt_nemo = None # special type significant
print("Is capt_nemo None?", capt_nemo is None)

# string comparison
name = "Valdis"
neighbor = "Voldemars"
print(f"{name} < {neighbor} ?", name < neighbor)
# what is the result and why?
print(ord("a"), ord("o"), ord("ā"))
# so 97 < 111 thus Voldemars wins
neighbor = "Vold"
print(f"{name} < {neighbor} ?", name < neighbor)
# so strings are compared lexicographically
# by length we have len(mystring)
print(len(name), len(neighbor), len(name) > len(neighbor))
