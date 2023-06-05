# print("Hello Robotics!)")
# print("I like programming 😁")
print("Raibi Runči Rīgā Rūc 🐱") # we can use any unicode
# comments are for humans
# computers ignore anything after single hash mark
# ideal comments explain why not what

# we can use Python as calculator

print("2+2") # notice the difference
print(2+2)
print("Let's add 20 and 22 result is", 20+22)

# we can do the usual math
print(10-3)
print(10*2)
print(30/2) # notice the result here
print(30/11)
print(30//11) # //gives us whole number
print(30%11) # reminder - more correct would be modulo
print(30//11, 30%11, (30//11)*11 + 30%11) # should be 30
# technically there is a difference between modulo and reminder
# but that difference is only when we take modulo from - number
print(2**8)  # important number
print(4**0.5) # square root
# let's see how much memory we can use on 32 bit systems
print(2**32)
# how about 64 bit systems?
print(2**64)
# python has built in large number support - automatic
# how about Gogol?
print(10**100)
print("Alice did", "speak "*5)
print("Beer 🍺 "*7)
print("Valdis likes "+"beer") # string concatenation
# print("Valdis likes number "+42) # not quite
# we can convert pretty much anything to string with str
print("Valdis does like number "+str(42))
print(f"2+2={2+2}")  # i can use f strings to evalute results inside string template