# we could put this in a loop
try:
    # try to do something here
    a = int(input("Try to enter some noninteger"))
    pass
except ValueError as error: # you should not cactch ALL errors only specific ones for your
    # run this code when some error occurs in try block
    print("Error Mr. Robinson!", error)
    # here I would ask the user to enter a again or perphas try to figure some way to get a value
    # really we want to do have a loop here
