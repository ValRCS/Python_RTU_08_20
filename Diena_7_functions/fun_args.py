# https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments
# https://realpython.com/python-kwargs-and-args/

def adder(*args):
    for arg in args:
        print(arg)


adder(5, 2, "Valdis")
adder(5, 2, "Valdis", "Līga", 1222)


def mult(*args, multiplier=1):
    result = multiplier
    for arg in args:
        result *= arg
    return result


print(mult(2, 10, 5))
print(mult(2, 10, 5, -3.6))
print(mult(2, 10, 5, -3.6, multiplier=1000))
print("A", 5, mult(3, 6))

# TODO iespēja padot arī **kwargs after we learn about dictionaries
