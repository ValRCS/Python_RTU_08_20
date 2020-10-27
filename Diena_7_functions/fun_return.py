# The return statement returns with a value from a function.
#  return without an expression argument returns None.
# Falling off the end of a function also returns None.

def mult(a, b):
    print(f"Look ma I am multiplying {a} with {b} result is {a*b}") # printing is a sideeffect
    return a*b

# mult(5,10)
# mult("Beer ", 3)
# print(mult(7,20))
# result = mult(10,50)
# print(result)


def add(a=50, b=10):
    inner_result = a+b
    print("Result will be", inner_result)  # print ir tā saucamais side-effects, print ir pasmags
    # how do we save the result?
    # return a+b
    # do more stuff with inner_result
    return inner_result

# result = add(5, 6)
# print(result)

# print(add(100)) # this means that a = 100, but b is still 10
# print(add()) # this means that a = 100, but b is still 10
# print("Done adding")

# # print(mult(10, 2.5))
# print(mult(add(3, 5), add(2, 1)))
# calc_result = add(mult(2, 0), mult(5, 4))
# print(calc_result)
# # print(a, b) are not available outside the functions in this case

# # since i added default b value for function add I can call it
# print(add(25))
# print(add())
# print(add(b=35))
# print(add(b=35, a=100))
# print(add())


def greeter(first, last, is_upper=False, add_suffix=""):
    """
    Prints Greeting
    Options -
    is_upper - whether to capitalize
    add_suffix - what suffix to add
    """
    if is_upper:
        print(f"Hello {first.upper()} {last.upper()}{add_suffix}")
    else:
        print(f"Hello {first} {last}{add_suffix}")


greeter("Valdis", "Saulespurēns")
greeter("Jānis", "Bērziņš", is_upper=True) # is_upper is not necessary but nice to include for clarity
greeter("Laine", " ", True) # is_upper is not necessary but nice to include for clarity
greeter("Svetlana", "Tomane", add_suffix=" sveicam kursā!") # i can skip is_upper since i name add_suffix
greeter("Gunta", "Berziņa", None, None) 
