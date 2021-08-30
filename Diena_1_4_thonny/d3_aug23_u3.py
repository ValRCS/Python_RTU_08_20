#3 uzdevums
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

        
if a <= b <= c:
    print(a , b , c)
elif a <= c <= b:
    print("Branch acb")
    print(a , c , b)
elif b <= c <= a:
    print(b , c , a)
elif b <= a <= c:
    print(b , a , c)
elif c <= b <= a:
    print(c , b , a)
else:
    print(c , a , b)