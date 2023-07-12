# we might want to make functions with default arguments


def eat(food="a sandwich"):
    print("I am eating " + food)
    print(f"I am eating {food}")

eat() # this will work and will eat a sandwich
eat("a burger") # this will eat a burger

# so we should strive to provide sane defaults for our functions

# we can provide default values for multiple arguments
def add(a=0, b=0, debug=False):
    if debug:
        print(f"adding {a} and {b}")
    return a + b

print(add(1, 2)) # 3
print(add(10)) # a will be 10 and b will be 0 so result will be 10

print(add(debug=True, a=1, b=2)) # 3 so order of arguments does not matter
# i myself forget order of sep and end in print function all the time
# so i use sep and end arguments by name
print("a", "b", "c", sep="|", end="***\n")

print(add(debug=True)) # a and b will be 0 so result will be 0

# finally we can have variable number of arguments

def add(*args, debug=False):
    summa = 0 # do not use sum as variable name - it is a built-in function
    for arg in args:
        summa += arg
        if debug:
            print(f"adding {arg} sum is {summa}")
    return summa

print(add(1, 2, 3, 4, 5)) # 15

# compare with add_list
def add_list(numbers):
    summa = 0
    for number in numbers:
        summa += number
    return summa

print(add_list([1, 2, 3, 4, 5])) # 15    

# i can have a function which has positional, variable an default arguments
def mega_add(a, b=0, *args, debug=False):
    summa = a + b
    for arg in args:
        summa += arg
        if debug:
            print(f"adding {arg} sum is {summa}")
    return summa

print(mega_add(1, 2, 3, 4, 5)) # 15
print(mega_add(100))
print(mega_add(100,22))
print(mega_add(100,22,33))

# finally we can have unroll a list into arguments
numbers = [1, 2, 3, 4, 5]
print(*numbers, sep=",") # I passed valued one by one
# above is same as print(1, 2, 3, 4, 5, sep=",")
# compare with normal print where I give whole list
print(numbers) # [1, 2, 3, 4, 5]

# let's make a function that returns 3 values
def get_user():
    return "John", "Doe", "Golf", 42

# i can assign the result to a tuple
_, _, _, age = get_user() # i am not interested in first two values
print(age) # 42
# even better I can just get tail
*_, age = get_user()
print(age) # 42
# _ will be a list
print(_) # ['John', 'Doe', 'Golf']
