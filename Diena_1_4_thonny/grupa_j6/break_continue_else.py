# break and continue (and else) in loops

# it = 100
it = 10_000 
while True:
    print(f"It is {it}")
    if it > 120:
        print("We are done here time to break free!")
        break # immediately goes to line after while loop
    it += 5
    
# this is where break goes
print("We are free already, but our iterator is now", it)

# in effect we have created so called do while loop
# Python does not have do while syntax but the above is very similar to do while
# these do while type loops do something AT LEAST ONCE and only then check condition
# so shoot first and ask questions later

# we can combine break with regular while condition
# so we have two ways of exiting the next loop
# total = 0
# counter = 0
# while total < 1_000:
#     number = int(input("Enter an integer please! "))
#     total += number
#     print(f"Total is {total} and entered number is {number}")
#     if counter > 5:
#         print("Sorry only 5 entries allowed")
#         print("Counter", counter)
#         break
#     counter += 1
    # i could add other break conditions if I want

# so our loop will continue as long as total stays under 1k
# and also while counter is 5 or less
# print("We are out of loop")
# print("Counter is", counter)
# print("Total is", total)

# we also have continue instruction which goes back to the start of the loop
i = 100
while i < 110:
    print("i is ", i)
    i += 1 # careful here
    if i == 103:
        print("Going back to start immediately")
        continue # goes back to start of while loop
    print("Things we do when i is not 103", i)
    # could do more stuff for when i is not 103
    # again we could have done this with else
    
# finally we have one more construction even more rare than continue
# else can be attached to while
# it means while loop finished without break

i = 10
while i < 15:
    print("i is", i)
    i += 1
    user_input = input("Do you want to continue (y/n)?")
    if user_input == "n":
        print("break time")
        break
    else: # attached to if, optional
        print("We are continuing normally")
else: # we enter this when while loop finished normally
    print("Finished normally")
print("Always prints")