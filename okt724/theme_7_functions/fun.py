# functions are a way to organize code into reusable blocks
# core idea, function should do one thing and do it well
# in real life functions can be much more complex
# functions let us reuse code

# let's say I want to go eat and order food
# print("I'm hungry, let's go eat")
# print("I want to order a pizza")

# # i do something else
# print("Doing something else")

# # I want to order another pizza
# # now i could just copy paste the code
# print("I'm hungry, let's go eat")
# print("I want to order a pizza")

# how about doing it 500 times?
# another consideration is that if I want to change the order

# let's start with basic function definition
def order_pizza(): # typically functions start with verbs
    print("I'm very hungry, let's go eat")
    print("I want to order a pizza")
    # I can easily change the instructions here
    # and they will be reflected in all calls to the function

# what will happend if I run code right now?
# why did nothing happen?
# I only defined the function, I didn't call it
# let's call the function
# order_pizza() # note the blank parenthesis - no other information is given
# I can order 3 times
# for _ in range(3): # _ means we do not care for the loop variable
#     order_pizza()

# ordering pizza is nice
# but how about ordering anything?
# for that we need to pass information
# we define parameters in the function definition
# we pass arguments to the function when we call it
# let's make function to order any type of food
def order_food(food):
    # food is now in scope of the function
    print("I'm very hungry, let's go eat")
    print(f"I want to order {food}")
    # when function ends, the variable food is destroyed - goes out of scope

# let's order a burger
# order_food("a burger")
# i can also pass in a variable
snack = "a hot dog"
# order_food(snack)



# how about writing a function that will take a food list and order everything
def order_all(food_list):
    print(f"We have {len(food_list)} items to order")
    for food in food_list:
        order_food(food)
    print("I am stuffed")

# let's order a lot of food
order_all(["salad", "soup", "steak", "ice cream", "coffee"])

print("All done")

# we can shadow variables in different scopes - tvērumos
# personally I am not against using the same variable names
# otherwise we run out of useful names
food = "a sandwich" # this is global variable
order_food(food) # this will use the global variable
# inside the function the variable food is local
# to illustrate let's make a function play with food
def play_with_food(food):
    # now food is local to the function
    food = food + " and a drink" # here it will not affect the global variable
    print(f"Playing with {food}")

play_with_food(food)
# the global variable is not changed
print(food)

# i could modify global variable with the global keyword
# this is usually not recommended
def change_food(extra_food):
    global food # now we have access to global variable
    food = food + " and " + extra_food
    print(f"Changed global variable to {food}")
# usually above is not to be used - leads to messy code

change_food("a cookie")
print(food)

# better would be to return something from the function
def change_food_return(food, extra_food):
    print('Changing food')
    result = food + " and " + extra_food
    return result # if we have return we can assign the result to a variable

new_food = change_food_return(food, "a cake")
print(new_food)

def print_addition(a, b):
    print(f"{a} + {b} = {a + b}")
    # returns None by default

# simpler example adding two numbers
def add(a,b):
    # i could validate the numbers etc here
    return a + b

print_result = print_addition(10,20)
print("Print_result result", print_result) # will be None, since our function returns nothin

result = add(5, 7)
print("Add function result", result)

# let's make a multiplication function
def multiply(a, b):
    return a * b

# now I can chain functions that return values

big_result = add(multiply(2,3), add(4,5)) # we can nest functions
# the inner functions will be evaluated first

print("Big result", big_result)

# often we have some sensible default values but we also want the ability to change them

def order_food_default(food="a pizza"): # we define a default value for the parameter food
    print("I'm very hungry, let's go eat")
    print(f"I want to order {food}")

# now I have two ways of calling the function
order_food_default() # will order a pizza
# i can order anything else
order_food_default("a salad")

# defaults should be sensible, meaning something that is often used
# if I want a healthier lifestyle I could change the default to a salad or something else

