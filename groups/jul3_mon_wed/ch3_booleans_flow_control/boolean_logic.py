# Boolean logic
# negation
print(not True) # we use english not
print(not False)
# we also can use not for toggle
is_sunny = False
print("is sunny?", is_sunny)
is_sunny = not is_sunny # we reverse and reassign to same variable
print("is sunny?", is_sunny)
is_sunny = not is_sunny # we reverse and reassign to same variable
print("is sunny?", is_sunny)

# logican conjunction
# again we use English and not && !!
print(True and True) # only True when both sides are True
print(True and False)
print(False and True)
print(False and False)

a = 5
b = 20
div = 0
print("a == 5 and b == 20 ?", a == 5 and b == 20)
# Python is lazily evaluated for logic
# div != 0 will be False and will stop evaluation
print(True and a == 5 and b==20 and div != 0 and b / div == 9999)
# if everything else were True we would get ZeroDivisionError
# print(True and a == 5 and b==20 and div == 0 and b / div == 9999)

# logical disjunction
# we use English or - not || !!
# so only one side has to be True for rest of it to be True
print(True or True)
print(True or False)
print(False or True)
print(False or False) # this is False rest are True
# with or lazy principle also works, as soon as anything is True
# evaluation stops!
print(False or a == 100 or div == 0 or b / div == 10_000)
# in above example we short circuit evaluation and div == 0 is True
# so b / div never got to evaluate




