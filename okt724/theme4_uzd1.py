# num=1
# while num<=100:
#     if num % 5 == 0:
#         print('Fizz',end=",",)
#     if num % 7 == 0:
#         print('Buzz',end=",",)
#     if num % 5 == 0 and num % 7 == 0:
#         print('FizzBuzz',end=",",)
#     if num % 5 !=0:
#         print (num,end=",",)
#     num+=1
# better to use for loop here
# the next 4 variables could be initiated from user intput or some other source
fizz = 5
buzz = 7
start = 1
finish = 100
for cipars in range(start, finish+1):  # Cikls no start līdz end ieskaitot
    end_symbol = ", "  # default for this application
    # now I check special case
    if cipars == finish:
        end_symbol = "\n" # \n means newline, could use "" for nothing
    # could have used else here
    # else:
    #	end_symbol = ", "
    
    # now my formatting is ready and I can do main logic of this loop
    if cipars % fizz == 0 and cipars % buzz == 0:
        print("FizzBuzz", end=end_symbol)
    elif cipars % fizz == 0:
        print("Fizz", end=end_symbol)
    elif cipars % buzz == 0:
        print("Buzz", end=end_symbol)
    else:
        print(cipars, end=end_symbol)
 