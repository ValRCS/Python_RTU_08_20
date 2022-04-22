# print("Hello")
# print("Hello")
# print("Hello")
# how to do this 100 or more times?
# # # # # 
# while True:
#     print("hello there!")
#     print("keep going")
    # so called infinite loop
# # # # # # 
# i = 0  # so caller iterator, or index if you will
# while i < 5:  # while loops are for indeterminate time
#     print("Hello No.", i)
#     print(f"Hello Number {i}")
#     i += 1  # i = i + 1 # we will have a infinite loop without i += 1, there is no i++
# # # # # # # # # #
# print("Always happens once loop is finished")
# print("i is now", i)
# # # # # # #
# i = -5
# while i >= 0:
#     print("Going down the floor:", i)
#     # i could do more stuff
#     if i == 0:
#         print("Cool we reached the garage")
#     elif i > 5:
#         print(f"Higher floors {i}")
#     else:
#         print(f"Normal floor {i}")
#     i -= 1 # i = i - 1
# print("Whew we are done with this i:", i)
# # # # # # #
# total = 0 # do not use sum as name for variable, sum is used by python
# i = 20
# print(f"BEFORE loop i is {i} total is {total}")
# while i <= 30:
#     total += i # total = total + i
#     print(f"After adding {i} total is {total}")
# #     i += 2 # step will be 2 here
#     i += 5
# print(f"AFTER LOOP i is {i} total is {total}")
# print(sum(range(20,30+1,5))) # sum is used to sum ranges(and other iterative structures)
# # # # # 
# # # # # # #
# start = 100
# end = 400
# step = 120  # we do have a for loop for this type of looping but step here can be a float
# i = start  # initialization
# while i <= end:
#     print(f"i is {i}")
#     # we could do  more work here inside our loop
#     i += step  # same as i = i + step
# # # #
# print("AFTER LOOP i is ", i)
# # # # # # 
# start = 10
# end = 500
# step = 20
# increase = 5
#
# i = start
# while i <= end:
#     print(f"i is {i}")
#     step += increase  # increasing the increase
#     print("Step is now", step)
#     print(i)
#     i += step
# print(i)
# # # # # 
# # # # # # in general while loops are best suited for loops when we are not 100 % sure of when they will end
# # # # # # so sort of indeterminate
# # # # # 
# # # # # # # #
# # # in effect we can simulate a do while loop
# i = 10   # _000
# while True:  # so i am saying here that this loop should run forever .. unless I have something inside to break out
#     print("i is",i)  # this line will always happen at least once
#     # could add more lines which will run at least once
#     # in a while True loop it is typical to check for exit condition
#     if i >= 14:  # similar to while i < 14:
#         print("Ready to break out i is", i)
#         break  # with break with break out of loop
#     i += 2
# # # # # # # # # # above is simulating do while looping functionality
# print("Whew AFTER BREAK out", i)
# # # # # # # # #
# i = 20
# is_active = True
# is_raining = True
# # # # # # # # while active or is_raining:  # careful here so for while loop to keep running here JUST ONE of the conditions here have to be true
# while is_active and is_raining:  # so for while loop to keep running here BOTH conditions here have to be true
#     print(f"Doing stuff with {i}")
#     i += 3
#     # TODO update weather conditions
#     # so is_raining could be False as well
#     if i > 30:
#         is_active = False # i could do break as well
#         print("Active no more")
# print("AFTER loop ", i, is_active, is_raining)
# # # # # # # #
# # # # # 
# while True:
#     res = input("Enter number or q(Q) to quit ")
#     if res.lower().startswith("q"): # more lenient any word starting with Q or q will work to quit
# #     if res == "q":
#         print("No more calculations today. I am breaking out of the loop.")
#         break # we break out of loop
#     elif len(res) == 0:  # so i had an empty string here...
#         print("Hey! You just pressed Enter, please enter something...")
#         continue # we go back to line 102 and start over
#     
#     try:
#         num = float(res)
#     except ValueError: # we want to use a concrete error type
#         print("Oops not a real number, try again..")
#         continue # again back to line 102
#     
#     cube = num**3
#     cube = round(cube, 2) # 2 digits after comma
#     print(f"My calculator says cube of {num} is {cube}")
# # # # # # # #
# print("All done whew!")
# # # # # #
# outer_flag = True
# inner_flag = True
# i = 10
# # outer_loop
# while outer_flag:
#     print(i)
#     # innter loop
#     while inner_flag:
#         res = input("Enter q to quit")
#         if res == 'q':
#             print("got q lets break from inside")
#             break
#     i += 1
#     if i > 14:
#         print("outer break about to happen")
#         break
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # #
i = 0
while i < 10:
    print(i)
    i += 1  # this will be bugged think about the even case....
    if i % 2 == 0:   # i am testing whether some number has a reminder of 0 when divided by 2
        print("Even number", i)
        continue  # we skip the following loop instructions
    else:  # this will perform just like continue
        print("Doing something with odd number", i)
        # i += 1  # this will be bugged think about the even case...
    print("We do something here")   # with continue this would not run