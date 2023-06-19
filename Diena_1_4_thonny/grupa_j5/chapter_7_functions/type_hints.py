# Python provides a way to add type hints to function arguments and return values.

# let's create a simple add function
def add(a: int, b: int) -> int:
    """Adds two numbers and returns the result"""	
    return a + b

# let's call it
print(add(1, 2))

# how about floats?
print(add(1.5, 2.5))

# how about strings?
print(add("abc", "def"))

# how about lists?
print(add([1, 2, 3], [4, 5, 6]))

# again so the code works but the type hints are wrong 
# you would need code linting to catch this

# code linting is a process of running a program that checks the code for errors

# in larger projects it is a good idea to use type hints

# in larger projects it is a good idea to run code linting - PyLint, Flake8, etc.