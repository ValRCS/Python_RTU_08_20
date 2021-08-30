# 1. FizzBuzz     
# for n in range(1,100+1):
#     if n%5 == 0 and n%7 == 0: 
#         print("FizzBuzz", end=",")
#     elif n%5 == 0:
#         print("Fizz", end=",")
#     elif n%7 == 0:
#         print("Buzz", end=",")
#     else:
#         print(n, end=",")

# Lekcija-3
 
## Uzdevums-1
fizz = "Fizz"
buzz = "Buzz"
fizz_buzz = "FizzBuzz"
 
numbers = []
for num in range(1,101):
    if num % 35 == 0:
        numbers.append(fizz_buzz)
    elif num % 5 == 0:
        numbers.append(fizz)
    elif num % 7 == 0:
        numbers.append(buzz)
    else:
        numbers.append(str(num))
 
print(numbers)