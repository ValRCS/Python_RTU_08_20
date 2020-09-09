a = int(input("Ievadi skaitli Nr.1: "))
b = int(input("Ievadi skaitli Nr.2: "))
c = int(input("Ievadi skaitli Nr.3: "))

if a <= b <= c:
 print(a, b, c)
elif a <= c <= b:
 print(a, c, b)
elif b <= a <= c:
 print(b, a, c)
elif b <= c <= a:
 print(b, c, a)
elif c <= a <= b:
 print(c, a, b)
else: # c <= b <= a:
 print(c, b, a)