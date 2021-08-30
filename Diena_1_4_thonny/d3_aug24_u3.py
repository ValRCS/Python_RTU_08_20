a, b, c = int(input("Ievadiet skaitli ")), int(input("Ievadiet otru skaitli ")), int(input("Ievadiet trešo skaitli "))
print(a,b,c)
if a <= b <= c:
    print(a, b, c)
elif b <= c <= a:
    print(b,c,a)
elif c <= a <= b:
    print(c,a,b)
elif a <= c <= b:
    print(a, c, b)
elif b <= a <= c:
    print(b, a, c)
elif c <= b <= a: #we could even skip elif and use else
    print(c, b, a) 
# else: this should never happen
# there is an even easier way to sort... 
print(sorted([a,b,c]))