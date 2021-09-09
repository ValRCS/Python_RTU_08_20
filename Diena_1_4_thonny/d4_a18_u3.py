n = int(input('Enter number: '))
flag = False
if n > 1:
    for i in range(2, int(n**0.5)+1): # we only need to check up to square root
        if n % i == 0:
            print(f"{n} divides by {i}")
            flag = True
            break
if flag:
    print(n, 'is not a prime number')
else:
    print(n, 'is a prime number')