# let's make a calculator function with some defaults
def calculator(a, b=0, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        # could add a check for division by zero
        return a / b
    else:
        return "Unknown operation"
    
# now I can call add by default
result = calculator(5, 7) # will add 5 and 7 since add is default
print("Default add", result)
# i could pass multiply
result = calculator(5, 7, "multiply")
print("Multiply", result)
# since I added default values I can also call the function without them
result = calculator(5) # will add 5 and 0
print("Default add", result)

# let's imagine I want to keep b as 0 but use multiply
# then I pass the operation as a keyword argument
result = calculator(5, operation="multiply") # will multiply 5 and 0

# remember how we used print with sep and end arguments
# that is the same idea
# let's add smiley to end
print(result, end=" :)\n") # will print the result and then a smiley

# i could make a function with all default arguments
def print_with_smiley(text="Hello", sep=" ", end=" :)\n"):
    print(text, sep=sep, end=end)
# we've just created so called wrapper function
# wrapper functions are functions that call other functions with some default values

# now I can call the function with nothing
print_with_smiley() # will print Hello :)
# i could call it with some or other values
print_with_smiley("Goodbye", sep=" - ") # will print Goodbye - :)

# one restriction on default values they must come after non-default values

# you are not required to use default values
# but they make life more pleasant

# returning multiple values
# how do we return multiple values?
# we can return a tuple
# tuple is simply an immutable list
# we return tuples using , syntax

# return min and max for list
def min_max(numbers):
    # of course I could have made a list and returned a list
    # but tuples are more common for small number of values
    # tuples are a bit faster than lists since they are immutable
    return min(numbers), max(numbers)

# let's test the function
numbers = [5, 7, 3, 9, 2]

# we can immediately unpack the tuple into separate variables
min_value, max_value = min_max(numbers)
print("Min value", min_value)
print("Max value", max_value)

both_values = min_max(numbers)
print("Both values", both_values) # prints the tuple note the normal parenthesis
# first value
print("First value", both_values[0])
# second value
print("Second value", both_values[1]) # so similar to list or string indexing

# lets make a function that returns min max and len
def min_max_len(numbers):
    return min(numbers), max(numbers), len(numbers)

# we can unpack the tuple into separate variables
min_value, max_value, length = min_max_len(numbers)
print("Min value", min_value)
print("Max value", max_value)
print("Length", length)

# now let us make our functions friendlier

# we can add docstrings to functions
# docstrings are a way to document functions
# they are enclosed in triple quotes
# let's make a function that returns sum, length and average

def sum_len_avg(numbers):
    """
    Returns sum, length and average of the numbers

    Input:

    numbers: list of numbers

    Output:

    triple of sum, length and average
    sum: sum of the numbers
    length: number of numbers
    average: average of the numbers
    Constraints:
    numbers should be a list of numbers
    """
    sum_numbers = sum(numbers)
    length = len(numbers)
    average = sum_numbers / length
    return sum_numbers, length, average

# let's test the function
sum_numbers, length, average = sum_len_avg(numbers)
print("Sum", sum_numbers)
print("Length", length)
print("Average", average)

# now how about providing some hints to the user on data types
# often the Python interpreter will not complain if you pass in wrong data type

# let's make a function that adds two numbers
# we can provide type hints in the function definition
def add_ints(a:int, b:int) -> int:
    """
    Adds two numbers

    Input:

    a: number
    b: number

    Output:

    sum of a and b
    """
    return a + b

# let's test the function
result = add_ints(50, 70)
print("Result", result)
# how about two floats
result = add_ints(50.5, 70.5)
print("Result", result) # will add the floats
# how about two strings?
result = add_ints("50", "70") 
print("Result", result) # will concatenate the strings
# how about two lists?
result = add_ints([5,6], [7,8])
print("Result", result) # will concatenate the lists

# type hints are not used by Python interpreter
# type hints are used by linting tools

# now let's talk about passing in mutable data types such as lists
# in Python arguments are passed by object reference
# for immutable values we basically get a copy
# for mutable values we have a reference to the original

# let's make a function called mutate a list

def add_something_list(some_list:list, item:any) -> None:
    """
    IN PLACE modifier of list
    """
    # now we will call append here
    some_list.append(item) # this will MODIFY the original list!!
    # we could return this list but we don't need to

# let's test the function
original_list = [5, 7, 3]
print("Original list", original_list)
# let's add 9 to the list
add_something_list(original_list, 9)
print("Modified list", original_list)

# we could also make a function that returns a new list without changing the original
def add_something_list_new(some_list:list, item:any) -> list:
    """
    Returns a new list with item added - OUT OF PLACE modifier of list
    """
    # we will return a new list
    new_list = some_list.copy() # we make a copy of the original list
    new_list.append(item) # we add the item to the new list
    # we need to return the new list else we lose it
    return new_list

# let's test the function
print("Original list", original_list) # we have 9 in the list
# let's add 11 to the list
new_list = add_something_list_new(original_list, 11)
print("Original list", original_list) # original list is unchanged
print("New list", new_list) # new list has 11 added

# let's make a function that will take a list or tupleand return sum of its squares
# return could be int or float
def sum_squares(numbers:list|tuple) -> int|float:
    """
    Returns sum of squares of numbers

    Input:

    numbers: list of numbers

    Output:

    sum of squares
    """
    # we will use list comprehension
    # squares = [x**2 for x in numbers]
    # return sum(squares)
    # we could just use a number
    total = 0
    for num in numbers:
        total += num**2
    return total

# let's test the function on list and tuple
numbers = [5, 7, 3]
result = sum_squares(numbers)
print("List result", result)
number_tuple = (5, 7, 3.1415926) # parenthesis are optional
result = sum_squares(number_tuple)
print("Tuple result", result)

# another question when should tuples be used?
# tuples are used when you want to return multiple values
# tuples are for different types of data
# tuples are for immutable data

# lists are for mutable data
# lists are for similar data