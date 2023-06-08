# Booleans are the most basic data type
# only 1 or 0 , off or on, True or False
# so for Booleans we use Capitalized True and False
is_hot = True
is_cold = False
is_summer = True
print(is_hot, is_cold, is_summer)
print(f"Is it summer? {is_summer}")
print(f"{is_summer} is of data type {type(is_summer)}")

# we can get booleans using comparison operators
print(2*2 == 4) # == is comparison NOT assignment!
# usually at least one item will be variable
a = 2
# b = 3
# we do nothing but we could do something
b = 4 # we might as well comment out b = 3 since it is not used
is_math_good = a*a == b # so evaluation happens from right side
# so we multiply first
# compare afterwards
# finally assign
print(is_math_good)
# notice I am using is_ before booleans it is just good style practice
# Python does not enforce this style

# we also have inequality which sometimes gives trouble
print(2 != 2) # False since they ARE equal
is_not_equal = a*2 != b
print(is_not_equal) # this will False if
print( a != 5) # True because a is 2!

# we have greater than
print(a > b)
print(b > a)
# Python has a nice feature to compare multiple values at once
c = 50
d = 100
print(f"{d} > {c} > {b} > {a}", d > c > b > a) # so 3 comparisions here

# we also have greater or equal >=
print(b >= b) # True
print(f"{d} >= {c} >= {b} >= {a} >= {a}", d >= c >= b >= a >= a)
# i can also assign result of long comparision to boolean
is_dbca_correct = d > c > b > a # again eval from right side first
print(is_dbca_correct)

# of course we can also do less than
print("a<b",a < b)
# and also less or equal
print("a <= b <= b", a <= b <= b)

# we can also compare strings but how?
name = "Valdis"
friend = "Voldemārs"
print(name < friend) # why is this True?
print("Valdis" < "Vol") # lexicographicals comparison
print(ord("a"), ord("o")) # tiebreaks!
# keep in min Latvian letters are higher than English
print(ord("k"), ord("Ķ"), ord("ķ")) # unicode codes

# how do we compare by length?
# we use len function
print(len(name), len(friend), len(name) < len(friend))