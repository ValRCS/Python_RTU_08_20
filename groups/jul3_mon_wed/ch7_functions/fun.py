# let's talk about functions in Python

# what is a function after all?
# a function is a block of code that can be reused
# ideally a function should do one thing and do it well - Platonic ideal
# we also have concept of DRY - Don't Repeat Yourself

# so what do functions bring us?
# 1. Reusability - we can reuse functions in our code in different places
# 2. Readability - we can give functions meaningful names, self documenting code
# 3. Modularity - we can separate our code into logical parts - divide and conquer
# 4. Testing - we can test our functions separately from the rest of the code
# 5. Abstraction - we can hide implementation details from the user of the function


# first of all we have been using built in functions
# print() is a function
# len() is a function
# type() is a function
# all Python built in functions https://docs.python.org/3/library/functions.html

# so let's build our own function

# let's say I want to eat a sandwich

# I need to get bread, put something in between, and eat it

# I could write a function like this
def eat_sandwich(): # notice empty parentheses - we will get back to them
    print("I am eating a sandwich")
    print("I am done eating a sandwich")

# i need to call my function to use it
eat_sandwich() # this is how we call a function

# functions in python are first class citizens
# that means we can assign them to variables
# we can pass them as arguments to other functions - for example as key in sorted()
# we can return them from other functions

# so let's assign our function to a variable
# usually this not very common but it is possible
my_alias = eat_sandwich # notice no parentheses!!!
print(my_alias) # so my_alias is a variable that points to a function
# we can call our function using my_alias
my_alias()

# eat_sandwich = "I am eating a sandwich" # this is a string
# # so original function is gone (well I still have my_alias)
# eat_sandwich() # this will not work - eat_sandwith is not a function

# let's make a more useful a generic eat something function
def eat(food): # notice food is a parameter
    print(f"Look Ma, I am eating {food}")
    print(f"I am eating {food}")
    print(f"I am done eating {food}")

# so i call it by passing an argument
eat("a sandwich")
eat("a burger")
eat("a pizza")
eat("a salad")
eat("some ice cream")
eat(3.1419265359) # some pie

# lets make an add function
# with two parameters
def add(a, b):
    print(a + b)
    # by default return value of a function is None

# this function will work with any two types that have + operator defined

add(1, 2)
add(1.0, 2.0)
add("1", "2") # this will concatenate strings so result will be "12"
add([1,5], [2,6]) # this will concatenate lists
# error will be if + is not defined for the types
try:
    add(1, "2") # this will not work
except TypeError as e:
    print(e)
# i could fix it by passing correct types
add(1, int("2")) # this will work

# so what is the difference between parameter and argument?
# parameter is a variable in the function definition
# argument is a value passed to the function
# so in the above example a and b are parameters
# and 1 and 2 are arguments
# practically we are using these terms interchangeably - same thing

# now about our functions we might want to return something
# let's make a function that returns multiplication of two numbers

def multiply(a, b):
    # i could do other stuff here such as print
    return a * b # return keyword returns a value from the function

# compare add and multiply functions
add_result = add(1, 2) # this will print 3 but add_result will be None !
print(add_result) # None
multiply_result = multiply(1, 2) # this will return 2
print(multiply_result) # 2

# with return we can now chain functions
# lets call multiply function inside another multiply function
big_result = multiply(multiply(1, 2), multiply(3, 4)) # first will be 2, second will be 12
print(big_result) # 24

# let's create a function that will take a list of food items and eat them
def eat_many(foods):
    for food in foods:
        eat(food)

menu = ["a sandwich", "a burger", "a pizza", "a salad", "some ice cream", 3.1419265359]
eat_many(menu)

# we can return multiple values from a function
# let's make a function that will return sum and product of two numbers

def sum_and_product(a, b):
    return a + b, a * b # this will return a tuple

summa, product = sum_and_product(2, 3) # this will unpack tuple into two variables
print(summa, product) # 5 6