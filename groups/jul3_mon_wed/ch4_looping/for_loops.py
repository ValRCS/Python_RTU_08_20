# for loop
# for loops are meant for definite iteration/looping
# while loops are meant for indefinite- we do not know when to quit ahead to time

# with for loop we go over each element of some iterable
# there are many types of iterables
for c in "Valdis": # string is iterable collection of mini single char strings
    print("Char ", c, type(c), ord(c))
    
for number in range(5): # range starts with 0 by default
    # goes until end - 1, so 5 is NOT included
    print("Number is", number)
    
# with range I can specify start and end
for n in range(10,15): # 15 is NOT included
    print("n is ", n)
    
# i can also specify step
for n in range(100, 110+1, 2):
    print("n is now", n)
    
# in python we use enumerate in for loop when we need index or enumaration
name = "Valdis"
for i, c in enumerate(name): # by default enumerate starts with 0
    print(f"index {i} letter {c} unicode {ord(c)}")
    
# i can set enumerate to start at any number
for i, c in enumerate(name, start=1_000): # by default enumerate starts with 0
    print(f"index {i} letter {c} unicode {ord(c)}")
    
# there are many more iterables that for loop can go over
# lists, sets, tuples, dictionary.items and many other custome defined

# finally for loop ALSO has else
# as well as break and continue
for n in range(10):
    print("n is ", n)
    response = input("Want to quit?(y/n)")
    if response == "y":
        print("early exit")
        break
    else: # attached to if # it is redundant since if had break
        print("Doing normal stuff")
else: # only runs if for loop quit normally
    print("normal exit without break")

#outside for loop
print("normal end of program")

# we can do negative step
for n in range(100,90, -4):
    print("n is ", n)
    
# why is range not actually array
# because if you have huuuge range
# you do not want the whole range in memory
