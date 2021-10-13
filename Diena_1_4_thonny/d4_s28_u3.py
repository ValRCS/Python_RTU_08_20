# Uzd. Nr.3
 
num = int(input("Please Enter a number that you would like to check: ")) #input a number to check
 
if num > 1:     # to exclude all numbers < 2, those are not prime numbers
    for i in range(2, int(num**0.5)+1):        #loop for checking the number (square root)
#             same result will be ### for i in range(2, int(num/2)+1): ### devided by 2 - the simple way
 
          if num % i == 0:  #check if for the modulus of number from interpretator should be 0, if not than FALSE
            print(f"{num} is not a prime, it divides by {i}")
            break
    else:
        print(f" {num} is a prime number") #if number is > than 1, and is a prime
        
else:
    print(f"{num} is not a prime number")   #if number <= 1 than not a a prime