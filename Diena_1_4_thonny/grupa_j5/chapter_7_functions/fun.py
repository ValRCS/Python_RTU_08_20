# let's talk about functions in Python

#  what is a function after all?
#  a function is a block of code that performs a specific task

# built-in functions
# docs: https://docs.python.org/3/library/functions.html

# so why do we need functions?

# 1. code reuse - 
# 2. abstraction - information hiding
# 3. organization - structuring code

# let's say i have a couple of tasks to do
# related to eating

# 1. go to the shop
# 2. buy food
# 3. prepare food

# i can do it all in one go
# or i can split it into smaller tasks

# 1. go to the shop
# we could have the instructions in code without a function
# print("Let's go to the shop")
# print("We are at the shop")

# however if we need to go to the shop again
# we would need to copy paste the code

# instead we can create a function
# that will do the job for us
# and we can reuse it as many times as we want

# 1. go to the shop
def go_to_the_shop():
    print("Let's go to the shop")
    print("We are at the shop")

# when i run this file nothing happens
# because i only defined the function
# but i did not call it

# let's call it
go_to_the_shop()
print('do something else')
go_to_the_shop()

# we use meaningful names for functions to describe what they do
# so get documentation for free - we also have docstrings

# now let's make a buy food function
# we want to buy a specific food
# so we need to pass the food as an argument
def buy_food(food):
    print(f"Let's buy {food}")

# let's call it
buy_food("bread")
buy_food("milk")

# we can create buy foods function
# that will buy multiple foods
# we need to pass a list of foods
def buy_foods(foods):
    for food in foods:
        buy_food(food) # we can use already existing function from before
# the function name should be defined before the function is called
# else we get NameError

shopping_list = ["bread", "milk", "eggs", "beer"]
buy_foods(shopping_list)

# 3. prepare food
# we can create a function that will prepare food
# we need to pass the food as an argument
# we will want to return the prepared food
def prepare_food(food):
    print(f"Let's prepare {food}")
    return f"Cooked {food}" # returns something - here string
# if we did not use return we would get None


# let's call it
prepared_food = prepare_food("eggs")
print(prepared_food)