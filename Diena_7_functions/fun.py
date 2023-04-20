# # # # # # # # # # # # # # # # formal https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# # # # # # # # # # # # # # # # built in functions https://docs.python.org/3/library/functions.html
# # # # # # # # # # # # # # # # DRY ! https://en.wikipedia.org/wiki/Don%27t_repeat_yourself

# # # # # # # # # # # # # # # # we can give our functions parameters and those parameters take arguments

# print("Go eat")
# print("Let's order food")

# print("maybe i do something else")
# # # lots of code could happen here
# print("Go eat")
# print("Let's order food")
# print("Go eat")
# print("Let's order food")

# # # go_eat() # not yet known
# # # # # # # # # # # # # defining simple function
# # so i create an abstraction for something that i want to do
def go_eat():
    # function block starts here
    print("Go eat fast food")
    print("Let's order food RIGHT Now!")
    print("Toast the host!")
    print("Leave a nice tip")
    # print("Pay and Leave")
    # we could add more stuff for our function here include loops, ifs etc

# # # # # # # # # # # # # # # # # calling function
# go_eat()
# go_eat()
# print("Do something else")
# for _ in range(4): # if we do not need the loop variable we use _ 
#     go_eat()
# # # # # # go_eat()

# functions with no parameters are sometimes called void functions
# also called procedures in some languages
# they are used to do something, but not return anything


# # # # # # # # # # # # # # # # # requirement that order_food is given an argument
def order_food(dish):
    dish = str(dish) # because we will be using capitalize later on 
    print(f"I am ordering {dish}")
    print(f"{dish.capitalize()} should be pretty tasty")
    # i could add more instructions here for order_food function
# # #     # so dish stops working here
# # # # # # # # # # # # # no dish here

# # order_food() # this will not work
# order_food("pizza") # this will work
# order_food("potatoes")
# order_food("ice cream")
# my_soup = "Beet soup"
# order_food(my_soup) # i can pass a variable as an argument
# # order_food(555)

# # print("All done ordering food!")	
# # # # # print(dish) # dish is not available globally because it is only inside function


# # # # # # # # # # # # # # # # # # go to restaurant


def eat(food_list):
    # everything after indent will be run by this function
    print("Hello")
    print("Let's order some food")
    # could add a check if food_list is truly a list
    for food_item in food_list:
        order_food(food_item)
    print("Lets eat")
    print("Let's leave and be happy")


# my_food_list = ["soup", "potatoes", "ice cream"]
# eat(my_food_list)
# # # print("Whew I am full")
# another_food_list = ["cabbage", "beans", "onions"]
# eat(another_food_list)

# # i could pass list directly
# eat(["salad", "soup", "potatoes", "ice cream"])

# # food_list = ["soup", "potatoes", "ice cream"]
# # for food_item in food_list:
# #     print(f"READY to eat {food_item}")
# #     order_food(food_item)

# # # # # # # # # # # # # # # # # # call the function 2 times
# # # # # # # # # # # # eat(["soup", "potatoes", "ice cream"])
# # # # # # # # # # # # eat(["Cabbage"]) # i need one argument for eat function
# eat(["Kartupelis"]) # so we passed a list of one item
# # # # # # # # # # # # # # # # what happens if we pass our function a string...
# eat("Kartupelis") # turns out we will go through our food one letter at a time...
# # # # # # # # eat(55) # we cant go through numbers

# # # # # # # # i can add another parameter
def add(a,b):
    print(f"{a}+{b}={a+b}") # print is a side effect of add function
#     # so by default we return None !

# add(3,322)
# add(5,7)
# add(25,37)
# my_result = add(10,25) # without return functions return None
# print(my_result)
# print(type(my_result)) # <class 'NoneType'>

# result = 55 # this is global not used inside mult!

def mult(a,b):
    result = a*b # result could be another name, this is a local variable not used outside function
    print(f"{a}*{b}={result}") # print is not always needed in a function, print is heavy
    return result # we can return anything, local function result ends its life here

# my_calc = mult(5,8)
# print(my_calc)
# print(my_calc, result) # so result is still 55
# result = mult(10,6)  #overwriting the global result

# print(result) # global result is now overwritten by local result

# multi_calc_result = mult(mult(5,10), mult(10,2)) # with return I gain ability to apply result to next function
# print(multi_calc_result)

# # # # # i can return multiple values at once
def multi_calc(a,b):
    # could add check for b == 0
    return a*b, int(a/b) # could return even more with comma multiple values are returned as tuples

# my_mult, my_div = multi_calc(10,2) # so called tuple unpacking 
# print(my_mult,my_div)
# # # print(multi_calc(9,2)) # parenthesis show up because we are returning a tuple(which is likea  fixed list)


# new_list = list(range(10))
# print(new_list)

