#4. uzd
 
prime_list = [2]
n = 2
N = int(input("Lūdzu ievadiet cik pirmskaitļus atrast: "))
 
while len(prime_list)<N:
    n+=1 # increase number to be tested
    is_prime = True
 
    for i in prime_list:
        if n%i==0:
            is_prime = False
            break # no need to continue testing
    if is_prime:
        prime_list.append(n)
 
print(prime_list)