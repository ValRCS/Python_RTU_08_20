def get_positive_int(prompt):
    while True:
        user_inp = input(prompt)
        try:
            number = int(user_inp)
            if number < 0:
                print("Ievadiet pozitīvu veselu skaitli")
                continue
            return number # this immediately quits the function with the return value
        except ValueError:
            print("Ievadiet veselu pozitīvu skaitli")
    # we are never going to get to this point since we are going to return from the function


 
# result_list = [] # do not need it yet


# let's make a function is_prime
def is_prime(number):
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

# let's define a function get n primes
def get_n_primes(n):
    prime_list = []
    number = 1
    while len(prime_list) < n:
        number += 1
        if is_prime(number):
            prime_list.append(number)
    return prime_list

# the main program
length = get_positive_int("Ievadiet cik pirmsskaitļus vēlaties: ")
result_list = get_n_primes(length)
print(result_list) # i could have made a function to pretty print the list

# while len(prime_list) < length:
#     number += 1
#     for i in range(2, int(number**0.5)+1):
#         if number % i == 0:
#             break
#     else: # this else is for the for loop, not the if
#     # this means that the for loop finished without breaking
#     # this saves on needing to use a flag variable
#         prime_list.append(number)
#     # now we go back to check if our list is long enough
 
# print(prime_list)