# logical operators
print(True and True) # not &&, Python uses and
print(True and False)
print(False and True)
print(False and False)
a = 4
b = 5
c = 10
print(a == 2*2 and a < b)
print(a < b and b < c)
print(a < b < c) # same as above line
print(True and a == 2*2 and b < c)
print(True and a == 2*2 and b < c and a > c) # one bad fly will spoil
print(True and a > c and a == 2*2) # firt false result will stop the eval

print(True or True) # not ||, Python uses or
print(True or False)
print(False or True)
print(False or False)

print(False or False or False or a == 2*2 or False)
is_my_statement_true = False or False or False or a == 2*2 or False

# 
print(True or True and False or True)

print(not True) # nevis ! True
print(not False)
print(not 2*2 == 4)
print(not not 2*2 == 4)

print(5 & 6) # bitwise and there are more bitwise operators who need them
print(bin(5))
print(bin(6))
print(bin(4))
