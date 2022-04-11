# # # # # # # # # for loops are for definite iteration
# # # # # # # # # # 
# for num in range(5):  # range is sort of half ready number sequence
#     print("Hello there!")
#     print("Number is", num)
#     # so no need for num += 1 
# print("out of loop", num)
# # # # # # # # # so range takes range(start(default 0), end(not included), step)
# # # # # #
# # # # # so from 1 to 10 included
# for i in range(1, 11): # so careful of off-by-one errors, remember range will stop at 10 not 11 here!
#     print(f"I like this {i} better")
#     print(f"Square of {i} is {i*i}")
#     print(f"Square root of {i} is {i**0.5}")
# import datetime
# print(datetime.datetime.now())  # time stamp
# total = 0
# for i in range(100_000):
#     # i am not printing
# #     pass  # empty instruction for syntax reasons
#     total += i
# print(datetime.datetime.now())
# print(i)
# print(sum(range(100_000))) # even quicker to sum sequence of numerics
# # # for (int i = 0;i<500;i++) 
# # # # # 
# my_name = "Valdis Saul 😀"
# # # # # my_name = "Kaķis Ņauva"
# for c in my_name: # c could be also char, or my_c, c is just shorter
#     print("Letter ", c)
#     print(f"Letter {c} Unicode is {ord(c)}")
# # # #     if c < "a": # this would include digits space,etc
# # #     if c.isupper():  #works  even on Latvian capital letters such as Ņ Ā etc
# # #         print("You are using capital letters are you not?", c)
# # #     else:
# # #         print("not capital could be anyting else", c)
# # # # #         
# # # # # # # # #     
# # # # # # print("This happens after the loop is done")
# # # # # # # 
# # # # # # range with 2 parameters we have start inclusive and until end exclusive
# for n in range(20,25):
#     print(n)
# # # # # # # # # #
# # # # # 
# for my_num in range(100,110+1,2): # i can add step to range
#     print(my_num)
# print(f"Done with loop and my_num is {my_num}")
# # # # #     
# for my_num in range(30,10-1,-5): # i can add step to range
#     print(my_num)
# # # # # #     
# start = 20
# end = 38
# step = 4
# early_break = 27
# fence_post = 1
# for my_num in range(start,end+fence_post,step): # i can add step to range
#     print(my_num)
#     if my_num > early_break:
#         print(f"Reached our early break threshold {early_break}")
#         break
#     else:
#         print("still good", my_num)
# # # # # # # rarely used is else for for loop
# # # # else: # when for loop terminates normally - without breaks
# # # #     print("no early break, so loop ended normally", my_num)
# # # # print("Normal main flow")
# # # # # # #     
# # # # # # #     
# # # # # # # 
# # # # # # # # # # 
# # # # # # # # # # 
# for _ in range(3):  # _ means that we do not care about the variable, i just want to do something 3 times
#     print("We do not need the number in this case")
    # do more stuff
# # # # # # # # #
# # # # # # # 
# # # # big_total = 0
# # # # even_number_count = 0
for i in range(10,50,10): # outer loop
    for j in range(1, 3+1):  #inner loop
        result = i * j
        print(f"{i}x{j}={result}")
# # #         big_total += result  # big_total = big_total + result
# # #         if result % 2 == 0:
# # #             print("oh even number", result)
# # #             even_number_count += 1
# # # # # # # # #     
my_name = "Valdis"
for c in my_name:
    print("Letter ", c)
    
# Python way of obtaining index for some sequence we are looping through
for index, c in enumerate(my_name):
    print("Letter ", c)
    print(f"Index {index} is letter {c}")
# # # # # # # # #     
# # # # # # # # my_list = [1,2,100,105,"Valdis","potatoes", 9000, 107.35]
# # # # # # # # total = 0
# # # # # # # # big_items = 0
# # # # # # # # for item in my_list:
# # # # # # # #     print("Working with item: ", item)
# # # # # # # #     if type(item) == int or type(item) == float:
# # # # # # # #         total += item
# # # # # # # #         if item > 100:
# # # # # # # #             big_items += 1
# # # # # # # # #             
# # # # # # # my_num_list = [1,6,17,7,-6,49,642,6,2,-5555] # this is a list
# # # # # # # # # 
# # # # # # # my_max = None
# # # # # # # for num in my_num_list:
# # # # # # #     print("Checking", num)
# # # # # # #     if my_max is None: # this will happen with first item
# # # # # # #         my_max = num
# # # # # # #     if num > my_max:
# # # # # # #         print("New max is", num)
# # # # # # #         my_max = num
# # # # # # # # # 
# # # # # # # print("My max is", my_max)
# # # # # # # print(max(*my_num_list)) # short way of finding max in list
# # # # # # # # 
# # # # # # # # # So what do we do when we need and index
# my_name = "Valdis Saulespurēns"
# # # # # # # # print(f"{my_name} is {len(my_name)} characters long")
# # # # # # # # print(my_name[0])
# # # # # # # # print(my_name[5])
# # # # # # # # # anti-pattern do not write this way in Python
# # for n in range(0, len(my_name)):
# #     print(n, my_name[n])
# # # # # # # # # #     
# # # # # # # # # # more Pythonic is using enumerate:
# # # # # # # # # # use this if you need index
# # # # # # # # 
# # my_name = "Valdis"
# # for index, c in enumerate(my_name):
# #     print("Letter", index, "is",c)
# # # # # # # #     
# # # # for index, c in enumerate(my_name,start=1001):
# # # #     print("Letter", index, "is",c)
# # # # # # # # #
# # # # # # # # # if i do not like 0 i can start with any number
# # # # # # # # for i, c in enumerate(my_name, start=101):
# # # # # # # #     print("Letter", i, "is",c)
# # # # # # # # 
# # # # # # # #
# # # # # # # # my_num = 20
# # # # # # # # for n in range(1,11):
# # # # # # # #     reminder = my_num % n
# # # # # # # #     result = my_num // n # whole number
# # # # # # # #     print(f"{my_num} divided by {n} gives {result} with {reminder} as reminder")
# # # # # # # 
for n in range(1,21):
    if n%2 == 0: # even numbers have no reminder when divided by 2
        print(f"{n} is even", end=",")  # end="," I change from default newline
    else:  # reminder is 1 so odd
        print(f"{n} is odd", end=",")
print() # prints newline 
import string
print(string.digits) # contains digits
print(" "*10+"*"*6)  # could be useful in 2nd assignment today
# # # # # # #
# # # # # # # print by default has end value \n - newline
# # # # # # # we can change this
# # # # # print("Fizz", end=",")
# # # # # print("Buzz", end=",")
# # # # # print("342", end="****")
# # # # # # 
# # print(" "*10+"*"*6)
# # for n in range(5):
# #     print(" "*n+"*"*n)
# # # # # #same as above but with inner loops
# #     for _ in range(n):
# #         print(" ", end="")
# #     for _ in range(n):
# #         print("*", end="")
# #     print() # to start a new ine
# # # # # print() # prints new line
# 