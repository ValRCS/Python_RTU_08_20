# sk=int(input("Please enter any positive integer number:"))
# is_prime = True
# for i in range(2,sk):
#     if not sk%i:
#         is_prime = False
#         break
# if is_prime:
#     print(f"{sk} is prime")
# else:
#     print(f"{sk} is not prime it divides by {i}")

import math
num=int(input('Please enter natural positive number'))
end = math.ceil(math.sqrt(num))
# end = int(num**0.5)+1 would also work without math library
# print(end)
i = 1
while i < end:
    i += 1
    if num % i == 0:
        print(f'Number is not a Prime number, because it can be divided by {i}')
        break
    elif i == end:
        print(f'Number {num} is a Prime number')