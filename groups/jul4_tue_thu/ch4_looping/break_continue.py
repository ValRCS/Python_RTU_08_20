# break and continue
# i = 10
i = 9_000 
while True:
    print("oh i is now", i)
    if i > 20:
        print("Time to break freeee", i)
        break # goes to next line after loop
    i += 2 # break will skip this
# break goes here
print("outside")
# so using break we can implement a do while loop
# do while loops do something at least once
# so called shoot first and ask questions later

# there is also lesser used continue
# continue goes immediately to the start of the loop

i = 10
turbo_threshold = 15
turbo_speed = 3
while i < 20:
    print("again i is ", i)
    if i == turbo_threshold:
        print("Going warp speed when i is at threshold", i)
        i += turbo_speed
        continue # so we skip rest of the loop in this case
    # here we could have done without continue just use else
    # do some stuff when not at threshold
    i += 1 # normal speed
# outside

# finally there is a strange else attached to while loop (not if!)
# used rarely can help avoid using some extra flag variables
i = 0
while i < 5:
    print("just a normal i",i)
    if i == 3:
        print("early break at", i)
        break # will skip else attached to while
    i += 1
else: # will run if loop exited normally
    print("Whew loop run normally")
    
print("outside loop")
