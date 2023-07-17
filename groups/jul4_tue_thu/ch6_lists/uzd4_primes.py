#4.Uzdevums -> Pirmsskaitļi
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
 
def get_primes_list(n):
    primes = []
    if n < 1:
        return primes
    if n == 1:
        primes.append(2)
        return primes
    num = 3 #starts with first prime numb
 
    while len(primes) < n :
        # for i in range(2, int(math.sqrt(num)) + 1): # could have used num**0.5 for square root
        #     if num % i == 0:
        #         break
        # else: # for loop fell through without finding a factor
        #     primes.append(num)
        if is_prime(num):
            primes.append(num)
        num += 2 #skips even numbers
    return primes
 
# Example 
list_lng = 2_000
prime_list = get_primes_list(list_lng)
print(prime_list)