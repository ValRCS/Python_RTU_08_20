# # # Boolean Algebra kas ir pamatā visiem datoriem (un elektronikai)
is_sunny = True
print(is_sunny)
print("let the toggling begin with not")
is_sunny = not is_sunny # Toggle pattern we reverse the logic
print(is_sunny)
is_sunny = not is_sunny # we reverse the logic
print(is_sunny)
is_sunny = not is_sunny # we reverse the logic
print(is_sunny)
print(not True, not False) # negation Python uses not, some other language use !
# #
# # # logical conjunction and in Python we use and (not &&)
print("Testing and logic, logical conjuction")
print(True and True) # only True here
print(True and False)
print(False and True)
print(False and False) # last 3 are False
# #
# # we can have conjuctions on multiple statements
print(2*2 == 4 and is_sunny and 5 > 1)
# # # above is False since in a chain one False statement will ruin everything
a = 0
print( a != 0 and 10 / a) # so 10 / a will not run

is_sunny = not is_sunny # we reverse the logic
print(2*2 == 4 and is_sunny and 5 > 1)
# #
# # # logical disjunction with or (Python uses actual or not ||)
print(True or True)
print(True or False)
print(False or True) # all 3 of the above ar True
print(False or False) # only one which is False

are_pigs_flying = False
is_devil_skating = False
is_september = True
print(are_pigs_flying or is_devil_skating or is_september or 2*2 == 5) # so True...
is_a_good_day = are_pigs_flying or is_devil_skating or is_september or 2*2 == 5
print(is_a_good_day)

# #
# # XOR - True when only one side is True but False when both or none
is_raining = True
my_xor = (is_sunny and not is_raining) or (not is_sunny and is_raining)
# # print(False or False or True or False) # still True
#
# # we also have bit operators - for hardware operation
a = int('0b101', 2) # 5 because first 1*2**0 + 0*2**1 + 1*2**2, so 1 + 0 + 4
print(a)
b = 7 # 111 in binary == 1+2+4
print(bin(b))
print(bin(8))
print(bin(9)) # SO + 1*8 + 0*4 + 0*2 + 1*1
print(a & b) # should be 5 because both 5 and 7 have 1 bit set and also 4 bit set but 2 bit is only set for 7
print(a | b) # should be 7
print(5 | 2) # also 7 because 101 or 010 will be 111
# below is bitwise XOR, so only bits on one side will be considered
print(a ^ b) # THIS is BIT xor 111 un 101 we are left with 010
print(5 ^ 2) # now 7
print(5 ^ 3) # this should be 6 because both sides have 1 bit set