# cube calculator app
# text = input("Enter a number")
# # try:
# #     print(f"Will try to convert {text} to number")
# #     num = 10
# #     num = int(text)
# #     # if we get Value Error in this block
# #     # the part below will run
# # except ValueError: # will run if we get ValueError
# #     print(f"That {text} was not an integer!)")
# #     # error handling block continues
# print("program continues")

print("Welcome to Cube App!")
print("*"*40)
while True:
    txt = input("Please enter a number to cube or q to quit")
    if txt == "q":
        print("quitting app")
        break
    try:
        num = float(txt)
        # if converstion to float will fail
    except ValueError:
        print(f"{txt} was not a valid float")
        print("Please try again")
        continue # will return to line 16
    # here we know that num is a valid float
    cube = num**3
    print(f"{num} cubed is {cube}")
    
print("Cleanup of the application")
    