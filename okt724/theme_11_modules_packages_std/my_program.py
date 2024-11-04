# let's learn how to utilize the modules and packages in Python

# import the module
# what is a module?
# A module is a file containing Python definitions and statements.
# in Python using a module is as simple as using the import statement

# why modular programming?
# 1. easier to understand the code
# 2. easier to maintain the code
# 3. easier to reuse the code
# 4. name conflicts less likely - namespaces

# so let's import my_module 
# my_module.py is just a file of Python code
# import my_module # now I can use the functions and variables from my_module

# naming modules try to avoid conflicts with standard library modules
# https://docs.python.org/3/library/index.html

# # now let's use the functions and variables from my_module
# print(my_module.my_favorite_foods) # ['pizza', 'pasta', 'sushi', 'ramen', 'tacos']
# # so we use my_module namespace to access the variables and functions in my_module

# # i can define some shopping list
# shopping_list = ['milk', 'eggs', 'bread', 'cheese', 'butter']
# # i can use the function from my_module to print my shopping list
# my_module.print_fav_foods(shopping_list)

# # i can use MyPet class from my_module
# my_pet = my_module.MyPet('Winnie', 'cat')
# print(my_pet) # Winnie is a cat

# if I do not like my_module name I can use alias

# import my_module as mm # typical in Python to use 2 or 3 letter alias
# # then I use mm instead of my_module
# print(mm.my_favorite_foods) # ['pizza', 'pasta', 'sushi', 'ramen', 'tacos']
# of course that assumes there is no conflict with the alias name 
# for example if my_math is using alias mm and my_module is using alias mm then we have a conflict

# we can also import specific functions, variables, classes from a module
# here we have to be careful not to have conflicts with the names
# we are losing namespace protection here, gaining shorter names

# i can import just MyPet class from my_module and then print_fav_foods function
# from my_module import MyPet, print_fav_foods # the variables will not be imported
# # this approach would be good if there is a huuuge module and I need only a few functions or classes

# # i can use MyPet class from my_module
# my_pet = MyPet('Winnie', 'cat')
# print(my_pet) # Winnie is a cat

# # i can define some shopping list
# shopping_list = ['milk', 'eggs', 'bread', 'cheese', 'butter']
# # i can use the function from my_module to print my shopping list
# print_fav_foods(shopping_list)

# we can combine importing specific functions, variables, classes with alias
# in other words I can rename the imported function, variable, class
# from my_module import MyPet as MP, print_fav_foods as pff # kind of cryptic but possible
# # personally I do not like this approach unless aliases are clear and short
# # # i can use MyPet class from my_module
# my_pet = MP('Winnie', 'cat')
# print(my_pet) # Winnie is a cat

# # # i can define some shopping list
# shopping_list = ['milk', 'eggs', 'bread', 'cheese', 'butter']
# # # i can use the function from my_module to print my shopping list
# pff(shopping_list)

# there is one dangerous import that is * - it imports everything from the module
# avoid it! it is unclear what is being imported and it can lead to name conflicts

# again use full module import or use alias or import specific functions, variables, classes


# now let's talk order of imports
# 1. standard library imports - usually first

# where does Python look for modules?
# let's use sys module to find out
import sys # this is a standard library module that provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter
# i can print python version
print(f"Python version: {sys.version}")
# i can print path where Python looks for modules
print(f"Python path where to look for modules: {sys.path}")
# so the first path is the current working directory
# then the paths where the standard library modules are stored

# let's look at some more standard library modules