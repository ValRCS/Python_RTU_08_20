# # # formal https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# # # built in functions https://docs.python.org/3/library/functions.html
# # # DRY ! https://en.wikipedia.org/wiki/Don%27t_repeat_yourself

# # # we can give our functions parameters and those parameters take arguments

# print("Go eat")
# print("Let's order food")
# print("Go eat")
# print("Let's order food")

# defining simple function
def go_eat():
    print("Go eat")
    print("Let's order food")

# # calling function
# go_eat()
# go_eat()
# go_eat()

# # requirement that order_food is given an argument
def order_food(dish):
    dish = str(dish)
    print(f"I am ordering {dish}")
    print(f"{dish.capitalize()} should be pretty tasty")
    # so dish stops working here
# no dish here


# order_food("potatoes")
# order_food("ice cream")
# my_soup = "Beet soup"
# order_food(my_soup)
# order_food(555)

# print(dish)


# # # go to restaurant


def eat(food_list):
    # everything after indent will be run by this function
    print("Hello")
    # print("Let's order some food")
    for food_item in food_list:
        order_food(food_item)
    print("Lets eat")
    print("Let's leave and be happy")


food_list = ["soup", "potatoes", "ice cream"]
eat(food_list)

# # # call the function 2 times
# eat(["soup", "potatoes", "ice cream"])
# # eat()
