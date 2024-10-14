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

# there is so called do while loop i some languages
# i call it "Shoot first and ask questions later"
# we do something at least ONCE only then we might possibly leave

i = 8000
while True:
    print("Doing something important")
    print(f"i is {i}")
    if i > 5:
        print("Quitting time! i is", i)
        break
    i+=1
    
# what will i be at the end?
print("i is", i)