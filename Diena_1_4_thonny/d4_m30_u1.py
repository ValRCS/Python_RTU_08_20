################## 1.uzd #######################
# Izdrukāt virknīti 1,2,3,4,Fizz,6,Buzz,8,.....34,FizzBuzz,36,....līdz  97,Buzz, 99,Fizz
# Tātad ja skaitlis dalās ar 5 tad Fizz
# Ja dalās ar 7 tad Buzz,
# Ja dalās ar 5 UN 7 tad FizzBuzz
# savādāk pats skaitlis
 
first = 1
last = 100
fizz = 5
buzz = 7
for n in range(first,last+1):
#     end = ","
#     if n == last:
#         end = "\n" # default is actually newline
    end = "\n" if n == last else "," # same as above 3 lines
    if n%fizz == 0 and n%buzz == 0:
        print(f"FizzBuzz", end=end)
    elif n%fizz == 0:
        print(f"Fizz", end=end)
    elif n%buzz == 0:
        print(f"Buzz", end=end)
    else:
        print(f"{n}", end=end)

# i = 1
#  
# while i <= 100:
#     if i%5==0 and i%7==0:
#         print('FizzBuzz,', end=',')
#     elif i%5==0 and i%7>0:
#         print('Fizz', end=',')
#     elif i%5>0 and i%7==0:
#         print('Buzz', end=',')
#     else:
#         print(str(i), end=',')
#     i += 1