# global variable here
dessert = "ice cream"

# defining function


def eat_food(dish):
    """
    Orders Food
    """
    # the above triple quoted string is documentation
    # printing is considered a side-effect
    print("Hello")
    print(f"Let's eat {dish}")
    print("Good bye")
    # returns None by default if not specified


eat_food("potatoes")
# DRY princips DO NOT REPEAT YOURSELF
eat_food("fish")

eat_food(dessert)
eat_food(9000)

print(dessert)

# returning values


def adder(a, b):
    result = a+b  # result will not be available outside adder
    # print(a+b)
    # print(result)
    # return a+b
    return result
 # result is not visible after indentation stops


my_val = adder(5, 10)
my_str = adder("alus", " muca")
print(my_val, my_str)

print(adder(adder(5, 20), 50))


def mult(a, b):
    return a * b
