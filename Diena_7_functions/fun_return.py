# The return statement returns with a value from a function.
#  return without an expression argument returns None.
# Falling off the end of a function also returns None.

def add(a=50, b=10):
    inner_result = a+b
    # print(a+b)  # print ir tā saucamais side-effects, print ir pasmags
    # how do we save the result?
    # return a+b
    # do more stuff with inner_result
    return inner_result


def mult(a, b):
    return a*b


result = add(5, 6)
print(result)
print(mult(10, 2.5))
print(mult(add(3, 5), add(2, 1)))
calc_result = add(mult(2, 0), mult(5, 4))
print(calc_result)
# print(a, b) are not available outside the functions in this case

# since i added default b value for function add I can call it
print(add(25))
print(add())
print(add(b=35))
print(add(b=35, a=100))
print(add())


def greeter(first, last, is_upper=False):
    if is_upper:
        print(f"Hello {first.upper()} {last.upper()}")
    else:
        print(f"Hello {first} {last}")


greeter("Valdis", "Saulespurēns")
greeter("Jānis", "Bērziņš", is_upper=True)
