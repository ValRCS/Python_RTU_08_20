# 4. uzdevums
# - = - = - = - = - = - = - = - = - = - = - = - = 
 
i = 2
count = 0
how_match = int(input('Cik daudz pirmsskaitlutu velies? >> '))
 
primes = []
while True:
    
    for e in range(2, i):
        if i % e == 0:
            break # we break out of inner loop
    else: # this else works when for loop is finished and no break is found
        print(i)
        primes.append(i)
        count+=1
    
    if count > how_match:
        break # we break out of outer loop
 
    i +=1
print(primes)