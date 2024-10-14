# there is also a continue instruction
# continue goes to start of loop immediately

i = 0
while i < 10:
    print("inside loop and i is", i)
    i += 1
    if i % 3 == 0: # divides with 3
        print(f"{i} divides with 3 with no reminder")
#         continue # we go back to start of loop to check i<10 AGAIN
    else: # often we can do the same thing as continue with else
    # here all other cases when i does not divide with 3
        print(f"i is not evenly divisible by 3. I is", i)
        
    # continue we could use if there are a lot of extra work to be done
    # and we do not want to put that extra work under else
    # mostly because of looks

print("Loop finished i is", i)
        