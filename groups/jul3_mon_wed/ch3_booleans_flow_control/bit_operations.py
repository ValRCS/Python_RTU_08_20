# Python has bit operations as well
a = 3
b = 4
c = 10
d = 11
print(bin(a))
print(bin(b))
print(bin(c))
print(bin(d))
# bitwise &
print(a&b) # returns bits that are common , here nothing in common so 0
print(a&c) # only 2 is common so answer will be 2
print(a&d) # so 1 is common and 2 is common so answer will be 3
# we also have bitwsise OR with |
print(a|c) # will set all bits that at least one side has
# so we have 1 and 2 bit and 8 bit so 11
print(b|c) # so we have 2 bit and 4 bit and 8 bit so 14
# we also have bitwise XOR (regular logic in Python does not have it)
# in XOR only those bits that are not common but one side has it are set
print(a^b) # should be 7 since none of the bits are common
print(c^d) # only 1 bit is not common so answer is 1
# we have bitwise not ~
# should be -(n+1)
print(~c) # -11
print(~b) # -5
# we also hav bitwise shifts << and >> as well