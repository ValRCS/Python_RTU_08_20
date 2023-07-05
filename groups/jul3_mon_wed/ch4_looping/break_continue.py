# break and continue
# i = 10
i = 10_000
while True:
    print("i is", i) # this runs at least once
    if i > 20:
        print("time to break freeeeeee", i)
        break # goes to next line after while loop end
    i += 2
print("Outside loop")
# essentially we have just made a do while loop
# which runs at least one time and only then checks
# so to say 'shoot first and ask questions later'
# we also have less used construction continue - it goes to start of loop immediately

i = 10
while i < 20:
    print("i is", i)
    if i == 15:
        print("Oh special number", i)
        i += 3 # big jump here otherwise continue would be pointless
        continue # goes to start of while loop
    i += 1
    
    
# we also have a strange construction else attached to while loop!
# it works when no break was performed in the loop
i = 0
while i < 5:
    print("normal i", i)
    if i == 3:
        print("quick break", i)
        break # will cause else block not to run
    i += 1
else: # this will run only if no break was encounterd in while loop
    print("While loop run normally")
print("Always runs")