# while loops
print("How are you?")
print("How are you?")
print("How are you?")
# how about 100 times, how about 1 million times?
# copy and paste are okay only for 2nd time
# basic rule if you are copy and pasting somethign 3 or more times, think about loops
# most infamous loop
# while condition before : is True we will continue looping
# infinite loop here
# while True:
#     # while loop block starts here
#     print("I am doing great!")
# outside while loop
print("I should be done...")

# philosophy of while loops
# they are for looping when we do not know when we are going to end
# there are other loops for definite looping
# however we can use while loops for everything

# so i want to do something a few times let's say 5 times
i = 0 # iterator variable, could be it, n, t, anything really
while i < 5: # so indentation serves as a start of a block
    print("I am doing great")
    print("My number is", i)
    # while block continues
    # we will want to adjust our iterator variable
    i+=1 # same as i = i + 1, Python does not have i++
# we are outside while block
print("We are outside the while loop and our number is", i)

# we can add delays to our programs with time.sleep(seconds) function
import time  # usually we would import at the beginning of program
# time.sleep(5)

floor = -10
# bottom_floor = -2
bottom_floor = -1
fall_speed = 5
delay = 0.1

while floor > bottom_floor:
    print(f"Falling down to floor {bottom_floor}")
    print(f"Currently I am at floor {floor}")
    floor -= fall_speed # floor = floor - fall_speed
    print(f"First we sleep a bit for {delay} seconds")
    time.sleep(delay)
    
print(f"We are at floor {floor}")