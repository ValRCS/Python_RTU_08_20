# for loops are for iterating a collection of something
# in other words for loops are for definite iteration
# we have some collection of items and we want to
# iterate over them
print("Will start a for loop")
# so range by default starts at 0 and goes until number-1 (exclusive of number)
for n in range(10): # range gives us numbers on demand like a factory
    print(f"n is now {n}")
    # i could create a variable as well
    square = n**2 # we would create this variable
    # if we need to do anything else besides printing
    # also readability reasons
    print(f"n squared is {n**2} same as {square}")
    # still inside for loop
    print("Going back to beginning of for loop")
# outside loop
print(f"After for loop is over n is {n}")

# what if we do not care about the numbers at all
# but just want to do something many times
# then use _ as indicator that variable is not important
# in Python we use _ to indicate variable that is needed for syntax
# but not used practically

# so a repeat functionality
# do something specific number of times
for _ in range(3): # _ will take on 0,1,2 but we don't care here
    print("Hello Rīga!")
    # open web page
    # check weather etc
    # maybe sleep a bit
    
name = "Valdis"
for c in name: # c is arbitrary, could be n, t, i or letter or whatever
    print(f"Working on letter {c}")
    print("Unicode code of this letter is", ord(c))
    
# there are more complex data structures that also offer iteration with for loops
# lists, dictionaries, sets and so on

# lets look at range in more detail
# default for range start is 0
# if we supply two parameters
# then first indicates start
for n in range(-10,15): # so start at 10 and go until 14 included
    # cosmetic changes for print function
    # we want to print ,space instead of newline
    end_char = ", "
    if n == 14:
        end_char = "\n"
    print("n is ", n, end=end_char) # end="," print will end with commA
    # instead of newline
print("\nAll done") # we had no newlines previously

# range also has step

for n in range(100,110,5): # so 3rd number is step
    print("n is ",n)
print("outside loop", n)

# full documentation for range
# https://docs.python.org/3/library/stdtypes.html#range

# names of these variables are arbitray, use your own
start = -2_000
stop = 5_000 
step = 700
# again stop is not included if it is reached exactly
for n in range(start,stop,step):
    print("n is now", n)
# all done with loop
print("after loop", n)

# steps can be negative
for n in range(10,8,-1): # again stop is not included
    print(n)
    
# limitation for range step has to be exact
# there are other range objects from libraries such as NumPY
# which have partial steps
# so if we need partial step we can use while loop instead

# we can count/enumerate things while looping
# by default enumerate starts with 0
for i, c in enumerate(name):
    print(f"Letter No. {i} is {c}")

# we can change start of enumerate to any number
for i, c in enumerate(name, start=101):
    print(f"Letter No. {i} is {c}")
    
for n in range(12):
    # we could use if inside
    if n % 2 == 0: # reminder when divided by 2
        print(f"{n} is even!")
    else:
        print(f"{n} is odd!")
        
        
# we can quit for loop earlier just like while loop
for n in range(1_000_000):
    print("big number", n)
    if n > 7:
        print("Sorry I am too tired")
        break # breaks to next line after for loop
    else:
        print("will jump to start of for loop")
        continue # jumps to start of the loop
    #unreachable code here due to break and continue
    print("This part will never run") # good IDE will pick up on this
    print("Still doing stuff with", n)
print("Outside for loop")

# my_data in a list - more on list later
my_numbers = [1,2,6,1,6,32,205]
for number in my_numbers:
    print("Doing work on certain item individually", number)

# lesser known feature of for loops(also while loops)
# there is optional else to for (and while loops)
# idea else will run if there is no break in for loop
for n in range(5):
    print("Minding my own business with number", n)
    user_input = input("Do you want to continue (y/n)?")
    if user_input == 'n':
        print("okay quitting time")
        break
    else: # attached to if runs if we enter y (or anything else actually)
        print(f"Entered symbol {user_input}")
        print("continuing normally")
else: # attached to for runs only if for loop above finished normally
    print("Whew everything worked out normally")
    
# outside
print("End of program in any case")