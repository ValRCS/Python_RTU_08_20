# for loops
# for definite looping / iteration

# we have some collection of some items and we want to loop over them
print("Before loop")

for n in range(5): # again indent specifies start of loop block
    print(f"n is {n}")
    # we jump back to next n

# compared to while loop we needed less writing for specific number iterations
# another difference n at the end is 4 not 5
print("WE still have access to n", n)

# so range starts with 0 and goes until the number(NOT INCLUDED) EXCLUSIVE

# we might want to implement repeat functionality
# meaning we do not care about the number at all
# we just want to do some things over and over

for _ in range(4): # so do something 4 times
    # _ means the variable is not important, it is still a regular variable
    print("Hello there")
    print("Where is the food?")
    
# we can iterate/loop over many different collections
# so far we know of range
# there is also string - which is a collection of characters - technically small strings in Python
name = "Valdis 😀 un kaķi"
for c in name:
    # so c is just a variable it gets assigned each letter one by one
    print("Working on character", c)
    print("Its Unicode is", ord(c))
    
print("After loop c is", c)

# let's look at range in more detail
# we have start and stop actually by default start is 0
start = -10
stop = 5
for n in range(start,stop): # so again stop is NOT included, exlusive 
    print(f"n is now {n}")
    # still inside loop

# outside
print("outside")

# finally we have step for the range
start = 100
stop = 110
step = 5
for n in range(start, stop+1, step):
    print(f"n is now {n}")

print("outside n is now", n)

# for range step has to be integer could be negative

for n in range(20, 10-1, -2): # again stop is not included
    print("n is ", n)

print("outside n is", n)

# so range can be negative, but it has to be integer
# there are external libraries such as NumPy that provide fractional steps
# alternative for fractional steps
# use while loop

start = 10
stop = 20
step = 1.5
it = start
while it < stop:
    print("Doing something with", it)
    it += step
    
    
for n in range(10):
    # lets print numbers all in row
    if n < 9:
        print(n, end=",") # default print end is \n - newline, we can supply our own
    else:
        print(n)
        
# sometimes it might be useful to enumerate your items in the collection
for i, c in enumerate(name): # so we have 2nd variable automatically generated
    print(f"Letter No. {i} is {c}")
    
# we can start enumeration from any number
for i, c in enumerate(name, start=101): # so we have 2nd variable automatically generated
    print(f"Letter No. {i} is {c}")
    
    
# for loops have break, continue and else just like while loops

for n in range(10):
    print(n)
    user_input = input("Do you want to quit (y/n)?")
    if user_input == "y":
        print("Alrighty, lets quit this loop")
        break # jumps to 107 - regular block of code
    # just normal loop stuff
    print("Still", n)
else: # part of for loop when no break is called
    print("Loop ended normally")

print("Regular block of code after loop",n)