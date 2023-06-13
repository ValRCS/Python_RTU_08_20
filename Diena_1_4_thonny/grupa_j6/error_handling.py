# error handling with loops
# users can end up entering all kind of weirdness

while True:
    try:
        user_input = input("Please enter a whole integer ")
        number = int(user_input) # possible error here jumps to except then
        print("Cool you entered", number)
        # we only get to this break if we did not get any errors in previous
        # 3 lines
        break
    except ValueError: # it is recommend that specific Errors are handled
        print(f"Sorry {user_input} is not a valid integer!")
    # we could add other error types here
        
# now we can do whatever we want with our number - it is guaranteed to be integer
print("normal work with integer", number)

# we can nest our loops

total = 0
while total < 1_000_000:
    # entering inner loop for input validation
    while True:
        try:
            user_input = input("Please enter a whole integer ")
            number = int(user_input) # possible error here jumps to except then
            # we could do it for floats as well, or some other types
            # we could ask for more inputs here as well
            print("Cool you entered", number)
            # we only get to this break if we did not get any errors in previous
            # 3 lines
            break
        except ValueError: # it is recommend that specific Errors are handled
            print(f"Sorry {user_input} is not a valid integer!")
    # we are out of inner loop with guaranteed integer
    total += number
    print("Total is ", total)
    ready_to_quit = input("Do you want to quit? (y/n)")
    if ready_to_quit == "y":
        print("I am tired ready to go home")
        break
    # now we go back to start of outer loop here

print("After work our total collected is", total)