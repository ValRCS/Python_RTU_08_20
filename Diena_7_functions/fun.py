# # # # # # formal https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# # # # # # built in functions https://docs.python.org/3/library/functions.html
# # # # # # DRY ! https://en.wikipedia.org/wiki/Don%27t_repeat_yourself

# # # # # # we can give our functions parameters and those parameters take arguments

# print("Go eat")
# print("Let's order food")
# print("Go eat")
# print("Let's order food")
# print("Go eat")
# print("Let's order food")

# # # # defining simple function
# def go_eat():
#     print("Go eat")
#     print("Let's order food RIGHT Now!")
#     print("Pay and Leave")

# # # # # # calling function
# go_eat()
# go_eat()
# go_eat()

# # # # # # requirement that order_food is given an argument
# def order_food(dish):
#     dish = str(dish) # because we will be using capitalize later on 
#     print(f"I am ordering {dish}")
#     print(f"{dish.capitalize()} should be pretty tasty")
#     # so dish stops working here
# # # no dish here


# order_food("potatoes")
# order_food("ice cream")
# my_soup = "Beet soup"
# order_food(my_soup)
# order_food(555)

# # print(dish) # dish is not available globally because it is only inside function


# # # # # # # go to restaurant


# def eat(food_list):
#     # everything after indent will be run by this function
#     print("Hello")
#     print("Let's order some food")
#     # could add a check if food_list is truly a list
#     for food_item in food_list:
#         order_food(food_item)
#     print("Lets eat")
#     print("Let's leave and be happy")


# food_list = ["soup", "potatoes", "ice cream"]
# eat(food_list)

# # # # # # # call the function 2 times
# eat(["soup", "potatoes", "ice cream"])
# eat(["Cabbage"]) # i need one argument for eat function



def add(a,b):
    print(f"{a}+{b}={a+b}")

# add(3,322)
# add(5,7)
# add(25,37)
# my_result = add(10,25) # without return functions return None
# print(my_result, type(my_result))

def mult(a,b):
    result = a*b
    print(f"{a}*{b}={result}")
    return result

my_calc = mult(5,8)
print(my_calc)
print(mult(mult(5,10), mult(10,2))) # with return I gain ability to apply result to next function

def multi_calc(a,b):
    # could add check for 0
    return a*b, a/b # could return even more, multiple values are returned as tuples

my_mult, my_div = multi_calc(10,2)
print(my_mult,my_div)

def big_calc(a,b,c=100):
    result = a*b+c
    print(f"a*b+c={result}")
    return result

my_big = big_calc(3,4,10)
another_calc = big_calc(3,5)
print(my_big, another_calc)

def talk(text, is_yelling=False):
    """
    Prints text 
    is_yelling capitalizes text
    returns transformed text
    """
    if is_yelling:
        text = text.upper()
    print(text)
    return text


talk("Hello there")
talk("Hello there", is_yelling=True)
print(talk("Hello", is_yelling=True).lower()) # if function returns something i can chain it
talk("Aha", True)

add(b=10, a=3)

print("Valdis", "coding", end="\n\n", sep="|||")

# so in Python data types in function parameters are just hints! they do not affect function functionality
def diff(a: int, b: int) -> int:
    result = round(a-b,2)
    print(f"{a}-{b}={result}")
    return a-b

diff(10,3)
diff(10.6,3.7)


