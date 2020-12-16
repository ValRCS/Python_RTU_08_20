a = int(input("enter first number"))
b = int(input("enter second number"))
c = int(input("enter third number"))
if a >= b >= c:
    print(a, b, c)
elif b >= c >= a:
    print(b, c, a)
elif c >= a >= b:
    print(c, a, b)
elif a >= c >= b:
    print(a, c, b)
elif b >= a >= c:
    print(b, a, c)
else:
    print(c, b, a)