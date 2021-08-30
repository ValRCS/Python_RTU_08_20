# # 1. Uzdevums:

#Uzdevums 1
for n in range(1,101):
    msg = str(n) # default
    if n%5==0 and n%7==0:
        msg = "FizzBuzz"
    elif n%5==0:
        msg = "Fizz"
    elif n%7==0:
        msg = "Buzz"
    if n == 100:
        print(msg, end="")
    else:
        print(msg, end=",")

#  
# i=0
# while i < 100:
#     i += 1
#     my_end = ","
#     if i == 100:
#         my_end = ""
#         
#     if i % 5 == 0 and i % 7 == 0:
#         print("FizzBuzz", end=my_end)
#         continue 
#     elif i % 7 == 0:
#         print("Buzz", end=my_end)
#         continue
#     elif i % 5 == 0:
#         print("Fizz", end=my_end)
#         continue
#     print(i, end=my_end)