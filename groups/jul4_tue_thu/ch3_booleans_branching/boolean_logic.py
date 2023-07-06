# Boolean Logic after George Boole in 19th century
# only math that is needed in programming
# https://en.wikipedia.org/wiki/Boolean_algebra
# negation
# we use English not (not !)
print(not True)
print(not False)
# we can use negation for toggle
is_sunny = False
print("Is it sunny?", is_sunny)
is_sunny = not is_sunny # so we reverse whatever boolean was there
print("Is it sunny?", is_sunny)
is_sunny = not is_sunny # so we reverse whatever boolean was there
print("Is it sunny?", is_sunny)
is_sunny = not is_sunny # so we reverse whatever boolean was there
print("Is it sunny?", is_sunny)

# logical conjuction
# in Python we use English and (not && !!)
print(True and True) # both sides have to be True
print(True and False)
print(False and True)
print(False and False)

# finally we have logical disjunction
# again we use English or (not || as in many other languages)
print(True or True) # ONLY one side has to be True to be True
print(True or False)
print(False or True) # ONLY one side has to be True to be True
print(False or False)

# now let's talk  a little about so called short-circuit evaluation
# also lazy evaluation

# so Python interpreter stops logic evaluation as soon as it knows the answer
# we can chain but need to keep this in mind
a = 2
b = 4
div = 0
print(a == 2 and b > 3 and True and div == 0)
# so as soon as one element in long and chain is False
# Python stops because it knows whole thing is false
print(a == 2 and b > 3 and True and div != 0 and 10/div == 9999)

# vice versa for or as soon as one element is True Python stops
# because whole thing is going to be True
print(a == 200 or b == 3 or False or div == 0 or 10/div == 9999)
# we can combine or and and
print((True or False) and (False or True))

