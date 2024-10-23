# sometimes we want to write functions with multiple arguments
# but we don't know how many arguments we will need
# similar to how print() can take any number of arguments
# we could pass in a list
# or we could use *args
# with args, we can pass in any number of arguments

def add(*args):
    total = 0
    for num in args:
        total += num
    return total

result = add(1, 2, 3, 4, 5) # note how I passed values in without a list
print(result)

# we can also pass in a list
def add_list(argument_list):
    total = 0
    for num in argument_list:
        total += num
    return total

result = add_list([1, 2, 3, 4, 5]) # note I had to use brackets to pass in a list
print("Add list", result)

# i can add args then add default values
def add_default(*args, default=0, verbose=False):
    total = default
    if verbose:
        print("Default is", default)
        print("Args are", args)
        print(f"Total number of args is {len(args)}")
    for num in args:
        total += num
    if verbose:
        print("Total is", total)
    return total

result = add_default(1, 2, 3, 4, 5, default=10) # note I have to specify the default value
print("Add default", result)

# I can use verbose now
result = add_default(1, 2, 3, 4, 5, default=50, verbose=True) # note I have to specify the default value
print("Add default", result)
# boolean values should be passed using keyword arguments
# otherwise if you have multiple boolean arguments, it can be confusing

# let's see an example with multiple arguments and multiple boolean defaults
def add_default_multiple(*args, default=0, verbose=False, debug=False):
    total = default
    if verbose:
        print("Default is", default)
        print("Args are", args)
        print(f"Total number of args is {len(args)}")
    for num in args:
        total += num
    if debug:
        print("Total is", total)
    return total

result = add_default_multiple(1, 2, 3, 4, 5, 
                              default=50, 
                              verbose=True, 
                              debug=True) # note I have to specify the default value

print("Add default multiple", result)