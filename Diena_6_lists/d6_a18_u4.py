# 4
print("#4 uzdevums")
show_primes=int(input("How much primes we will show ? "))
prime_check= 1
primes_list=[]

while True:
    prime_check += 1 # we could preseed list with 2 and start at 3 jumping by 2
    if len(primes_list) >= show_primes:
        print("Got enough primes, all good")
        break
    is_prime=True
    for it in range(2,int(prime_check**0.5)+1):
        if prime_check % it == 0:
            print(prime_check, "Not prime it divides by", it)
            is_prime = False
            break
    if is_prime:
        print("Cool", prime_check, "is prime")
        primes_list.append(prime_check)
print(f"First {show_primes} primes are: {primes_list}")