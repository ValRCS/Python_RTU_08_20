# using our input_error_checking.py example
# i an make a program that will sum numbers forever or until user quits
total = 0

while True:
    print("Please enter a valid number or press Enter or type Q to quit")
    num = input("->")
    # num is string here
    # I will check if it is empty ""
    if num == "" or num == "Q":
        print("okay you want to quit alright")
        break
    # now we will try
    try:
        num = float(num) # -> is not required
        # point is that float will work or we go to except section
        # here we are guaranteed that float worked!
        print("Cool you entered a float!", num)
    except ValueError:
        print("Sorry you did not enter a valid number")
        continue # we want to request input again!
    # here we know two thing
    # we have a valid number and user wants to continue
    total += num
    print("Running total is ", total)
    
print("All finished")
print(f"Last number will be empty <{num}>")
print(f"Your total is {total:.4f}") # displayed with up to 4 digits after comma

    