# Boolean Algebra kas ir pamatā visiem datoriem (un elektronikai)
is_sunny = True
print(is_sunny)
is_sunny = not is_sunny # we reverse the logic
print(is_sunny)
is_sunny = not is_sunny # we reverse the logic
print(is_sunny)
is_sunny = not is_sunny # we reverse the logic
print(is_sunny)
print(not True, not False) # negation

# logical conjuction and in Python we use and (not &&)
print(True and True) # only True here
print(True and False)
print(False and True)
print(False and False)

print(2*2 == 4 and is_sunny and 5 > 1)
# above is False since in a chain one False statement will ruin everything
is_sunny = not is_sunny # we reverse the logic
print(2*2 == 4 and is_sunny and 5 > 1)

# logical disjuntion with or (Python uses actual or not ||)
print(True or True)
print(True or False)
print(False or True)
print(False or False) # only one which is False

print(False or False or True or False) # still True