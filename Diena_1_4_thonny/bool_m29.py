print(type(True))
print(type(False))
# Booleans we typically start with is_
is_snowing = True
is_sunny = True
is_raining = False

print(2*2 == 4)  # notice == that is equality operator not =
print(2+2 == 5)

is_math_sound = 3*3 == 9  # evaluation happens from right side
print(is_math_sound)
print(2.0 == 2)
print(1 == True)
print(0 == False)
print(5 == True) # finally False statement

# inequality
print(2*2 != 4)  # False because that is a True statement
a = 2
b = 4
c = 5
print(a, b, a*a == b)
print(a*a != b) # False
print(a*a != c) # True because the sides are NOT equal

print(a > b, c > b)
print(a > a)  # False

print(a < b, b < c, c < a)
print(a*10 < b*50)

print(a >= a) # True
print(a*a >= b, a*a >= c) # True and False

print(b <= b) # again True
print(a*a <= b, a*a <= c) # True and True

print(id(a), id(b)) # shows virtual memory at which variable points
print(a is 2) # True but we do not use is for simple comparision

# we use is for more complex types checking memory (by id)
print(type(a) is int) # this is one use of is
print(type(a) == int)

print(type("Valdis") is str)

name = "Valdis"
friend = "Voldemars"
print(name < friend) # True but why? Two hypothesis
print("Valdis" < "Voldis")
print("Valdis" < "Vol") # so we have tiebreaks
print(ord("a"), ord("o"))
print(ord("ā"), ord("ķ"))

# if we want length comparison
print(len("Valdis") < len("Voldemars"))