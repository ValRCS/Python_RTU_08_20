# let's talk about functions in Python

# what is a function?
# a function is a block of code that performs a specific task
# ideally a function should do one thing and do it well
# in programming we have a concept of DRY - Don't Repeat Yourself

# why do we need functions?
# 1. Reusability - we can reuse functions in different parts of our program
# 2. Readability - we can give functions meaningful names - so our code is easier to read
# 3. Modularity - we can divide our program into smaller parts - so it is easier to maintain
# 4. Abstraction - we can hide implementation details - so we can focus on the task at hand

# first of all we have built-in functions
# we have already used some of them
# docs: https://docs.python.org/3/library/functions.html


# so I have some tasks related to eating

# first I want to eat a sandwich

# 1. I want to eat a sandwich
# 2. I want to eat a burger
# 3. I want to eat a salad
# 4. I want to eat a soup 
# 5. I want to eat a pizza
# etc.

# first i will write a function to eat a sandwich

def eat_sandwich():
    print("Look Ma!")
    print("I am eating a sandwich")
    # I could do more tasks related to eating a sandwich here
# we have defined a function here

# notice If i run the file nothing happens
# why? because I have only defined the function

# now I can call the function
eat_sandwich()
# i could even call a loop to eat 5 sandwiches
for _ in range(5): # again _ is a throwaway variable
    eat_sandwich()

# so if I want to eat a burger I need to write another function
# if eating burger was so much different from eating a sandwich
# i would write a new function for it eat_burger()
# but if it is very similar I can reuse my eat_sandwich() function

# so instead I will create a general eat_food() function
# and I will pass the food as a parameter
def eat_food(food):
    print(f"Look Ma! I am eating {food}")
    # I could do more tasks related to eating a anything here

# now I can call the function
eat_food("burger")
eat_food("salad")
eat_food("soup")
eat_food("pizza")
eat_food("sandwich") # no need for eat_sandwich() anymore

# lets make a function to eat from a plate of foods
# we will pass a list of foods
def eat_from_plate(foods):
    for food in foods:
        eat_food(food)
    print(f"I've eaten {len(foods)} foods from the plate")

my_foods = ["burger", "salad", "soup", "pizza", "sandwich"] # list of foods
eat_from_plate(my_foods) # we pass the list to the function