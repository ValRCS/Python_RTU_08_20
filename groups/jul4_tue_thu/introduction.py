print("Let's talk about Python basics")
# by default we print to std output - we change that later
# Python 3 has full Unicode support
print("Varu drukāt Latviski par runčiem")
print("Es varu dzert arī alu... 🍺")
# arithmetic - pretty normal
print(2+2)
# regular arithmetic
print(2*3)
print(-7)
print(10/4) # 10/2 returns float
print(10//4) # returns int 2
# reminder
print(20%7) # 6 will be reminder
print(10%2, 11%2, 12%2, 13%2) # note that , by default gives us space
# standard arithmetic rules apply but we can use parenthis to change it
print((2+5)*(4+6))

# i can multiply strings...
print("Beer"*5)
# i add strings .. concatenate
print("Riga " + "Technical" + " University")
# i can't add strings and number - need to cast first
print("Agent00" + str(7))
print("Agent00")

# power is built in
print(2**8) # 256
print(2**16) # 65536
# how about 32 bits
print(2**32) #
# how about 64bits
print(2**64)
# Python has built in Large number support
print(10**82) # could go higher
# print(100**20)

# how to print without newline
# we use end = "" paremeter
print("Something", end="")
print(" cool") # now this has newline
