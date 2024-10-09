# we might want to combine multiple booleans with some logical operators
# we need a bit of Boolean Algebra
# https://en.wikipedia.org/wiki/Boolean_algebra
# let's start with negation
is_raining = True
print("is it raining?", is_raining)
# we can reverse it with not operator
is_still_raining = not is_raining # not reverses the True to False
# and False to True
print("is it still raining?", is_still_raining)
# not can be used to create a toggle switch
is_light_on = True
print("Is light on?", is_light_on)
is_light_on = not is_light_on # so we overwrite the old value with new True->False->True->False and so on
print("Is light on?", is_light_on)
is_light_on = not is_light_on
print("Is light on?", is_light_on)
is_light_on = not is_light_on
print("Is light on?", is_light_on)

# then we have logical conjuction that requires that all statements are true to be true
# Python uses and (not && as other languages)
print("True and True ?", True and True) # in place of True there could be variables holding that
print("True and False ?", True and False)
print("False and True ?", False and True)
print("False and False ?", False and False)

# we can do a longer chain
# as soon as one of the statements is False, whole chain is False!
print("True and True and 2*2 == 4 and is_light_on", True and True and 2*2 == 4 and is_light_on)
is_light_on = not is_light_on
print("True and True and 2*2 == 4 and is_light_on", True and True and 2*2 == 4 and is_light_on)

# going back to 2 < 4 < 5
# that is same as 2 < 4 and 4 < 5 just shorter
print("2 < 4 < 5", 2 < 4 < 5)
print("2 < 4 and 4 < 5", 2 < 4 and 4 < 5) # same as previous

# finally we have logical disjunction
# where we need just one statement to be True for whole chain to be True
print("True or True ?", True or True) # in place of True there could be variables holding that
print("True or False ?", True or False)
print("False or True ?", False or True)
print("False or False ?", False or False)



