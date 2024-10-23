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