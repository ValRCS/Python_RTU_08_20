# Python offers bit operators
# print(bin(1))
# print(bin(2))
# print(bin(3))
# print(bin(4))

for n in range(10):
    print(f"{n} -> {bin(n)}")
    
# we can use bit and &
print(3 & 4) # bin & will give 1 onlye when both bits are 1
print(6 & 7) #

# we also have bit or using |
# so either bit will set 1
print(3 | 4) # 7 because we get all bits from 1,2 and 4
print(6 | 7) # 7 again

# if we did not have exclusive OR (XOR) in regular logic in Python
# in bit logic we do have it
print(3 ^ 4) # 7 because each number has no common bits
print(6 ^ 7) # 1 because 2 and 4 bits are common

# we would use this logic if we want to apply logic across multiple single bits
# saved in a number
# so when a number represent individual flags/on/off settings etc

print("bit AND for 14 and 12", 14 & 12)
print(14 | 12) # so 8, 4 and 2 bits are common
print(14 ^ 12) # so 2 because that is the only bit that is not common
print(bin(12))
print(bin(14))