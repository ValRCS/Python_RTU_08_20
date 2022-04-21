# # # https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments
# # # https://realpython.com/python-kwargs-and-args/

print(min(1,2,-6,6,20,30))
print(max(3,7,2))

def adder(*args): # so a list of arguments of any length
    print(f"My adder with {len(args)} arguments, args is {type(args)}")
    for arg in args:
        print(arg)

adder() # will work even with no arguments
adder(5, 2, "Valdis")
adder(5, 2, "Valdis", "Līga", 1222, None, True, 3.15)

def summator(*args, verbose=False):  # so verbose is a named argument
    if verbose:
        print(f"got {args}")
    result = sum(args)
    if verbose:
        print("result is", result)
    return result

my_result = summator(23,3,234,2235)  # notice this is not a list
print(my_result)
another_result = summator(5,2,6,20, verbose=True)
print(another_result)
# another_sum = summator(23,3,234,2235,1000)
# print(another_sum)


def mult(first: int, *args: list[int], multiplier=1): #so positional arguments have to come first, named afterwards
    result = multiplier * first
    for arg in args:
        # could add an if here to check data type if we are not sure of numbers
        result *= arg
    return result 
    
    
print("Checking Mult")
print(mult(56)) # i need to enter at least one argument since first is positional - ie required
print(mult(2, 10, 5))
# # print(mult(2, 10, 5, -3.6))
print(mult(2, 10, 5, -3.6, multiplier=1000))

# # # print(mult(2, 10, 5, -3.6, multiplier=0))
print(mult(35, multiplier=0.5))


# # # # print("A", 5, mult(3, 6))

# # # # TODO iespēja padot arī **kwargs after we learn about dictionaries

# def fun(*argv, required, my_default="Given as default"):
#     # so what will be the minimu arguments that I need to add?
#     print(f"got {len(argv)} positional arguments")
#     for arg in argv:
#         print("arg:", arg)
#     print(f"Required arg is {required}")
#     print(f"My default is {my_default}")

# fun(required="hmm") # so hmm will be assigned to required
# fun(1,2, "oho", required="hmm") # so hmm will be assigned to required
# fun(1,2, "oho", required="hmm", my_default="changed default") # so hmm will be assigned to required
