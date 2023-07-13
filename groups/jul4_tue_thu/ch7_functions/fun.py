# let's talk about functions in Python

# so what is a function after all?
# it is a way to group together some code that we can reuse
# ideally we want to have functions that do one thing and do it well
# so called ideal functions are short and do one thing
# in practice we will often have functions that do more than one thing

# so what do functions bring to the table?
# 1. Reusability - we can reuse our code
# 2. Readability - we can give our code meaningful names, just like with good variable names
# 3. Testability - we can test our functions separately from the rest of the code
# 4. Modularity - we can separate our code into modules and then import them - divide and conquer
# 5. Extensibility - we can add new functionality to our code without breaking the old code
# 6. Maintainability - we can maintain our code more easily
# 7. DRY - Don't Repeat Yourself - we can avoid repeating ourselves - just see no. 1
# 8. Abstraction - we can hide some of the complexity of our code - we humans can only keep so much in our heads

# we have already been using plenty of functions
# print() is a function
# input() is a function
# len() is a function
# type() is a function
# range() is a function
# list() is a function
# list of all built-in functions https://docs.python.org/3/library/functions.html

# let's make our own function
# so let's say I want to drink a beer
# to do so I need to go to the shop, buy a beer, open it and drink it
# so let's make a function that does that
# we will call it drink_beer
# we will not give it any parameters - for now

# let's start with do absolutely nothing function - so called stub function
def do_nothing():
    # TODO implement this function
    pass # pass is a keyword that does nothing - we need it to have a valid function
# we would use this when we know we need a function but we don't know what it should do yet

def drink_beer(): # so after : we need to indent our code
    print("Going to the shop") # arguable whether going to the shop is part of drinking a beer
    print("Buying a beer")
    print("Opening the beer")
    print("Drinking the beer")
    # recycle the bottle
    print("Recycling the bottle")

# so to use a function I need to call it
drink_beer() # so I call it by writing its name followed by ()

# so let's say I want to drink 3 beers
for _ in range(3): # _ means I do not care about the value of the variable
    drink_beer()

# we usually want to have some parameters in our functions
# let's make a generic drink function

def drink(liquid): # we can give our parameters any name we want
    print(f"Drinking {liquid}")
    # all done
    print("All done with drinking")

drink("water") # so now we can drink anything we want
drink("beer")
# drink specific beer
drink("Budvar")
drink("Pilsner Urquell")

# we can create a function that will drink from a list of drinks
def drink_from_list(drinks):
    # how many drinks
    print(f"Drinking from {len(drinks)} drinks")
    # drink each drink
    for my_drink in drinks:
        print(f"Drinking {my_drink}")
        # call drink function
        drink(my_drink)
    # all done
    print("All done with drinking from list")

drink_list = ["water", "beer", "Budvar", "Pilsner Urquell", "wine", "whiskey"]
drink_from_list(drink_list)

# how about function with more than 1 parameter
# let's make a function that will add 2 numbers
def display_add(a, b):
    print(f"{a} + {b} = {a + b}")
    # by default functions return None

result = display_add(2, 3)
print(result) # None

# let's make a function that will return the result
def add(a, b):
    return a + b

result = add(2, 3)
print(result) # now I can use it for something else

# let's make a function that will add 3 numbers
def add3(a, b, c):
    return a + b + c

result = add3(2, 3, 4)
print(result)

# I could make functions for adding 4, 5, 6, 7, 8, 9, 10 numbers
# but that would be silly
# there is a better way
# one way would be simple to use a list

def add_list(numbers):
    result = 0
    for number in numbers:
        # to make it slightly useful we could check if the number is actually a number
        if isinstance(number, (int, float)):
            result += number
    # of course sum() is a built-in function that does exactly this
    return result

my_mixed_values_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e", None, False, True]
# so sum will not work
try:
    print(sum(my_mixed_values_list))
except TypeError as e:
    print(e)

# but our function will
my_sum = add_list(my_mixed_values_list)
print(my_sum)
# why 56 not 55?
# turns out False is 0 and True is 1 actually
# check if True is number
print(isinstance(True, (int, float)))
# check if False is number
print(isinstance(False, (int, float)))

