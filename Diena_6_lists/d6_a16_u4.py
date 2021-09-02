# 4. Pirmskaitļi. Atrodiet un izvadiet pirmos N pirmskaitļus saraksta veidā.
# Piemērs: [2,3,5,7,11,...]
prime_list = []
n = int(input('Input number of prime numbers you want to see: '))
i = 2
count = 0
 
while count < n:
    c = 0
    for y in range(1, i + 1):
        if i % y == 0:
            c += 1
    if c == 2: # means divides by itself and 1
        count += 1
        prime_list.append(i)
    i += 1
print(prime_list)
# TODO optimize prime algorithm inside - the inner loop
# alernative would be to build a sieve of Eurosthene