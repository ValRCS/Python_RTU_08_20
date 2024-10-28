# we covered dictionaries and lists and tuples
# sets are last major data type in python
# sets - Latviski: kopas
# less used but quite useful

# in one way sets are like dictionary keys - they are unique
# they are also unordered

# they are mutable - you can add and remove elements
# but elements themselves are immutable inside the set
# elements are UNIQUE - main property of sets
# this means we can use sets to remove duplicates from lists and tuples
# sets are created with curly braces {} or set() function
# sets also offer set operations like union, intersection, difference and symmetric difference

# finally sets offer instant membership testing just like dictionaries.keys()

# let's make a set from string "abracadabra"

# we can use curly braces
# but we have to be careful because curly braces are also used for dictionaries
# we can also use set() function

unique_characters = set("abracadabra")
print(unique_characters) # {'a', 'b', 'c', 'd', 'r'} # ORDER IS NOT GUARANTEED

# let's check if a is in our set
print('"a" in unique_characters', "a" in unique_characters) # True
# ABOVE is instant operation in very large sets unlike lists or tuples

# thus if you have to often check if element is in a collection, use sets

# let's make a set of unique foods
food_list = ["apple","banana", "apple", "banana", "grapes", "banana", "grapes", "apple", "grapes", "banana", "apple", "grapes"]
unique_foods = set(food_list)
print(unique_foods) # {'banana', 'apple', 'grapes'}

# now I need a list of unique foods I simply convert it back to list
unique_foods_list = list(unique_foods)
print(unique_foods_list) # ['banana', 'apple', 'grapes']

# if I wanted a sorted list
unique_foods_list.sort()
print(unique_foods_list) # ['apple', 'banana', 'grapes']

# let's try this again in one line
also_unique_foods_list = list(set(food_list)) # food_list could be a tuple
also_unique_foods_list.sort()
print(also_unique_foods_list) # ['apple', 'banana', 'grapes']

# note there is no index for sets
try:
    print(unique_foods_list[0]) # will work since it is a list
    print(unique_foods[0]) # will raise TypeError
except TypeError as e:
    print(e)

# however we can loop through sets
# again order is not guaranteed!
for food in unique_foods:
    print(food)

# if we need order then we convert it to list

# we could also use {} when creating sets
# note it is similar to dictionaries
# except we do not have key-value pairs!

unique_numbers = {1,2,4,2,1,5,7,7,1}
print(unique_numbers) # {1, 2, 4, 5, 7} # order not guaranteed

# let's do some set operations now

# first some numbers
numbers_1_12 = set(range(1,13)) # 13 is not included
even_numbers = set(range(2,13,2)) # 13 is not included
odd_numbers = set(range(1,13,2)) # 13 is not included

print(numbers_1_12) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
print(even_numbers) # {2, 4, 6, 8, 10, 12}
print(odd_numbers) # {1, 3, 5, 7, 9, 11}

# are even numbers subset of numbers 1-12?
print("even_numbers subset of numbers_1_12?", even_numbers.issubset(numbers_1_12)) # True
# even better we can use shorthand
print("even_numbers <= numbers_1_12?", even_numbers <= numbers_1_12) # True
# we also have strict subset
print("even_numbers < numbers_1_12?", even_numbers < numbers_1_12) # True
# strict will not be true for same sets
print("even_numbers < even_numbers?", even_numbers < even_numbers) # False

# similarly we can check for superset the other way around
print("numbers_1_12 superset of even_numbers?", numbers_1_12.issuperset(even_numbers)) # True
# we also have shorthand
print("numbers_1_12 >= even_numbers?", numbers_1_12 >= even_numbers) # True
# strict superset
print("numbers_1_12 > even_numbers?", numbers_1_12 > even_numbers) # True
# again strict will not be true for same sets
print("even_numbers > even_numbers?", even_numbers > even_numbers) # False

# now let's create an intersection of even and all numbers
# means we only keep those that are in both sets

# first I will add some numbers to even_numbers so let's say 14 and 16
even_numbers.add(14) # adds one if it is not in the set
# we could also use update method
even_numbers.update([8, 14, 16,18]) # adds multiple elements
print(even_numbers) # {2, 4, 6, 8, 10, 12, 14, 16, 18} # order not guaranteed

# now we can do intersection - šķēlums
even_and_numbers = even_numbers.intersection(numbers_1_12)
print(even_and_numbers) # {2, 4, 6, 8, 10, 12} as rest are not in both sets
# we even have a shorthand
even_and_numbers = even_numbers & numbers_1_12 # note single &
print(even_and_numbers) # {2, 4, 6, 8, 10, 12}

# we can also do union - apvienojums
even_or_numbers = even_numbers.union(numbers_1_12)
print(even_or_numbers) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18} # no duplicates
# we also have shorthand
even_or_numbers = even_numbers | numbers_1_12 # note single | for union
print(even_or_numbers) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18}

# now difference - starpība
even_not_numbers = even_numbers.difference(numbers_1_12)
print(even_not_numbers) # {16, 18, 14} # only in even_numbers

# difference is no commutative
# try the other way around but let's use shorthand
numbers_not_even = numbers_1_12 - even_numbers
print(numbers_not_even) # {1, 3, 5, 7, 9, 11} # only in numbers_1_12

# finally we have a symmetric difference - simetriskā starpība
# it is like difference but only unique elements
# that are not in both sets
# so it is like union - intersection
even_or_numbers_not_and = even_numbers.symmetric_difference(numbers_1_12)
print(even_or_numbers_not_and) # {1, 3, 5, 7, 9, 11, 14, 16, 18} # no duplicates
# of course we have shorthand
even_or_numbers_not_and = even_numbers ^ numbers_1_12 # note single ^ for symmetric difference
print(even_or_numbers_not_and) # {1, 3, 5, 7, 9, 11, 14, 16, 18}

# again just like lists and tuples = is not copy

numbers_1_12_alias = numbers_1_12
numbers_1_12_alias.add(13)
print(numbers_1_12) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}

# now if you want a copy then use copy method
numbers_1_12_copy = numbers_1_12.copy()
numbers_1_12_copy.add(14)
print("ALIAS", numbers_1_12_alias) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13} # no change
print("OG", numbers_1_12) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13} # no change
print("COPYCAT", numbers_1_12_copy) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14} # 14 added

# finally we can remove elements from sets
# we can use remove method
numbers_1_12_copy.remove(14)
print(numbers_1_12_copy) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13} # 14 removed
# if we try again it will raise KeyError
try:
    numbers_1_12_copy.remove(14)
except KeyError as e:
    print(e)

# of course we could have checked if element is in set before removing

# we can also use discard method
# it will not raise error if element is not in set
numbers_1_12_copy.discard(14) # no error

# finally we can clear the set
numbers_1_12_copy.clear()
print(numbers_1_12_copy) # set() # empty set
# original set is not affected
print(numbers_1_12) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13} # no change

# when should you use sets?

# when you need to remove duplicates
# when you need to check if element is in collection
# when you need to perform set operations like union, intersection, difference, symmetric difference