# num=1 not needed because num will be 1 when we start the for loop
for num in range(1,101):
    result = ""
    if not num%5==0 and not num%7==0:
        result = num
    elif num%5==0:
        result = "Fizz"
    elif num%7==0:
        result = "Buzz"
    else:#num%5==0 and num%7==0
        result = "FizzBuzz"
    print(result)



# for n in range (1,40):
#     if n % 5 == True:
#         print(f'Fizz')
#     elif n % 7 == True :
#         print(f'Buzz ')
#     elif n % 5 == True and n % 7 ==True:
#         print(f'Fizzbuzz ')
#     else:
#         print(f'{n}')



# i=1
# while i<40:
# #     if i % 5 == 0 and i % 7 == 0:
# #         print("FizzBuzz",end=",")
# #     elif i % 5 == 0:
# #         print("Fizz",end=",")
# #     elif i % 7 == 0:
# #         print("Buzz",end=",")
# #     else:
#     print(i,end=",")
#     i+=1