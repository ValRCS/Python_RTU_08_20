print(2*2 == 4)
print(2*2 == 5)
a = 4
b = 5
print(a == b)
print(a == 2*2)
is_ab_equal = a == b
print(is_ab_equal)

print(2*2 != 5)
print(2*2 != 4) # this should be false because 2*2 == 4
is_not_equal = 2*2 != 5
c = 10
print(a > b, b > c, c > a)
is_c_larger_than_a = c > a
print(a < b, b < c, c < a, a < c)
print(a < b < c)
d = 5
print(a >= b, b >= c, c >= a)
print(d >= a, d >= b, d >= c)
print(a <= b, b <= c, c <= a)
print(d <= a, d <= b, d <= c)
e = 5.0
# this really means a and d point to the same object
print(b == e)
print(b is e)
print(b is d)
print(id(b) == id(d)) # same as b is d