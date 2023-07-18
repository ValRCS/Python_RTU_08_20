# Sets in Python
# less used but very useful data structure

# documentation: https://docs.python.org/3/tutorial/datastructures.html#sets

# sets are unordered collections of unique elements
# Latviski - kopa
# sets are mutable - we can add and remove elements
# sets can be used to perform mathematical set operations like union, intersection, symmetric difference etc.
# sets can be used to remove duplicates from a list
# sets are great for membership testing - O(1) - very fast faster than lists, tuples which are O(n)

# sets are not indexed - we can not access elements by index

# another bad news - we run out of parentheses, brackets and braces
# solution - we use same curly braces as for dictionaries but without key value pairs

# ok let's create some sets
# we can use set() function to create a set from an iterable
unique_letters = set("abrakadabra maģija mana") # set takes any iterable as an argument
print(unique_letters) # note there is no specific order -
# we can check if letter is in the set
print("a" in unique_letters) # True
print("z" in unique_letters) # False
# both of these checks are very fast O(1) - constant time even in large sets

# let's make a number set with {}
number_set = {1,2,3,4,5,6,7,8,9,10,3,2,5,1,1,20,10}
print(number_set) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20} # but order is not guaranteed!!

foods = ["kartupelis","banāns","kafija","kartupelis", "kafija", "kafija", "kafija", "alus", "alus"]
# i pass list to set
unique_foods = set(foods)
print(unique_foods) # {'kartupelis', 'kafija', 'alus', 'banāns'} - no duplicates
# if i need some order i can convert set back to list
unique_food_list = list(unique_foods)
print(unique_food_list) # ['kartupelis', 'kafija', 'alus', 'banāns'] but i can change order

# so typical workflow to remove duplicates is:
# 1. convert list to set
# 2. convert set back to list
# 3. if order is important - sort the list

# sets can store any hashable objects
crazy_set = {True, False, 0, 0, 1,2,3,4,5,6,7,8,9,10,3,2,5,1,1,20,10,"kartupelis","banāns","kafija","kartupelis", "kafija", "kafija", "kafija", "alus", "alus"}
print(crazy_set) # {True, False, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'kartupelis', 'kafija', 'alus', 'banāns', 20}
# note no 0 or 1 because True and False are 1 and 0


# let's create a set of numbers 0 to 11
numbers = set(range(12))
print(numbers) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# i can update set with any iterable
numbers.update([3,5,12,13,14,15]) # duplicates are ignored
print(numbers) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15}

# now let's do some set operations

numbers_3_7 = {3,4,5,6,7}
numbers_5_9 = {5,6,7,8,9}
# subset
print(numbers_3_7.issubset(numbers_5_9)) # False
print(numbers_3_7.issubset(numbers)) # True
# we have shorter syntax
print(numbers_3_7 <= numbers) # True
# proper subset does not allow equality
print(numbers_3_7 < numbers) # True
print(numbers_3_7 < numbers_3_7) # False

# vice versa we have superset
print(numbers_3_7.issuperset(numbers_5_9)) # False
print(numbers.issuperset(numbers_3_7)) # True
# we have shorter syntax
print(numbers >= numbers_3_7) # True means numbers is superset of numbers_3_7
# proper superset does not allow equality
print(numbers > numbers_3_7) # True
print(numbers_3_7 > numbers_3_7) # False

# disjoint sets - no common elements
print(numbers_3_7.isdisjoint(numbers_5_9)) # False
print(numbers_3_7.isdisjoint({1,2})) # True

# union - all elements from both sets still unique
print(numbers_3_7.union(numbers_5_9)) # {3, 4, 5, 6, 7, 8, 9}
# shorter syntax with |
print(numbers_3_7 | numbers_5_9) # {3, 4, 5, 6, 7, 8, 9}
# i can save union to a variable just like any other operation
nums_3_9 = numbers_3_7 | numbers_5_9
print(nums_3_9) # {3, 4, 5, 6, 7, 8, 9}

# intersection - common elements
print(numbers_3_7.intersection(numbers_5_9)) # {5, 6, 7}
# shorter syntax with &
print(numbers_3_7 & numbers_5_9) # {5, 6, 7}
# i can save intersection to a variable just like any other operation
nums_5_7 = numbers_3_7 & numbers_5_9
print(nums_5_7) # {5, 6, 7}

# difference - elements in first set but not in second
# regular difference is not commutative
print(numbers_3_7.difference(numbers_5_9)) # {3, 4}
# we have shorter syntax with -
num_3_4 = numbers_3_7 - numbers_5_9
num_8_9 = numbers_5_9 - numbers_3_7
print(num_3_4) # {3, 4}
print(num_8_9) # {8, 9}

# finally symmetric difference - elements in either set but not in both
print(numbers_3_7.symmetric_difference(numbers_5_9)) # {3, 4, 8, 9}
# shorter syntax with ^
print(numbers_3_7 ^ numbers_5_9) # {3, 4, 8, 9}
# i can save symmetric difference to a variable just like any other operation
nums_3_4_8_9 = numbers_3_7 ^ numbers_5_9
print(nums_3_4_8_9) # {3, 4, 8, 9}

# a few more methods
# specific removal
nums_3_4_8_9.remove(8)
print(nums_3_4_8_9) # {3, 4, 9}

# pop - removes and returns an arbitrary element from the set
random_pop = nums_3_4_8_9.pop()
print(random_pop)
print(nums_3_4_8_9) 

# we have copy
nums_3_4_8_9_copy = nums_3_4_8_9.copy()
print(nums_3_4_8_9_copy)

# clear
nums_3_4_8_9.clear() # IN PLACE modification
print(nums_3_4_8_9) # set()



