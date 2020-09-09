print(True,False)
print(2*2 == 4)
print(2*2 == 5)
isCalcGood = 3*3 == 10 # from the right side we compare first
b = 2*2
c = 4
c == 2*2 # c exists now but the result is not saved
a = 50
print(a != b, b != c , c != a)
print(4 > 4, 4 > 5, a > b, b > a)
print(4 < 4, 4 < 5, a < b, b < a)
print(4 <= 4, 4 <= 5, a <= b, b <= a, b <= c)
print(4 >= b, 4 >= 5, a >= b, b >= a, b >= c)

# the next two we use less in real
print(b is c) # this actually compares whether they are they point to same object
print(id(b) == id(c)) # same as above line
print(b == c)