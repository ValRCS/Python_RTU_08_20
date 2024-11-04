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
import my_module # now I can use the functions and variables from my_module

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