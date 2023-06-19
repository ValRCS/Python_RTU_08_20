# we can write functions that can handle multiple arguments

def add_everything(*args, debug=False):
    """Adds all arguments and returns the result"""
    if debug:
        print(args)
    result = 0
    for arg in args:
        result += arg
    return result

# let's call it
print(add_everything())
print(add_everything(1))
print(add_everything(1, 2))
print(add_everything(1, 2, 3, 4, 5))

# same principle is used in print function
print("abc", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, sep="|", end="***\n")	
# i passed in 11 arguments and it worked
#also i used named arguments sep and end

# so i can pass debug=True to my function
print(add_everything(1, 2, 3, 4, 5, debug=True))
# technically I could skip the name of the argument
print(add_everything(1, 2, 3, 4, 5, True)) 
# but it is not as readable
# booleans should be passed as named arguments
# just imagine if you had a function with 10 arguments
# and 6 of them are booleans

# because for named arguments order does not matter
print(1, 2, 3, end="**\n", sep="||") 
# in above example i mixed end and sep arguments but it will work

# finally we could have a function which takes specific arguments
# then variable arguments and then default arguments
def add_everything2(a, b, *args, debug=False):
    """Adds all arguments and returns the result"""
    if debug:
        print(args)
    result = a + b # a and b have to be supplied - required arguments
    for arg in args:
        result += arg
    return result

# let's call it
print(add_everything2(10, 2, 30, 4, 5, debug=True))
# so 10 and 2 are required arguments
# 30, 4, 5 are variable arguments
# debug is a default argument - named argument