# Boolean Logic
# How to combine different Truth values
# We need to learn three operations
is_raining = False
is_summer = True
is_sunny = True

# we have logical conjunction
# Python uses english and , (not && as many other languages)
print(is_raining and is_summer) # False

print(True and True) # only one which is True
print(True and False) # False
print(False and True) # False
print(False and False) # False

print(2*2 == 4 and 3*3 == 9 and 4*4 == 16)
# one little false statement breaks whole chain for and
print(2*2 == 4 and 5*5 == 30 and 3*3 == 9 and 4*4 == 16)
# also Python uses lazy evaluation
# this means that nothing after False will be evaluated

# then we have logical disjunction
# again Python uses or (not || as many other languages)
# we need only one of the statements to eval to True
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # only one False

# with or we can chain multiple ors
# first True will stop evaluation
print(2*2 == 9 or 5*5 == 25 or 10/0 == 100) # 10/0 == 100 will not run
# because 5*5 = 25 so no need to proceed
# print(10/0) # Arithmetic Error ZeroDivisionError: division by zero


# finally we have negation
# reverse the boolean
print(not True)
print(not False)

# we can create a toggle_switch
my_toggle = False
print("my button", my_toggle)
my_toggle = not my_toggle # we reverse whatever we had
print("my button", my_toggle)
my_toggle = not my_toggle # we reverse whatever we had
print("my button", my_toggle)
my_toggle = not my_toggle # we reverse whatever we had