# while loops
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")


# while True:
#     print("Alice talked and talked")
#     print("more talking")
    # return to start of while loop
    
# counter = 3
# counter = 23
# while counter < 5:
#     print(f"Counter is now {counter}")
#     # if we want to quit this loop we need to change counter
#     counter += 1 # same as counter = counter + 1
    # still inside loop
# out of loop here
# print(f"Counter once we are finished is {counter}")

# i = 9
# while i > 0:
#     print(f"Going down to floor No. {i}")
# #     i -= 1 # same as i = i - 1
#     # if i am impation I could go down quicker
# #     i -= 2
#     i -= 5
# # outside loop
# print(f"I am now on floor {i}")

# i = 20
# total = 0  # do not use sum for variable name because sum is a function in Python
# while i < 40:
#     print(f"i is {i} and total is {total}")
#     total += i # total = total + i
#     i += 5
#     
# print(f"At the end i is {i} and total is {total}")
# # could have use sum and range
# print(sum(range(20,40,5)))

# let's generalize
# start = 1_000  # same as 1000 _ is for humans
# end = 2_000
# step = 250 # could write this way... 2_5_0
# # initialization
# i = start
# while i <= end:
#     print(f"Doing something with {i}")
#     i += step
# print(f"Finished with {i}")

# i = 0
# while True:
#     print(f"Doing something with {i}")
#     if i > 20:
#         print(f"I am done with {i}")
#         break # this exits current loop
#     i += 5
# print("we are out of loop!")
# print(f"I is now {i}")

# using break we can make a small app to do some calculations

# total = 0
# user_input = "" # empty string
# while True:
#     user_input = input("Enter number or q to quit")
#     if user_input == "q" or user_input == "Q":
#         print("Quitting time")
#         break
#     # i can have other breaks
#     if user_input == "QUIT":
#         break
#     number = int(user_input)
#     total += number
#     print(f"You entered {number} now total is {total}")
#     # total += int(user_input) one liner
# print(f"END: You entered {number} now total is {total}")

i = 0
# while i < 10:
#     print(i)
#     if i == 4:
#         print("i is 4", i)
#         print("will jump")
# #         i += 2
#         continue # will jump to start of while loop
#     if i == 5:
#         print("i is 5", i)
#         break
#     i += 1