# often we want to make sure of input being correct
# we can combine while loop with try except inside it

# let's say we want to get a float for sure out of input

while True:
    print("Please enter a valid number with such as 5 or 3.1415")
    # now we will try
    try:
        num = float(input("->")) # -> is not required
        # point is that float will work or we go to except section
        # here we are guaranteed that float worked!
        print("Cool you entered a float!", num)
        print("Exiting input loop")
        break
    except ValueError:
        print("Sorry you did not enter a valid number")
        # i could use continue here but no need
        
# here I can use num with 100% guarantee that it is a float
print(num, "squared is", num**2)