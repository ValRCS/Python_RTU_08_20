# Python has bit operations
a = 4
b = 5
c = 6
d = 7
e = 8
print(bin(a))
print(bin(b))
print(bin(c))
print(bin(d))
print(bin(e))
# we have bitwise and using &
# so we keep 1 bits where both bits are 1
print(a&b) # 4 since only 4 bit matches
print(b&d) # so 5&7 will be 5 since we match on 1 bit and 4 bit
# bitwise or using |
# we keep 1 bits where at least one side has that bit
print(b|c) # 5|6 == 7 we keep all bits in this case
print(b|d) # 5|7 == 7 again 7
print(d|e) # 7|8 == 15 since all bits are only represented once
# negation bitwise
# same as -(n+1)
print(~b) # -(5+1) == -6
print(~e) # -9 == -(8+1)

# we even have bitwise XOR - only one bit should be set on either side
print(a^d) # should be 3 because 4 bit is set on both sides
print(b^d) # should be 2 since 4 bit is set and also 1 bit is set on both

# there are also << bit shifts and also >> shifts
print(2>>4)
print(2<<4) # 32 ( so essentially a * (2**b)
print(10<<3) # should be 80



