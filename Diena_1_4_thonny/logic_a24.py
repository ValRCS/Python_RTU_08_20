# # Boolean Algebra kas ir pamatā visiem datoriem (un elektronikai)
is_sunny = True
print(is_sunny)
is_sunny = not is_sunny # we reverse the logic
print(is_sunny)
is_sunny = not is_sunny # we reverse the logic
print(is_sunny)
is_sunny = not is_sunny # we reverse the logic
print(is_sunny)
print(not True, not False) # negation Python uses not, some other language use !
# 
# # logical conjuction and in Python we use and (not &&)
print(True and True) # only True here
print(True and False)
print(False and True)
print(False and False)
#
# we can have conjuctions on multiple statements
print(2*2 == 4 and is_sunny and 5 > 1)
# # above is False since in a chain one False statement will ruin everything
is_sunny = not is_sunny # we reverse the logic
print(2*2 == 4 and is_sunny and 5 > 1)
# 
# # logical disjunction with or (Python uses actual or not ||)
print(True or True)
print(True or False)
print(False or True) # all 3 of the above ar True
print(False or False) # only one which is False
#
# XOR - True when only one side is True but False when both or none
is_raining = True
my_xor = (is_sunny and not is_raining) or (not is_sunny and is_raining)
# print(False or False or True or False) # still True

# we also have bit operators
a = int('0b101', 2) # 5 because first 1*2**0 + 0*2**1 + 1*2**2
b = 7
print(bin(b))
print(bin(8))
print(bin(9))
print(a & b) # should be 5
print(a | b) # should be 7
print(a ^ b) # THIS is BIT xor 111 un 101 we are left with 010