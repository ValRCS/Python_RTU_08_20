# Python offer try except construction for handling errors
# num = 0
# try:
#     num = int(input("Enter a number please "))
#     # having error will cause next line to be skipped
#     print("Cool a int number", num)
# except ValueError as e: #typically we want to catch specific errors
#     print("Oops you did not enter a valid integer", e)
#     # as e is optional , and e is just a variable name, could err, error etc
    
print("outside")

# we can combine try except with while loop to ensure valid input

while True:
    try:
        number = int(input("Please enter an integer "))
        # we could add more conversion attempts here
        # if there are any errors we will skip the next lines
        # and jump immediately to except
        print("All good with", number)
        break # so we break out of infinite loop only when no errors
    except ValueError:
        print("Please enter a valid integer")
        # continue could be used here but not needed
        
print("i am guaranteed that number is integer here")
print(number **2)
        