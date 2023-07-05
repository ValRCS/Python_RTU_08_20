import random
a = random.randint(-100,100)
b = random.randint(-100,100)
c = random.randint(-100,100)
print("Original", a,b,c)

if a <= b <= c: # same as a<=b and b<=c
    print(a,b,c)
elif a <= c <= b:
    print(a,c,b)
elif b <= a <= c:
    print(b,a,c)
elif b <= c <= a:
    print(b,c,a)
elif c <= b <= a:
    print(c,b,a)
else: # nothing else remains c<=a<=b
    print(c,a,b)

# if we had 4 it would need 4! 24 cases to consider
# in real life we would use sorted or sort method for some collection data type
