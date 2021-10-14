primes_list = []
max_primes = int(input("Please input number of primes to find:"))

i = 2
 
while len(primes_list) < max_primes:
    # print(primes_list)
    for n in range(2, int(i**0.5)+1):
        if i % n == 0:
            break
    else:  # this else is for for loop when it does not break
        primes_list.append(i)
    i +=1
print(primes_list)