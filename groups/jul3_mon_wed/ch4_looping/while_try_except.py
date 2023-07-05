# error handling in Python
# number = 0
# try:
#     number = int(input("Please enter a number"))
#     # except block will run when we encounter specific error
# except ValueError:# usually we want to catch specific number
#     print("There was an error converting input to number")
    

# with this construction the loop will continue
# until user enters a valid integer
while True:
    try:
        number = int(input("Please enter a number"))
        # there is a possibility of int failing with ValueError
        # everything is good so far
        # i am ready to break
        break # this will only occur if no errors!!
    # except block will run when we encounter specific error
    except ValueError:# usually we want to catch specific number
        print("There was an error converting input to number")

# i have guarantee that number will be valid here
print("number is", number)