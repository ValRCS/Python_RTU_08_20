#4. uzd
 
prime_list = [2]
n = 2
N = int(input("Lūdzu ievadiet cik pirmskaitļus atrast: "))
 
while len(prime_list) < N:
    n+=1 # increase number to be tested
 
    for i in prime_list:
        if n%i==0:
            break # no need to continue testing
    else: # means for loop finished without break
        prime_list.append(n)
 
print(prime_list)