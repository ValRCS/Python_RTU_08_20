a = int(input("Ievadi skaitli"))
b = int(input("Ievadi otru skaitli"))
c = int(input("Ievadi trešo skaitli"))
 
if a <= b <= c:
    print(a, b, c)
elif b <= a <= c:
    print(b, a, c)
elif c <= a <= b:
    print(c, a, b)
elif a <= c <= b:
    print(a, c, b)
elif b <= c <= a:
    print(b, c, a)
elif c <= b <= a:
    print(c, b, a)