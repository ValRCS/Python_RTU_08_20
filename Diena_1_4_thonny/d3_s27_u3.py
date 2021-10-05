a=float(input("Ievadiet 1. skaitli"))
b=float(input("Ievadiet 2. skaitli"))
c=float(input("Ievadiet 3. skaitli"))

# if a <= b and b <= c: #same as below line
if a <= b <= c: 
    print("ABC")
    print(a, b, c)
elif a <= c <= b:
    print("ACB")
    print(a, c, b)
elif b <= a <= c:
    print("BAC")
    print(b, a, c)
elif b <= c <= a:
    print("BCA")
    print(b, c, a)
elif c <= a <= b:
    print("CAB")
    print(c, a, b)
elif c <= b <= a: #this could be else
    print("CBA")
    print(c, b, a)
else: # this should never execute
    print("Aliens!!")