# now that we know about Booleans True and False
# we might want to use them
# we use Booleans to choose some action(s) conditionally
# if something is True we do it, if False do not
print("Starting our program")
is_late = True
is_late = False # something caused the condition to change

if is_late: # in Python if we see : usually it is followed by indentation
    # we start a new code block inside if
    print("is it late?", is_late)
    print("We do whatever we do when it is late...")
    # block is still active
# here we exit if block
print("This is outside our if, will always happen")

# often we want to choose one of two choices but not both

# is_raining = True
is_raining = False

if is_raining:
    print("Oh it is raining, I should grab the umbrella!")
else: # this means is_raining == False
    print("Nice let's risk it, I will go in shorts and sandals")
# back to normal flow we took ONE of the if else branches

# how about choosing ONE of THREE choices?
# then we use if elif else chain

number = int(input("Enter a number please "))
# I could have used number = int(number) but I am lazy and did it one row

if number > 42:
    print(f"Oh {number} is more than 42")
    print("Aim a bit lower")
    # still in block where number > 42
elif number < 42: # this check will be 2nd to be done after number > 42
    # now we are in the 2nd block
    print(f"Oh {number} is less than 42")
    print("Aim a bit higher")
else: # only one choice remains that number == 42 šeit
    # When you have eliminated the impossible, whatever remains, however improbable, must be the truth
    # - Sherlock Holmes
    print("Wow your number is just like mine!")
    print(f"You entered 42 indeed {number}")
    
# now back to normal program
print("Finishing") # always runs
