# Arnis
number_of_primes = input("cik primskaitļu nepieciešams atrast? ")
try:
    number_of_primes = int(number_of_primes)
    i = 1
    candidate = 3
    primes = ["1: 2"]
    while len(primes) < number_of_primes:
        is_prime = True
        i = 2
        while True:
            if candidate % i == 0:
                is_prime = False
                break
            i += 1
            if i > candidate**0.5:
                break
        if is_prime:
            primes.append(str(len(primes)+1)+": "+str(candidate))
            # print(n)
        candidate += 1
    # print(primes)
    print(*primes, sep="\n")
except ValueError:
    print("nekorekta ievade")
