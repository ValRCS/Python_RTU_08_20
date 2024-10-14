# philosophically while loops are best
# when we do not know exactly how many iterations/cycles/loops we have
# we have some condition to check to break/exit

# often we have some sort of collection that we want to go through
# for those we use for loops with iterable
# iterable some sort of collection that can be looped 
# simplest for loop would be to print some numbers using range iterable

# let's print 5 numbers
for number in range(5):
    print(f"Number is {number}")
    # still inside loop
# loop is finished
print("at the end number is", number)

# we only know one another iterable at this moment - string
# string is sequence of single letter strings
name = "Valdis"
for char in name: # char could be any other name for variable, such as c etc
    print("This char is", char)
# outside loop
print("last char is", char)

# okay back to numbers
# what if we want to start at another number not 0?
# simply change range to fuller syntax
# range(start, end) # end is not included
# so 10 to 15 included what do we write?
start = 10
end = 12
for n in range(start, end+1): # I add + 1 if I need the end(inclusive)
    print("n is",n)
    
# how about step?
# no problem
# full range syntax is range(start, end, step) # again end is not inclusive
# step has to be integer

# so from 100 to 110 with step 2
for n in range(100, 110+1, 2):
    print("n is now", n)
    
print("outside n is", n)
    
    
# how about counting down? no problem
# we use negative step and our start should be more than end
# so our start is 9
# our end is 0 (not included)
# and we have negative step of -1
for floor in range(9, 0, -1): #0 is not included so we will stop at 1
    # if we wanted to stop at 0 then second value should be -1
    print("Going down  floor is", floor)
    
print("We stopped at floor", floor)

# we can use for loops with if elif and else
# also we can use break (and continue but less often)

for n in range(5):
    print(n)
    if n > 2:
        print("Oh no! n is over 2, quitting time!", n)
        break
    print("Still working on ", n) # this will not be seen on 3
    
print("Outside is nice and n is", n)

# we can use if elif else

for n in range(10):
    # let's save/cache our reminder - micro optimization
    reminder = n % 3
    if reminder == 0:
        print("Cool n divides with no reminder with 3", n)
    elif reminder == 1:
        print(f"Okay reminder is {reminder} after division by 3", n)
    else: # must be 2 for reminder nothign else
        print(f"So only {reminder} remains as reminder for", n)

print("Outside n is", n)
    


    
