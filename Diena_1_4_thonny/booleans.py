is_raining = True
is_sunny = False
is_summer = True
print(is_raining, is_sunny)
print(type(is_raining), type(is_sunny), type(is_summer))
print(2*2 == 4) # notice  double == , this is comparison this is not assignment!

is_math_correct = 2*2 == 4 # we go from right to left

print(is_math_correct)
a = 2
b = 4
print(a*a == b, a*a == 4, a*a == 5) # more common
print(2 == 2.0) # two types but should be true
print(1 == True, True == 1, False == 0, 0 == False) # True is represented by 1
# and False by 0
# there are some other falsy values, meaning values which equal to False when comparing
print("" == False) # empty string is not the same as False but it will be used similarly in logical operations
print("" == '') # same empty string
my_name = "Valdis"
print(my_name == my_name, my_name == "Valdis", my_name == "Voldis")
print("Valdis" == 55)

# inequality
print(a != b) # if they are inequal then != will give True
print(2 != 2) # this is a False statement because 2 is in fact equal to 2
is_not_equal = a*2 != b
print(is_not_equal)

# greater >
print(2 > 3, 3 > 2, 9001 > 9000)
print(a*a > 3, a*a > b, a*a > 5)
print(True > False) # if True is 1 and False is 0 then this should be True :)
# we can compare other data types
print("Voldemars" > "Valdis") # gives us True but why?
#
print("Voldis" > "Valdis") # this is also true
print("Vol" > "Valdis")
print(ord("V"), ord("a"), ord("ā")) # we can get Unicode codes for characters
print(chr(86), chr(97), chr(257)) # i can print from codes the symbols

# less than <
print(2 < 3, 3 < 3, a < b, b < a)

# less or equal
print(2 <= 3, 3 <= 3, 3 <= 4, 5 <= 3)

# gt greater or equal
print(2 >= 3, 3 >= 3, 4 >= 3, a*2 >= b)

c = 5
# we can compare more than two at once
print(a < b < c < 1000) # four values at once
print(a < -50 < b < c < 1000) # false because first operation shortcircuits to False

# is compares actual memory address
# used less
print(a is b) # really it is id(a) == id(b)
# we use it when we need to see if both variables point to same object

print( a + b == c, a + b == c + 1)