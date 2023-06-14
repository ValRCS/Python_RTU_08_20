# Lists are major data structures in Python. 
# They are used to store collections of items.

# let's think about some variables with similar names
a1 = 5
a2 = 10
a3 = 15
a4 = 20
# not a good idea to keep going
# so if we need 100 of these we would need to write 100 lines of code!
# lists offer a way to store multiple values in a single variable

# lists share some similarities with strings
# both are sequences of values
# both can be indexed and sliced
# both can be iterated over with for loop
# both can be concatenated and repeated

# difference is that strings are immutable while lists are mutable
# we can store any type of data in lists

# let's start with empty list
empty_list = [] # we use square brackets to define a list
print(empty_list)

# we can also create a list with some values
my_list = [1, 2, 3, 4, 50, 20]
print(my_list)
# we can store different types of data in a list
my_list = [1, 2, 3, 4, 50, 20, "Valdis", True, False, None, 3.14]
print(my_list)
# philosophically we should strive to keep lists with same type of data
# but in practice we will have mixed lists

# we can use many of the same functions we used with strings

# len function
print(len(my_list)) # 11

# we can use in operator to check if a value is in a list
print("3 in my list", 3 in my_list) # True

# we can use indexing to get a value from a list
print(my_list[0]) # 1
# again indexing starts at 0
# we can also use negative indexes
print(my_list[-1]) # 3.14
print(my_list[-2]) # None

# crucially we can change values in a list
my_list[0] = 100
print(my_list) # [100, 2, 3, 4, 50, 20, 'Valdis', True, False, None, 3.14]

# we can also use slicing to get a sublist
print(my_list[2:5]) # [3, 4, 50]

# lets make numbers with list from range
my_list = list(range(12))
print(my_list) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# let's get last 3 elements
print(my_list[-3:]) # [9, 10, 11]

# i can always get type of a variable
print(type(my_list)) # <class 'list'>
print(type(my_list[0])) # <class 'int'>

reversed_numbers = my_list[::-1]
print(reversed_numbers) # [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# let's make a loop to print all elements of a list
for element in my_list:
    print(element, end=" ")

# how about index? - this is not good Python style - more C style
for index in range(len(my_list)):
    print(index, my_list[index])

# better would be to use enumerate function
for index, element in enumerate(my_list):
    print(f"Index {index} has value {element}")

# names index and element are not special they are just variables