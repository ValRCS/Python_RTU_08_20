# for loops in Python
# philosophically
# for loops in Python are used for definite iteration
# we iterate over some collection of known value - usually
# while while loops are generally for indefinite iteration
# with while loops we are not sure when we will finish

# so for loops iterate/loop over a collection of some sort
# this collection has to be iterable (essential it has to have a next() method)

# in practice let's start with a collection we already know - string
name = "Valdis"
for c in name: # c could be anything, char, letter, t, n etc, 
    print("Letter", c)
# note c remains alive even here and will have last value from iterator

# if we want to go through some numbers
# we will want to use a range most likely
# range in Python 3 is sort of like half-made array/list of numbers
# it gives numbers on demand

for n in range(5):
    print("n is ", n)
    
# we can also specify start(inclusive) and end(not inclusive)

for n in range(100, 105): # so 105 is NOT included
    print("n is now", n)
    
# we can also specify step
start = 100
stop = 120

step = 5
for n in range(start, stop, step): # will not include stop
    print("n is now", n)
    
# i can includ stop with + 1
# stop_inclusive = stop + 1
for n in range(start, stop+1, step): # will include stop
    print("n is now", n)
    
# for counting things in for loops we use enumerate
# enumerate starts from 0 by default
for i, c in enumerate(name):
    print(f"Letter no:{i} is {c} - unicode: {ord(c)}")
    
# i can change start of enumerate - less used
for i, c in enumerate(name, start=-1_000):
    print(f"Letter no:{i} is {c} - unicode: {ord(c)}")
    
# we can go down of course
for n in range(50, 30, -4):
    print("n is now", n)
    
# finally for loops can use usual break continue and also that strange else

for n in range(10):
    print("n is now", n)
    answer = input("Do you want to quit(y/n)?")
    if answer == 'y' or answer == "Y": # could use lower or startswith
        print("early quittting time")
        break
    else: # attached to if
        print("continue normally")
        # could use continue here but no need
else: # attached to for
    print("no breaks happened")
    
print("Time to solve some exercises!")

    
