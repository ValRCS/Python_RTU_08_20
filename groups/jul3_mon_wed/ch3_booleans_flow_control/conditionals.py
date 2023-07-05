# conditional execution
# flow control
# if True: # in Python : will lead to indentation next line
#     # this starts the code block
#     # that runs when if statement is True
#     print("Fly to Mars")
#     # we do more stuff
# # back to normal flow
# print("We are outside if")
# usually we will have some variable inside our if
a = 2
b = 4
if a < b:
    # inside if block
    print("a < b", a < b)
    print(a, b)
# back to normal code block
print("Normal flow")
# if we want to do one or another we use if else
# we will only take one path
if a > b:
    print(" a is larger than b")
else: # essentially a <= b
    print("so a is either equal or less than b")
    
# we also have elif for more branching
number = 10_000 # _ is purely cosmetic for numbers
number = -9_000
number = 42
answer = 42
# only one out of three paths will be executed
if number > answer:
    print(f"Hmm {number} is larger than {answer}")
    # i could do more stuff here when number < answer
elif number < answer:
    print(f"Hmm {number} is less than {answer}")
else: # only case number == answer remains
    print(f"Hmm {number} is equal to {answer}")
    
# we can do nested ifs

if number > 40:
    if number < 50:
        print(f"so {number} is over 40 but less than 50")
    else:
        print(f"so {number} is 50 or more")
else: # number <= 40
    if number < 20:
        print(f"so {number} is less than 20")
    else:
        print(f"so {number} is under 40 but more than 20 or equal to 20")   


# i would rewrite more flatly
if 40 < number < 50:
    print(f"so {number} is over 40 but less than 50")
elif number >= 50:    
    print(f"so {number} is 50 or more")
else: # number <= 40
    print(f"so {number} is 40 or less")
    
# or even
if number >= 50:
    print(f"so {number} is 50 or more")
elif number <= 40:
    print(f"so {number} is 40 or less")
else: # so number has to be over 40 but less than 50
    print(f"so {number} is over 40 but less than 50")
    
# since Python 3.10 we also have match case which can be good replacement
# for longer if elif elif elif chains
letter = "c"
letter = 'd'
match letter:
    case 'a':
        print("Got a")
        # no need for break here
    case 'c':
        print("Got c")
    # default when no match
    case _:
        print(f"Got something in {letter}")
        
# match case can also match on particular types and number of values in them

