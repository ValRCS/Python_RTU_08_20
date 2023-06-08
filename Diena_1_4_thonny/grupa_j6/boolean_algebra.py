# We also need to learn a tiny bit of Boolean Algebra
# Again thank you George Boole!
# we can have negation
print(not True) # False
print(not False) # True
# This leads to toggle trick - button that changes state
my_toggle = False
print("Toggle is on? ", my_toggle)
my_toggle = not my_toggle # so I reverse whatever was there
print("Toggle is on? ", my_toggle)
my_toggle = not my_toggle # so I reverse whatever was there
print("Toggle is on? ", my_toggle)
my_toggle = not my_toggle # so I reverse whatever was there
print("Toggle is on? ", my_toggle)

# we have logical conjunction
# in Python we use English and (not && as in many languages)
print(True and True) # only this is True
print(True and False)
print(False and True)
print(False and False)

# conjunction is lazy means first False stops the whole evaluation
a = 0
print(True and a < 10 and a != 0 and 50/a > 100) # so last part will not run
# because 3rd part was False
# one drop of oil ruins the honey jar...

print("Logical disjunction ", "*"*30)
# we also have logical disjunction using or (not || as other languages)
# as long as one expression is True everything is True
print(True or True) # True
print(True or False)
print(False or True)
print(False or False) # only this is False

# means

# we also have bit logical operations # those a little bit later
