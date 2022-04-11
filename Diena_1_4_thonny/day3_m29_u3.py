# Trešais uzdevums
 
# Enter the numbers
a = float(input("1st number: "))
b = float(input("2st number: "))
c = float(input("3d number: "))
 
# Checkout the numbers
if a <= b <= c :
    print(a, b, c)
elif a <= c <= b :
    print(a, c, b)
elif c <= b <= a:
    print(c, b, a)
elif c <= a<= b:
    print(c, a, b)
elif b <= c <= a:
    print(b, c, a)
else:  # b<=a<=c
    print(b, a, c)
 