##############################
#####  Task #6 ###############
##############################
num = int(input("Enter your number here: "))
 
for i in range(2, int(num**0.5)+1): # we only need to check up to square root
    if num % i == 0:
        print(num, f"is not a prime number divides by {i} .. bad cryptography :/")
        break
else: # no break thus it is prime!
    print(num, "is a prime number")