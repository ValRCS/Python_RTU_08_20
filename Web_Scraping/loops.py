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
        i += 2 # same as i = i + 2 # we increment i by 2
        continue # skip the rest of the loop go back to the top
    print("This will only run if i is less than 12")
    i += 1 # same as i = i + 1 # crucial to avoid infinite loop


    # we can combine while with try except to process user input
    # we will ask user for a number and print it
    # if user enters something that is not a number we will ask again
    # we will use while True loop
    # we will use try except to catch ValueError

# while True: # we could use any condition here for example counter < 3
#     try:
#         text = input("Please enter a whole/integer number ") # no error here
#         number = int(text) # possible ValueError here
#         print(f"You entered {number}")
#         break # we will break out of the loop if we got a number
#     except ValueError:
#         print(f"That {text} was not a whole number")
#         print("Please try again")
#         # if we used a counter here we would increment it here

# # we can only arrive here if we got a number
# print("We got a whole number")
# print(f"number is {number}")

# philosophically while loop is for indefinite number of iterations
# we use while when we do not know how many times we need to repeat

# when we know exactly how many times we need to repeat we use for loop

# for loop is used to iterate over a sequence or range of numbers or collection

for n in range(5):
    print(n)
    # we could do more stuff here

# we are outside for loop here

# we could loop over string
name = "Valdis S"
for letter in name:
    print(f"Letter is {letter}")

# if we need an index we can use enumerate
for index, letter in enumerate(name):
    print(f"Letter {index} is {letter}")
    # index and letter are just variables we can use any names here
# outside loop
print("We are outside for loop")
print(f"index is {index}")
print(f"letter is {letter}")

# we can also loop over a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in my_list: # this will be sligthy slower than range
    print(f"number is {number}")

print("*" * 20)	
# we can use range with start and stop
for number in range(5, 10): # note that 10 is not included
    print(f"number is {number}")

print("*" * 20)

# we can use range with start, stop and step
for number in range(5, 10, 2): # note that 10 is not included
    print(f"number is {number}")

# we can loop over multiple collections at the same time using zip
# zip will stop when the shortest collection is exhausted
for number, letter in zip(my_list, name):
    print(f"number is {number} and letter is {letter}")

# we can zip multiple collections

# for loops can use break and continue as well

for number in range(10):
    if number > 5:
        print("Breaking out of the loop")
        print(f"breakout number is {number}")
        break
    print(f"number is {number}")

# we can also use continue to skip the rest of the loop
for n in range(10):
    if n % 2 == 0:
        print(f"Skipping even number {n}")
        continue # we could have use else: here
    print(f"n is {n}")  

# we can also use else: with for loop
# else will run only if we did not break out of the loop

for n in range(10):
    if n % 2 == 0:
        print(f"Skipping even number {n}")
        continue # we could have use else: here
    print(f"n is {n}")
    if n == 3:
        print("Breaking out of the loop")
        break # will cause else to not run
else: # this else is for for loop NOT if !!
    print("We did not break out of the loop")
    print(f"n is {n}")


# we can nest loops
# we can use for loop inside while loop
# we can use while loop inside for loop
# we can use for loop inside for loop
# we can use while loop inside while loop

for x in range(3):
    # outer block of for loop
    for y in range(4):
        # inner block of for loop
        print(f"x is {x} and y is {y}")
        print(f"x * y is {x * y}")

# we can use break and continue in nested loops as well
# break will apply to the innermost loop
# thus we need two break statements to break out of both loops