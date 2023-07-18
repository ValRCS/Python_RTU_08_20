def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
 
def generate_prime_numbers(n):
    if n < 1:
        return []
    primes = [2]

    num = 3
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 2
    return primes
 
# n = int(input("Ievadiet izvadāmo pirmo pirmskaitļu skaitu: "))
n = 200
primes = generate_prime_numbers(n)
print(primes)