# we have another way of doing something with unknown of parameters
# we can use *args
# args is short for arguments, could use any name really, *argv for example or *args

def add_args(*args):
    result = 0
    for number in args:
        # to make it slightly useful we could check if the number is actually a number
        if isinstance(number, (int, float)):
            result += number
    return result

# now this function will take any number of arguments and will return the sum of those that are numeric (floats, ints, bools)

# so let's try it
my_result = add_args(1, 2, 3, 4, "Valdis", 6, 7, 8, 9, 10)
# compare with add_list
print(add_list([1, 2, 3, 4, "Valdis", 6, 7, 8, 9, 10]))


# now let's talk about default values
# let's make a function that will greet us
def greet(name="Valdis"):
    print(f"Hello {name}")
    # if we are lazy and don't want to type name every time
    # we could set a default value for name
    # idea is to use something that is usually a name, sane default

greet() # so now we can call greet without any parameters
greet("Līga") # but we can still call it with a parameter

# default values are great to add some extra functionality to existing functions without breaking existing code
# how about mult function that will multiply 2 numbers
def mult(a, b, debug=False):
    if debug:
        print(f"Multiplying {a} and {b}")
    return a * b

print(mult(2, 3))

# now I can debug my function
print(mult(2, 3, debug=True))

# returning multiple values
# we could return a list 
# but we can also return a tuple
def mult_and_div(a, b):
    return a * b, a / b # so we return a tuple - the usual way

# add and substract
def add_and_sub(a, b):
    return [a + b, a - b] # so we return a list  - less common

# how do we use those?

mult_result, div_result = mult_and_div(10, 5)
print(mult_result, div_result)
my_list = add_and_sub(10, 5)
print(my_list)
my_add, my_sub = add_and_sub(10, 5) # so I unpacked the list into 2 variables
print(my_add, my_sub)

# again this is not limited to 2 values, could be as many as we want

# let's say I make a function that returns a big list of number doubles
def double_list(start, stop):
    result = []
    for number in range(start, stop):
        result.append(number * 2)
    return result
    # list comprehension would be better here
    # return [number * 2 for number in range(start, stop)]

# now I want to use this function to make a list of doubles from 1 to 100
my_doubles = double_list(1, 101)
print(my_doubles)
# I could have done partial unpacking without knowing exactly how many values I will get
first, second, *rest, tail = double_list(1, 101)
print(rest) # so rest is a list of all the numbers in between
print(first, second, tail)

# again all of those are just names of variables, I could have used any names

# again i could have used list slicing to get what I want but this is more flexible
also_first = my_doubles[0]
also_second = my_doubles[1]
also_rest = my_doubles[2:-1]
also_tail = my_doubles[-1]

# finally let's combine positional arguments, variable arguments and default values
# let's make a shopping list function
def shop_smart(required_purchase, *args, shop="Rimi"):
    print(f"Going to {shop} to buy {required_purchase}")
    for item in args:
        print(f"Also buying {item}")
    # return how many items I bought
    return len(args) + 1 # why len(args) + 1 ? because we have required_purchase as well

# so now I can call my function with any number of items
shop_smart("Bread")
shop_smart("Bread", "Milk")
shop_smart("Bread", "Milk", "Eggs")
# how about I want to go to Maxima instead of Rimi
shop_smart("Bread", "Milk", "Eggs", shop="Maxima") # i need to add shop= to specify that I want to change the default value

# what do I do if I have a shopping list already in a list?
# I can use * to unpack the list
my_shopping_list = ["Bread", "Milk", "Eggs"]
shop_smart(*my_shopping_list) # so now I unpacked the list into positional arguments
# now how about going to Lidls instead of Rimi
shop_smart(*my_shopping_list, shop="Lidls")
# i can add some arguments as well
items_bought = shop_smart("Butter", "Cheese", *my_shopping_list, shop="Lidls") # so I can't mix positional and keyword arguments
print(f"I bought {items_bought} items")


    

