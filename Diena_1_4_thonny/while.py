# print("Hello")
# print("Hello")
# print("Hello")
# i = 1
# while i < 5: # while loops are for indeterminate time
#     print("Hello No.", i)
#     print(f"Hello Number {i}")
#     i += 1  # i = i + 1 # we will have a infinite loop without i += 1
# print("Always happens once loop is finished")
# print("i is now", i)
# i = 10
# while i >= 0:
#     print("Going down the floor:", i)
#     # i could do more stuff
#     if i == 0:
#         print("Cool we reached the garage")
#     i -= 1 # i = i - 1
# print("Whew we are done with this i:", i)
# 
# total = 0 # do not use sum as name for variable
# i = 20
# while i <= 30:
#     total += i # total = total + i
#     print(f"After adding {i} total is {total}")
#     i += 2 # step will be 2 here
# print(f"i is {i} total is {total}")
# 
# start = 20
# end = 400
# step = 25
# i = start # initialization
# while i <= end:
#     print(f"i is {i}")
#     i += step
# # 
# i = 200
# while True:
#     print("i is",i) # this line will always happen at least once
#     # could add more lines which will run at least once
#     if i > 28: # similar to while i <= 28:
#         break # with break with break out of loop
#     i += 2
# # above is simulating do while looping functionality 
# print(i)
# 
# i = 20
# active = True
# is_raining = True
# while active and is_raining:
#     print(f"Doing stuff with {i}")
#     i += 3
#     # TODO update weather conditions
#     if i > 30:
#         active = False
# #     
# while True:
#     res = input("Enter number or q to quit ")
# #     if res.lower().startswith("q"): # more lenient any word starting with Q or q will work to quit
#     if res == "q":
#         print("No more calculations today")
#         break
#     elif res == "a": # TODO check if if the input is text
#         print("I can't cube a letter a")
#         continue # means we are not going to try to convert "a" to float
#     num = float(res)
#     cube = num**3
#     cube = round(cube, 2) # 2 digits after comma
#     print(f"My calculator says cube of {num} is {cube}")
# # 
print("All done whew!")

# outer_flag = True
# inner_flag = True
# i = 10
# while outer_flag:
#     print(i)
#     while inner_flag:
#         res = input("Enter q to quit")
#         if res == 'q':
#             print("got q lets break from inside")
#             break
#     i += 1
#     if i > 14:
#         print("outer break about to happen")
#         break
# # 
# # 
# #     
# #

i = 5
while i < 10:
    print(i)
    i += 1
    if i % 2 == 0:
        print("Even number", i)
        continue # we skip the following loop instructions
    print("Doing something with odd number", i)