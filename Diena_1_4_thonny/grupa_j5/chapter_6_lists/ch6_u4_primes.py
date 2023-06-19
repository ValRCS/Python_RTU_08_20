# start = int(input("Pirmskaitlu atlase intervala. Ludzu, ievadiet intervala sakumu no cik: "))
# stop = int(input("ludzu, ievadiet intervala beigas lidz cik: "))
 
# prime_list=[]
 
# for number in range( start , stop + 1 ) :
#     if number == 2 :
#         prime_list.append(number)
            
#     n = 1
#     while n <= number**0.5 :
#         n += 1
        
#         if number % n == 0 :
#             print(f"{number} nav pirmskaitlis, jo dalas ar {n}, nemam ara")
#             break
#         elif n >= number**0.5 : 
#             prime_list.append(number)
#             break
   
# if start <=1 :
#     prime_list.remove(1)     
 
 
 
# print(f"Intervala no {start} lidz {stop} ir sadi pirmskaitli {prime_list}")

########## 4. uzdevums ##########
 
count = int(input("Enter the number of prime numbers to print: "))
 
# primes = []
# number = 2
 
# while len(primes) < count:
#     is_prime = True
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         primes.append(number)
#     number += 1

# we can rewrite the above using for-else

# count = int(input("Enter the number of prime numbers to print: "))
primes = []
number = 2
while len(primes) < count:
    for i in range(2, int(number**0.5) + 1):
      if number % i == 0:
        break
    else: # so we have a prime number for loop finished without break
        primes.append(number)
    number += 1
print(primes)