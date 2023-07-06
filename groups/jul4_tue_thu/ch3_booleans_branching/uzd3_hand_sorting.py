a = int(input("tell me a number:"))
b = int(input("tell me another number:"))
c = int(input("and another one, please1:"))
print("thanks!")

if a <= b <= c:
    print(a, b, c)
elif a <= c <= b:
    print(a,c,b)
elif b <= c <= a:
    print(b, c, a)
elif b <= a <= c:
    print(b,a,c)
elif c <= a <= b:
    print(c,a,b)
else:# only c b a remains
    print(c, b, a)

# if we had 4 numbers we would need 24 different cases....
# luckily we have sorting built in for next lecture