# sometimes we want to break out of loop early
# especially forever loops which you might want to finish at some point
# for that we have break instruction which quits the inner loop

counter = 0

while True:
    my_input = input("Do you want to quit? (Y/N)")
    if my_input == "Y": # when we know more about strings we will have more lenient ways of comparing
        print("Let's leave this place!")
        break # this goes to next line after loop block
    print("Loop continues")
    counter += 1 # this is not necessary but we are counting loops here
    print("Counter at", counter)
    # we jump back to start
    
    
# after break we will be here
print("Whew we should be free now")
print(f"Counter is {counter}")