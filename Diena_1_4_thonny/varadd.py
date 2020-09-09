a = 5
b = 20
c = a + b
print(c)
a = a + b
print(a)
a = a + 10
# a = a + 10 is very common operations
a += 10 # same as a = a + 10
# a++ is not in Python
a += 1
b = b / 10
print(b, type(b))
b /= 10 # b = b / 10
b /= 10 # b = b / 10
c -= 1
d = a+b+c
print(round(d))
print(round(d,2))
print(round(d,3))
d += 0.98
d = int(d)
myStr = "Valdis"
myStr += " aha!" # same as myStr = myStr + " aha!"
myStr += " aha!"
myStr += " aha!"
myStr += str(d)
