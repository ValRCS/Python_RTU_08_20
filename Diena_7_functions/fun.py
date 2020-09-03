# formal https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# built in functions https://docs.python.org/3/library/functions.html
# DRY ! https://en.wikipedia.org/wiki/Don%27t_repeat_yourself

# we can give our functions parameters and those parameters take arguments

def order_food(dish):
    print(f"I am ordering {dish}")
    print(f"{dish.capitalize()} should be pretty tasty")

# go to restaurant


def eat():
    # everything after indent will be run by this function
    print("Hello")
    # print("Let's order some food")
    order_food("potatoes")
    order_food("ice cream")
    print("Lets eat")
    print("Let's leave and be happy")


# call the function 2 times
# eat()
eat()
