#3. Noprasiet lietotājam ievadīt 3 skaitļus, izvadiet tos sakārtotā secībā.
# Piezīme: pagaidām šo uzdevumu risinam tikai ar if, elif, else darbībām
# Pastāv arī risinājums izmantojot kārtošanu un list struktūru, kuru vēl neesam skatījuši.
 
a = int(input("Please enter first number: "))
b = int(input("Please enter second number: "))
c = int(input("Please enter third number: "))

if a <= b <= c: # alternative would be a <= b and b <= c
    print(a, b, c)
elif a <= c <= b:
    print(a, c, b)
elif b <= a <= c:
    print(b, a, c)
elif b <= c <= a:
    print(b, c, a)
elif c <= b <= a:
    print(c, b, a)
else: # nothing else is possible just c <= a <= b
    print(c, a, b)
print("End")