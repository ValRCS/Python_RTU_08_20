# we know primite data types: int, float, str, bool
# what happens when we want to store multiple values?
# we could use variables such as 
a1 = 1
a2 = 2
a3 = 3
a4 = 5
a6 = 8
a7 = 13 # fibonacci sequence, but again not very efficient to store data

# instead we use lists - the main data structure in Python for sequential data
# citās valodās to sauc par array - masīvs, bet Python ir savi nosaukumi

# main idea we have a list of values
# we can access them by index
# we can append new values
# we can remove values
# we can sort values
# we can iterate over values
# we can replace values
# we can find values

# so lists are very versatile
# let's see how we can create a list

# empty list
my_list = [] # we use square brackets to denote a list
print(my_list) # we print the list

# how many elements are in the list?
print(f"Number of elements in the list: {len(my_list)}")

# let's make a shopping list
shopping_list = ['apple', 'banana', 'milk', 'bread']
print(shopping_list)
# how many elements are in the list?
print(f"Number of elements in the list: {len(shopping_list)}")

# so syntax for creating lists is as follows:
# we use square brackets
# we separate elements by commas

# let's see number_list
# we could do this
number_list = [1, 2, 3, 5, 8, 13]
print(number_list)
# how many elements are in the list?
print(f"Number of elements in the list: {len(number_list)}")

# we can have mixed lists - Python places no restrictions on the data types
mixed_list = [1, 'apple', 3.14, True] # we have 4 different data types in one list
# generally it is not recommended to mix data types - it is better to have lists of the same data type
print(mixed_list)
# how many elements are in the list?
print(f"Number of elements in the list: {len(mixed_list)}")