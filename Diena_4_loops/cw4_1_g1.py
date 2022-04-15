for n in range(1,101):
    if n % 5 == 0:
        print("Fizz")
        if n % 5 == 0 and n % 7 == 0:
            print("FizzBuzz")
    elif n % 7 ==0:
        print("Buzz")
    else:
        print(f"{n}")
 


# n=100
# Fizz = 5
# Buzz = 7
# for i in range(1,n+1):
#     endsymbol = ","
#     if i == n:
#         endsymbol="\n"
#     if i % Fizz == 0 and i % Buzz == 0:
#         print("Fizzbuzz",end=endsymbol)
#     elif i% Fizz == 0:
#         print("Fizz",end=endsymbol)
#     elif i % Buzz == 0:
#         print("Buzz",end=endsymbol)
#     else:
#         print(i,end=endsymbol)
#  



# for i in range(1,101):
#     if i%5==0 and i%7==0:
#         print("FizzBuzz")
#     elif i%5==0:
#         print("Fizz")
#     elif i%7==0:
#         print("Buzz")
#     else:
#         print(i)