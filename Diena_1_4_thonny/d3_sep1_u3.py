print("3. uzdevums")
 
a = int(input("Input 1st number! "))
b = int(input("Input 2nd number! "))
c = int(input("Input 3rd number! "))
 
if a <= b <= c:
    print(a, b, c)
elif a <= c <= b:
    print(a, c, b)
elif b <= a <= c:
    print(b, a, c)
elif c <= a <= b:
    print(c, a, b)
elif b <= c <= a:
    print(b, c, a)
else: # c <= b <= a
    print(c, b, a)
    
print(sorted([a,b,c]))