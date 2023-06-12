# break lets us quit loops early
i = 9_000
while True:
    print("Will run at least once i is", i) # will always print at least once
    if i > 5:
        break # exits Loop and gets to next line after loop
    i += 1 # crucial we do change i else we will be stuck forever
print("Whew we are out of loop an i is", i)

# in effect we have created a do while loop
# do while loops run the loop at least once

# total = 0
# while True:
#     print(f"Total so far {total}")
#     number = input("Enter a number or Q to quit")
#     if number == "Q":
#         print("Done working time to quit")
#         break
#     number = int(number)
#     total += number
# # out of loop
# print(f"Total finally is {total}")

# we can combine while with try except to ask for specific data

while True:
    try:
        whole_num = int(input("Please enter a whole number "))
        # if there is error we will skip to except part
        print(f"Cool you entered correct {whole_num}")
        print("Time to break out of input processing loop")
        # i could process more inputs in the same loop or different ones
        break
    except ValueError:
        print("Sorry you need to enter a whole number")
        print("For example -5 or 9_000 or 0")
        
print("After input processing whole_num is", whole_num)

# we could add this while inside another while

total = 0
is_job_done = False
while not is_job_done:
    print("Total is", total)
    while True:
        try:
            whole_num = int(input("Please enter a whole number "))
            # if there is error we will skip to except part
            print(f"Cool you entered correct {whole_num}")
            print("Time to break out of input processing loop")
            # i could process more inputs in the same loop or different ones
            break # will break out of inner loop only!
        except ValueError:
            print("Sorry you need to enter a whole number")
            print("For example -5 or 9_000 or 0")
    total += whole_num
    print(f"Total so far is {total}")
    user_input = input("Do you want to continue Y/N?")
    if user_input == "Y":
        print("We want to continue")
        continue # goes immediately to start of outer loop
        # in this case continue is not strictly necessary
        # because we have nothing after else anyways
    else: # everything that is not Y
        print("Time to quit")
        # break # exit from outer loop as well
        # alternative to break would be
        is_job_done = True # now we go back to beginning
        # continue would be ok but not needed
    # maybe we want to do some cleanup for outer loop
    # here after each loop
# after all loops are finished
print("Finally the big total is", total)


