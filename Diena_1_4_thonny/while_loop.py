# # while loops
# print("Hello")
# print("Hello")
# print("Hello")
# # # DRY princips - do not repeat yourself
# 
# i = 0
# while i < 3: # while i < 3 is True
#     print("Hello")
#     i += 1 #  same as i = i + 1 if we forget this lets see what happens....
# 
# i = 1 # reset our iterator variable
# while i <= 5:  # so while i < 5 == True the loop will run
#     print("Hello Nr.", i)
#     print(f"Hello Nr. {i}")
# #     # do more stuff here inside the loop
#     i += 1 # i = i + 1   # python has no ++
# # #     
# # # # loop is finished here
# print("This will happen no matter what")
# 
# i = 10
# while i > 0:
#     print("Going Down the floor:", i)
#     i-=1 # same as writing i = i - 1
# print("All done, am outside loop now i is now", i)
# # 
# total = 0 # do not use sum as a variable please :)
# start = 1
# end = 30
# step = 2
# i = start
# while i <= end:
#     total += i # total = total + i
#     print("Added ", i)
#     print("Sum so far is", total)
#     i += step
# # print("20 to 30 summed is", total)
# print(f"{start} to {end} by {step} step summed is {total}")
# # # # for simple sums we could have done this as below with sum and range
# print(sum(range(20,30+1)))
# print(sum(range(1,10+1)))
# 
# i = 10
# while i<=20:
#     print("Now on ", i)
#     i+=2 # so counting only in steps of 2
# print(i)
# 
# i = 5
# while i != 1:
#     print(i)
#     i-=1
#

import random
# print(random.randint(1,6))
# # 
# # indeterminate loop
# my_num = random.randint(1,20)
# # while my_num != 1 and my_num != 2 and my_num != 15:
# while my_num >= 3:
#     print("Current throw", my_num)
#     my_num = random.randint(1,20)
# # i=0
total = 0
while True: # infinite loop but we have break
    prompt = input("Do you want to quit (Y/N)?")
#     if prompt == "Y":
    if prompt.upper().startswith("Y"): # so now Yeah, yes will work and y also
        print("Quitting loop")
        break
    num = input("Enter a number to add to total")
    num = float(num)
    total += num
    print(f"After adding {num} our total is {total:.2f}")
print("out of loop our total is {total}")
# while i<5:
#     print(i)
#     i+=1
#     if i>2:
#         print("i is larger than 2", i)
#     else:
#         print("this is just smaller or equal to 2", i)
# #     if i==3:
# #         break # so this would cause else not to execute
# else: #finally would have been a better name
#     print("This prints when loop ends normally",i) # this would not print on break
# print("This always prints")