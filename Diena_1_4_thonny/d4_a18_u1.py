first_i = 1
last_i = 100
step = 8
step_2 = 5
 
for my_num in range(first_i, last_i+1):
    end_symbol = ","
    if my_num == last_i:
        end_symbol = ""
            
    if(my_num % step == 0 and my_num % step_2 == 0):
        print(f"FizzBuzz", end = end_symbol)
    elif (my_num % step == 0):
        print(f"Fizz", end=end_symbol)
    elif (my_num % step_2 == 0):
        print(f"Buzz", end=end_symbol)
    else:
        print(my_num, end = end_symbol)



# for i in range(1,100+1):
#     if i%5 == 0 and i%7 == 0:
#         rez = 'FizzBuzz'
#     elif i%7 == 0:
#         rez = 'Buzz'
#     elif i%5 == 0:
#         rez = 'Fizz'
#     else:
#         rez = str(i)
#     print(f'{rez},',end='')