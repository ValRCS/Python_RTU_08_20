## Passing kwargs to function

## we can pass unlimited number of NAMED arguments to a function using kwargs

def fun(**kwargs):
    print(f"got {len(kwargs)} named arguments")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

fun() # no arguments
fun(name="Valdis", age=49, city="Rīga")

# fun(10, 20, 30) # this will not work these are positional arguments

def fun_all(my_default="Given as default", *args, **kwargs):
    print(f"my_default = {my_default}")
    print(f"got {len(args)} positional arguments")
    for arg in args:
        print(arg)
    print(f"got {len(kwargs)} named arguments")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

fun_all(10, 20, 30, name="Valdis", age=49, city="Rīga")
fun_all() # just default
fun_all(33)  # just default is overwritten
fun_all(10, 20, 30, name="Valdis", age=49, city="Rīga")
a = 10