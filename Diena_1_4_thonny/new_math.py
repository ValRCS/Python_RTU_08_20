a = 5
b = 20
c = a + b
# remember = is assignment
# we evaluate from the right side
a = a + b
a += b # a = a + b
a += c # a = a + c
a *= 10
print(a, type(a))
a /= 100
print(a, type(a))
a += 13
name = "Valdis"
middle = "Nemo"
myName = name + " " + middle
myName2 = f"{name} {middle}"
print(myName2, end="****\n")
# next line will not use newline 
print(myName2, end="")
print("More stuff")

print(max(a,b,c))
myBigName = myName2.upper()
myTinyName = myName2.lower()