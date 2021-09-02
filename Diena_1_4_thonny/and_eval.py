a = 10

b = 20

c = a and b # https://docs.python.org/3/reference/expressions.html#and
d = a == 10 and b == 20
e = a or b # this will be a (assuming a is truthy)
# so c is 20 because
print(a,b,c,d,e)
