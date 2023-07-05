# Booleans
# the simplest data type there is 0 or 1, yes or no, on or off
# in Python we try to use is_something for booleans
is_sunny = True # notice capital T
is_raining = False # again capital F
is_summer = True
# since 3.8+ we have a = syntax inside f strings
print(f"{is_sunny=} {is_raining=} {is_summer=}") # will print both name and value

# often we will get Booleans values by comparison
print(2*2==4) # not very useful but still we print Boolean

# usually at least one side of comparison will involve some variable
a = 2
b = 4
is_math_correct = a*a == b # right side will evaluate first
print(f"{is_math_correct=}")

# one trick is to use 4 == b reverse order, usually we would use b == 4

# we also have inequality
print("b != 5", b != 5) # so True
print("b != 4", b != 4) # and False because b == 4

# greater than
c = 10
print(c > b, b > a)
# Python also offers a way to combine multiple comparison
print(c,b,a,c > b > a) # so two comparisons at once
d = 50
print(d,c,b,a,d > 36 > c > b > a) # so four comparisons at once

# we have also less than
print(a < b, b < c)
# so also possible to chain <
print(a,b,c, a < b < c)

# we also have less than and equal lteq
print(a <= b)
print(a <= 2) # also True
# finally we have greater than and equal gteq
print(5 >= b)
print(4 >= b) # also true
print(10 >= c >= 4 >= b >= 2)
# we also have a way to compare by memory address using is
# essentialy id(a) == id(b)
# we use this mostly when comparing compound objects if they are actually the same
print(is_summer is is_sunny) # True because both are True and take up same memory
# also we use it for checking if something is None
mr_nemo = None # special None type
print(mr_nemo is None) # for checking None we use is , not ==

name = "Valdis"
friend = "Voldemars"
print(f"{name} < {friend} ?", name < friend) # will be True, but why?
# here it is lexicographical (by alphabet)
print(ord("a"), ord("o"), ord("ā"))
# by length
print(len(name), len(friend), len(name) < len(friend))