# # # this method will modify whichever list I pass IN PLACE!! returning reference to original list
def mod_my_list(my_list, my_item):
    if my_item in my_list:
        print(f"removing item {my_item} from list ")
        my_list.remove(my_item)
    else:
        print(f"adding item {my_item} to list ")
        my_list.append(my_item)
    return my_list # this is a reference to the original list

# list_alias = mod_my_list(new_list, 5)
# mod_my_list(new_list, 42)
# print(new_list)
# print(list_alias)
# # list_alias is a reference to the same list as new_list
# print(list_alias is new_list) # True

## We could make this function OUT OF PLACE by returning a new list
def mod_my_list_out_of_place(my_list, my_item):
    new_list = my_list.copy() # so we make a copy of the list
    if my_item in new_list:
        print(f"removing item {my_item} from list ")
        new_list.remove(my_item)
    else:
        print(f"adding item {my_item} to list ")
        new_list.append(my_item)
    return new_list # this is a reference to the original list

# modded_list = mod_my_list_out_of_place(new_list, 50)
# # lists are different!
# print(new_list)
# print(modded_list)


# # mod_my_list(new_list, "Valdis")
# # print(new_list)
# # # # # # Default argument idea

def big_calc(a=-500,b=1000,c=100, verbose=False): # so c will be 100 if not given as argument
    """
    My big calc function - docstring used for documentation and help\n
    a - is the first number - we should write what it is\n
    b - is the second number\n
    c - is the third number\n
    verbose - is a boolean value that tells us if we want to print the result or not
    """
    result = a*b+c
    if verbose:
        print(f"Incoming Arguments: a {a}, b {b}, c {c}")
        print(f"a*b+c={result}")
    # so function prints nothing unless verbose flag/argument is passed as True
    return result


# my_default_result = big_calc() # will use ALL default values
# print(my_default_result)
# my_big = big_calc(3,4,10) # so we can use it normally
# print(my_big)
# print(big_calc(30,40,100,True)) # so we can use it normally
# print(big_calc(30,40,100,verbose=True)) # so we can use it normally

# print(big_calc(b=40,a=30,verbose=True,c=100)) # i can mix up the order but generally best avoided
# print("Valdis", "Kazlauskas", "Kaunas", sep=" -\*/- ") # so we can use it normally
# another_calc = big_calc(3,5) # notice we only need 2 arguments, and c will be default 100
# print(another_calc)
# # # # # # # print(my_big, another_calc)

# print(big_calc(5)) # only giving value for a, : b,c use defaults (1000 and 100)
# print(big_calc(a=5)) # only giving value for a, : b,c use defaults (1000 and 100)
# print(big_calc(b=10)) # only giving value for b, : a,c use defaults (-500 and 100)
# # # # print(big_calc()) # this will use ALL 3 default values
# # # # # print(big_calc(c = 10, b = 5, a = 4)) # i can pass arguments in whichever order I want if i use named arguments
# # # # # print(big_calc(b=25)) # i can pass only one named argument, the rest stay default

# # # # # print(big_calc(10,30,50, verbose=True))

# # # # # so use sane defaults

def talk(text, is_yelling=False):
    """
    Prints text 
    is_yelling capitalizes text
    returns transformed text
    this is a docstring - used in help(talk) also good for generating documentation and webpages
    """
    if is_yelling:
        text = text.upper()  # notice we change the value of text here
    print(text) # printing is considered a side effect inside a function
    return text


# talk("Hello there") # basically a print
# talk("Hello there indeed", True) # True refers to is_yelling but it might not be obvious with many flags
# talk("Hello there", is_yelling=True) # this is more clear
# talk(is_yelling=True, text="some random text") # with named arguments I can change order, but generally not recommended
# # # print(talk("Hello", is_yelling=True).lower()) # if function returns something i can chain it
# # # # # # # # # talk("Aha", True)



# # # # # # # # # # # add(b=10, a=3)

# # # # print("Valdis", "coding", "and even more strings", end="\n\n\n!*-*\n\n", sep="|||") # a bit extreme for end and sep but your choice

# # # type hints in Python
# # # # # # # # # # # so in Python data types in function parameters are just hints! they do not affect function functionality
def diff(a: int, b: int = 35) -> int: # we defined a function signature , what data types should be used
    result = round(a-b,2)
    print(f"{a}-{b}={result}")
    return result
    # return "badac"

# print(diff(100))
# print(diff(10,3))
# print(diff(10.6,3.7)) # even if the data types are wrong, Python will still run the program
# # print(diff(100))

# def get_string_length(text: str) -> int:
#     return len(text)

# print(get_string_length("Valdis"))
# print(get_string_length([1,2,6]))
# # # # # # # # # diff("Valdis",35354)
# # # # # # # # # # it is only static type checking tool such as Pyright extension that will yell at us

# # # # # # # # go_eat()

# # talk("Hello there", True)

# last thing functions can be called only after they are defined
