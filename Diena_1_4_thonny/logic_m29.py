# Logical Negation - Python uses not (not ! as many others)
# George Boole's - Boolean algebra
print(not True)
print(not False)
is_sunny = True
print(is_sunny)
is_sunny = not is_sunny  # toggle reverse existing
print(is_sunny)
is_sunny = not is_sunny  # toggle reverse existing
print(is_sunny)

# in python Logical Conjuction uses and (not &&)
print(True and True) # only True rest are False
print(True and False)
print(False and True)
print(False and False) # last 3 are False

print(True and True and True)

# python is lazy first bad apple ruins the whole batch
print(True and 2*2 == 4 and 3*3 == 10 and 10/0 == 1)

# Logical Disjunction
# Python uses or (not || as many others)
print(True or True)
print(True or False)
print(False or True)
print(False or False) # above all are True, this one is Falsee

a = 10
b = 9000
print(a == 10 and b == 9000) # False
print(a == 10 or b == 9000) # True
# exclusive OR - XOR
print((a == 10 and b != 9000) or (a != 10 and b == 9000))

# how about & , |, ^ operations
# those are bit operations
a = 5
b = 6
print(bin(a))
print(bin(b))
print(bin(255))  # 8 ones
print(128+64+32+16+8+4+2+1)

c = a & b # bitwise and
print(c) # 4 but why?
print(bin(c))

c = a | b # bitwise or
print(c) # 7 but why?
print(bin(c))

# c = a ^ b # exclusive or
# print(c) # 3 but why?
# print(bin(c))

print(a < b and b < c) # normal True

print(a < b < c) # even nicer same as above

print(a < b < c < 1000) # and so on

print(a < b < c < 9000 < 1000) # and so on