# 4.uzd.
 
primes_list = []
number = 0
c = 0
count = int(input('Cik pirmskaitļus izvadīt?'))
while c <= count:
    number += 1
    if number > 1:
        for i in range(2, number): # could optimize with sqrt
            if number % i == 0:
                break
        else: # this is for loop else 
            primes_list.append(number)
            c += 1
    else:
        continue
 
print(primes_list)