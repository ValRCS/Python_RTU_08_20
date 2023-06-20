# we can provide default values for function arguments

# default values should be something that makes sense
def add(a, b=0, debug=False):
    # debug is just a name of variable - nothing special, could be anything
    if debug:
        print(f"Adding {a} and {b}")
    return a + b

print(add(2, 3)) # 5
print(add(2)) # 2, so b is optional

# let's test debug
print(add(2, 30, debug=True)) # 32

# if function returns something we can test it with assert
assert add(2, 3) == 5 # will throw AssertionError if False
assert add(2) == 2 # will throw AssertionError if False
# assert add(2, 2) == 5 # will throw AssertionError if False

# finally have variable number of arguments
# we use *args to indicate that we will have variable number of arguments

def add_many(*args):
    # args is a tuple of arguments
    result = 0 # initialize result to 0
    # if no arguments given loop will not run
    for number in args:
        result += number
    return result

print(add_many(2, 3, 4, 5)) # 14
print(add_many(2, 3)) # 5
print(add_many()) # 0

# i can also mix positional arguments with *args
# i can even add named arguments at the end
def add_many_with_positional(a, b, *args, debug=False):
    result = a + b # a and b are positional arguments - required
    for number in args:
        result += number
    if debug:
        print(f"a and b are {a} and {b}")
        print(f"Arguments are {args}")
        print(f"result is {result}")
    return result

print(add_many_with_positional(2, 3, 4, 5)) # 14
# print(add_many_with_positional(2)) # Error - missing b
print(add_many_with_positional(2, 3, 10, -5, debug=True)) # 5

# we can also use **kwargs to indicate that 
# we will have variable number of named arguments
# for that we would need to use dictionary - those are next chapter