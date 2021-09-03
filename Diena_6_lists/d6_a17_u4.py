"""
Atrodiet un izvadiet pirmos 20 (vēl labāk iespēja izvēlēties cik pirmos pirmskaitļus gribam) pirmskaitļus saraksta veidā t.i. [2,3,5,7,11,...]
"""
prime_count = int(input("Enter desired amout of prime numbers: "))
primes = [2]
 
head = 3
while prime_count >= len(primes):
    prime_found = True
    for i in range(3,head,2):
        if head % i == 0:
            prime_found = False
            break # we break from inner cycle 
    if prime_found:
        primes.append(head)
    head += 2
print(primes)