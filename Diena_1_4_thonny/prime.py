n = int(input("Enter number to check for prime: "))
is_prime = True
if n % 2 == 0:
    is_prime = False
    print("n divides by 2")
for i in range(3,int(n**0.5)+1,2):
    if n % i == 0:
        print("not a prime", n, "divides by", i)
        is_prime = False
        break
if is_prime:
    print(n, "is prime")
