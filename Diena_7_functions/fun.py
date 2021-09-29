# # # # # # # # # # formal https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# # # # # # # # # # built in functions https://docs.python.org/3/library/functions.html
# # # # # # # # # # DRY ! https://en.wikipedia.org/wiki/Don%27t_repeat_yourself

# # # # # # # # # # we can give our functions parameters and those parameters take arguments

# print("Go eat")
# print("Let's order food")

# print("maybe i do something else")
# print("Go eat")
# print("Let's order food")
# print("Go eat")
# print("Let's order food")

# # # # # # # defining simple function
def go_eat():
    # function block starts here
    print("Go eat fast food")
    print("Let's order food RIGHT Now!")
    print("Pay and Leave")
    # we could add more stuff for our function here include loops, ifs etc

# # # # # # # # # # calling function
# go_eat()
# # # go_eat()
# # # print("Do something else")
# for _ in range(4): # if we do not need the loop variable we use _ 
#     go_eat()
# # # go_eat()

# # # # # # # # # # requirement that order_food is given an argument
def order_food(dish):
    dish = str(dish) # because we will be using capitalize later on 
    print(f"I am ordering {dish}")
    print(f"{dish.capitalize()} should be pretty tasty")
    # so dish stops working here
# # # # # # no dish here


# order_food("potatoes")
# order_food("ice cream")
# my_soup = "Beet soup"
# order_food(my_soup)
# order_food(555)

# # # # # # print(dish) # dish is not available globally because it is only inside function


# # # # # # # # # # # go to restaurant


def eat(food_list):
    # everything after indent will be run by this function
    print("Hello")
    print("Let's order some food")
    # could add a check if food_list is truly a list
    for food_item in food_list:
        order_food(food_item)
    print("Lets eat")
    print("Let's leave and be happy")


# food_list = ["soup", "potatoes", "ice cream"]
# eat(food_list)
# another_food_list = ["cabbage", "beans", "onions"]
# eat(another_food_list)

# # # # # # # # # # # call the function 2 times
# # # # # eat(["soup", "potatoes", "ice cream"])
# # # # # eat(["Cabbage"]) # i need one argument for eat function
# eat(["Kartupelis"]) # so we passed a list of one item
# # # # # # what happens if we pass our function a string...
# eat("Kartupelis") # turns out we will go through our food one letter at a time...
# eat(55) # we cant go through numbers

# i can add another parameter
def add(a,b):
    print(f"{a}+{b}={a+b}")
    # so by default we return None !

# add(3,322)
# add(5,7)
# add(25,37)
# my_result = add(10,25) # without return functions return None
# print(my_result, type(my_result))

result = 55 # this is global not used inside mult!

def mult(a,b):
    result = a*b # result could be another name, this is a local variable not used outside function
    print(f"{a}*{b}={result}") # print is not always needed in a function, print is heavy
    return result # we can return anything

# my_calc = mult(5,8)
# print(my_calc, result) # so result is still 55
# result = mult(10,6)
# print(result)

# multi_calc_result = mult(mult(5,10), mult(10,2)) # with return I gain ability to apply result to next function
# print(multi_calc_result)

def multi_calc(a,b):
    # could add check for 0
    return a*b, int(a/b) # could return even more, multiple values are returned as tuples

# my_mult, my_div = multi_calc(10,2) # so called tuple unpacking 
# print(my_mult,my_div)
# print(multi_calc(9,2)) # parenthesis show up because we are returning a tuple(which is likea  fixed list)


# Default argument idea
def big_calc(a=-500,b=1000,c=100, verbose=False): # so c will be 100 if not given as argument
    result = a*b+c
    if verbose:
        print(f"Incoming Arguments: a {a}, b {b}, c {c}")
        print(f"a*b+c={result}")
    # so function prints nothing unless verbose flag/argument is passed as True
    return result



my_big = big_calc(3,4,10) # so we can use it normally
another_calc = big_calc(3,5) # notice we only need 2 arguments, and c will be default 100
print(my_big, another_calc)

print(big_calc(5)) # only giving value for a, : b,c use defaults (1000 and 100)
print(big_calc()) # this will use ALL 3 default values
print(big_calc(c = 10, b = 5, a = 4)) # i can pass arguments in whichever order I want if i use named arguments
print(big_calc(b=25)) # i can pass only one named argument, the rest stay default

print(big_calc(10,30,50, verbose=True))

def talk(text, is_yelling=False):
    """
    Prints text 
    is_yelling capitalizes text
    returns transformed text
    """
    if is_yelling:
        text = text.upper()
    print(text) # printing is considered a side effect inside a function
    return text


talk("Hello there") # basically a print
talk("Hello there indeed", True) # True refers to is_yelling but it might not be obvious with many flags
talk("Hello there", is_yelling=True) # this is more clear
talk(is_yelling=True, text="some random text") # with named arguments I can change order, but generally not recommended
print(talk("Hello", is_yelling=True).lower()) # if function returns something i can chain it
# # # talk("Aha", True)

# # # # add(b=10, a=3)

print("Valdis", "coding", end="\n\n\n!*-*\n\n", sep="|||") # a bit extreme for end and sep but your choice

# # # # # so in Python data types in function parameters are just hints! they do not affect function functionality
def diff(a: int, b: int) -> int: # we defined a function signature , what data types should be used
    result = round(a-b,2)
    print(f"{a}-{b}={result}")
    return a-b
    # return "badac"

diff(10,3)
diff(10.6,3.7) # even if the data types are wrong, Python will still run the program

def get_string_length(text: str) -> int:
    return len(text)

print(get_string_length("Valdis"))
# # diff("Valdis",35354)
# # # it is only static type checking tool such as Pyright extension that will yell at us

# go_eat()


