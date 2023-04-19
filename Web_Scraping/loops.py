# Looping in Python

# We can use loops to repeat some code multiple times

# we will start with while loop

# while loop will repeat code as long as some condition is True

# this will be infinite loop because condition is always True
# to stop it press Ctrl+C
# while True:
#     print("Hello there web scraper! 😅")

# we can use some number as a condition
# this will print Hello there web scraper! 😅 3 times
i = 2
while i < 3:
    # inner block of while loop
    print("Hello there web scraper! 😅")
    print(f"i is {i}")
    i = i + 1 # without this we will get infinite loop
    # we go back to the top of while loop

# we are outside while loop here
print("We are outside while loop")
print(f"i is {i}")

# we can go down to 0
i = 3
while i > 0:
    # inner block of while loop
    print("Taking Floor down! ")
    print(f"i is {i}")
    i = i - 1 # without this we will get infinite loop
    # we go back to the top of while loop

# we can also break out of the loop early

i = 10
while True:
    print("Hello there web scraper! 😅")
    print(f"i is {i}")
    if i > 12:
        # we can use break to exit the loop
        print("Breaking out of the loop")
        break
    i = i + 1 # crucial to avoid infinite loop

print(f"OUTSIDE: i is {i}")

# we can also use continue to skip the rest of the loop

i = 10
while i < 20:
    # print("Hello there web scraper! 😅")
    print(f"i is {i}")
    if i > 12:
        # we can use continue to skip the rest of the loop
        print("Skipping the rest of the loop")
        i = i + 2 # we increment i by 2
        continue # skip the rest of the loop go back to the top
    print("This will only run if i is less than 12")
    i = i + 1 # crucial to avoid infinite loop


    # we can combine while with try except to process user input
    # we will ask user for a number and print it
    # if user enters something that is not a number we will ask again
    # we will use while True loop
    # we will use try except to catch ValueError

while True: # we could use any condition here for example counter < 3
    try:
        text = input("Please enter a whole/integer number ") # no error here
        number = int(text) # possible ValueError here
        print(f"You entered {number}")
        break # we will break out of the loop if we got a number
    except ValueError:
        print(f"That {text} was not a whole number")
        print("Please try again")
        # if we used a counter here we would increment it here

# we can only arrive here if we got a number
print("We got a whole number")
print(f"number is {number}")