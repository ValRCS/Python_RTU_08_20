# Boolean algebra

# logical conjuction AND some other languages use && but not Python
print("Testing AND")
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# logical disjunction OR some other languages use || but not Python
print("Testing OR")
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print("Chaining logic")
# we can join our logic
print(True and True and True and 2*2 == 4)
# one bad apple ruins our cider, darvas piliens medū
print(True and 2*2 > 5 and True and True and True and 2*2 == 4)

print(True or True or True or False) # we only need one True with or
print(2*2 == 10 or 2*2 == 5 or 2*2 == 4 or 2*2 == 3)  # as soon as one True is reached we get True back

# True = 2*2 == 5 # cant do True is reserved keyword

# we also have negation with not
print(not True) # False
print(not False) # True
# a little trick in programming
my_toggle = True
print(my_toggle)
my_toggle = not my_toggle # so my_toggle is reverse of whatever was there before
print(my_toggle)
my_toggle = not my_toggle
print(my_toggle)
my_toggle = not my_toggle
print(my_toggle)
