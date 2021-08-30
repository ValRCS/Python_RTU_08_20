is_raining = True # typically booleans are written with is_
is_sunny = False
print(is_raining, is_sunny)

print(2*2 == 4) # == salidzināšanas operātors, nevis piešķiršanas =
print(2*2 == 5)

a = 2
b = 3
c = 4
print(a*a == b, a*a == c)

is_math_good = a*a == c # evaluation happens from the right side
print(is_math_good)
print(type(is_math_good))
print(is_math_good == is_raining)

# rarer is is which compares actual memory that the variables point to
print(is_math_good is is_raining)
# same as
print(id(is_math_good) == id(is_raining))
# is can be useful when comparing more complex objects
# to check for copy or same object

# often we want to use inequality
print(a*a != b) # this will be true since 4 does not equal 3
print(a*a != c) # since 2*2 is in fact equal, the statement is false

print(a > b, b > a)
# python lets us compare multiple values in a chain
print(c > b > a) # True since 4 > 3 > 2
print(4 > 3 > 2)

print(c > b > 3) # this should be false since b is 3 and notlarger than 3
print(4 > 3 > 3)

# we can compare data other than numbers
print("Voldemars" > "Valdis")
print("Voldis" > "Valdis")
print("Vol" > "Valdis")
# string comparison is by Unicode symbols for each letter starting on the left
# we can print 
print(ord("V"), ord("a"), ord("o"))
print(ord("k"), ord("ķ")) # latvian letters will be after 256
print(chr(107), chr(311))# we can go back to letters from Unicode numbers
print(f"ka{chr(311)}is", "kaķis")

# less than 
print(a < b)
print(a < b < c)
print(c < a) # this should be false

# less or equal
print(a <= b)
print(a <= a) # also true
print(2 <= 2 <= 5 <= 7)

# greater or equal
print(a >= b) # should be false since 2 is not greater or equal to 3
print(c >= b)
print(c >= b >= a >= 2 >= -55 >= -3432)
are_my_numbers_ordered = a <= b <= c
print(are_my_numbers_ordered)