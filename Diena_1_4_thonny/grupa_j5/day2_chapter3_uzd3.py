#3. Noprasiet lietotājam ievadīt 3 skaitļus, izvadiet tos sakārtotā secībā.
#Piezīme: pagaidām šo uzdevumu risinam tikai ar if, elif, else darbībām
#Pastāv arī risinājums izmantojot kārtošanu un list struktūru, kuru vēl neesam skatījuši.
 
a=int(input("ievadiet vienu no 3 skaitļiem: "))
b=int(input("ievadiet otro no 3 skaitļiem: "))
c=int(input("ievadiet trešo no 3 skaitļiem: "))
# if we skip conversion to in
# comparision will not work correctly
# string 9 will be greater than string 20 because of lexigraphical comparison
if a <= b <= c :
    print(a, b, c)
elif b <= c <= a :
    print(b, c, a)
elif c <= a <= b :
    print(c, a, b)
elif a <= c <= b :
    print(a, c, b)
elif b <= a <= c :
    print(b, a, c)
else: # c <= b <= a :
    print(c, b, a)