# 3. Noprasiet lietotājam ievadīt 3 skaitļus, izvadiet tos sakārtotā secībā.
# 
# Piezīme: pagaidām šo uzdevumu risinam tikai ar if, elif, else darbībām
# 
# Pastāv arī risinājums izmantojot kārtošanu un list struktūru, kuru vēl neesam skatījuši.
  
    
a=float(input("1. cipars "))
b=float(input("2. cipars "))
c=float(input("3. cipars "))   
 
if c <= b <= a:
    print (c, b, a)
elif b<=c<=a:
    print (b, c, a)
elif a<=b<=c:
    print(a, b, c)
elif b<=a<=c:
    print(b, a, c)
elif a<=c<=b:
    print(a, c, b)
else:
    print(c, a, b)
    
import math
print("Factorial of 3", math.factorial(3))