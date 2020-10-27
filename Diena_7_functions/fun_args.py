# https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments
# https://realpython.com/python-kwargs-and-args/

# print(min(1,2,-6,6,20,30))

def adder(*args): # so a list of arguments of any length
    print(f"My adder with {len(args)} arguments")
    for arg in args:
        print(arg)

# adder()
# adder(5, 2, "Valdis")
# adder(5, 2, "Valdis", "Līga", 1222)


def mult(*args, multiplier=1):
    result = multiplier
    for arg in args:
        # could add an if here to check data type if we are not sure of numbers
        result *= arg
    return result


print(mult(2, 10, 5))
print(mult(2, 10, 5, -3.6))
print(mult(2, 10, 5, -3.6, multiplier=1000))
print(mult(2, 10, 5, -3.6, multiplier=0))


# print("A", 5, mult(3, 6))

# TODO iespēja padot arī **kwargs after we learn about dictionaries
