# Sets in Python

# sets are unordered collections of unique elements
# somewhat similar to dictionary with just keys
# plus set operations such as union, intersection, difference
# sets are mutable
# sets are iterable
# sets are dynamic - can change size and contents

# where to use sets
# 1. when we need to keep track of unique elements
# 2. when we need to perform set operations
# 3. when we need fast membership testing - faster than lists or tuples

# only bad news - we run out of parentheses, brackets and braces
# so we use curly braces for sets

# let's make a simple set
my_set = {1, 2, 3, 4, 5, 3, 2, 1, 100, 200, 300, 100, 200, 300}
print(my_set, type(my_set))
# notice how duplicates are removed
# sets are unordered so we can not index into them
# also order is not guaranteed to be the same as we created the set

# i can use set on any iterable such as string, range, list, tuple etc

unique_letters = set("Valdis Saulespurēns")
print(unique_letters) #notice no specific order
# in fact order could change if we run this again
foods = ["saldējums", "kafija", "kūka", "saldējums", "kafija", "kūka", "kafija", "kūka", "kafija", "kūka"]
unique_foods = set(foods)
print(unique_foods)
# then I can go back to list if I need to
unique_foods_list = list(unique_foods)
print(unique_foods_list)

# so for quick membership testing sets are great
# same speed as keys in dictionaries - O(1) constant time
# so if i have 1 million items in set it will take same time to find any of them
# compare this to lists where it will take on average 500,000 tries to find an item
# cost of course is time to create the set and also memory to store it

# what can we store in a set?
# any immutable object can be stored in a set
# so lists and dictionaries can not be stored in a set
# but say tuples can be stored in a set also strings, numbers, booleans etc

crazy_set = set([True, 1, 2, 3, "Valdis", "Saulespurens", (1, 2, 3), True, False, 1, 2, 0,  3, 1, 2, 3])
print(crazy_set) # notice no 0 why? because False and 0 are the same in Python

# so now let's do some set operations

# lets make a set from numbers 0 to 11
numbers_0_11 = set(range(12))
print(numbers_0_11)

numbers_3_7 = set(range(3, 8))
print(numbers_3_7)

# so let's check if numbers_3_7 is a subset of numbers_0_11
print("numbers_3_7 are subset of numbeers_0_11", numbers_3_7.issubset(numbers_0_11))
# ther is a shorter way to write this
print("numbers_3_7 are subset of numbeers_0_11", numbers_3_7 <= numbers_0_11)
# we also have strict subset
print("numbers_3_7 are strict subset of numbeers_0_11", numbers_3_7 < numbers_0_11)
# strict subset will be false on
print("Numbers_0_11 are strict subset of numbeers_0_11", numbers_0_11 < numbers_0_11)

# vice versa we can superset
print("Numbers_0_11 are superset of numbeers_3_5", numbers_0_11 >= numbers_3_7)
print("Numbers_0_11 are superset of numbeers_3_5", numbers_0_11.issuperset(numbers_3_7))
# strict superset
print("Numbers_0_11 are strict superset of numbeers_3_5", numbers_0_11 > numbers_3_7)

# let's make a set of numbers 5 to 9 inclusive
numbers_5_9 = set(range(5, 10))
print(numbers_5_9)

# so let's start with union
# union is all elements from both sets without duplicates!
print("Union of numbers_3_7 and numbers_5_9", numbers_3_7.union(numbers_5_9))
# there is a shorter way to write this
print("Union of numbers_3_7 and numbers_5_9", numbers_3_7 | numbers_5_9)
# i could save the result in a new set
numbers_3_9 = numbers_3_7 | numbers_5_9
print(numbers_3_9)

# intersection is all elements that are in both sets (common elements)
print("Intersection of numbers_3_7 and numbers_5_9", numbers_3_7.intersection(numbers_5_9))
# there is a shorter way to write this
print("Intersection of numbers_3_7 and numbers_5_9", numbers_3_7 & numbers_5_9)
# again i can save the result in a new set
numbers_5_7 = numbers_3_7 & numbers_5_9
print(numbers_5_7)

# difference is all elements that are in one set but not in the other
print("Difference of numbers_3_7 and numbers_5_9", numbers_3_7.difference(numbers_5_9))
# so difference is not symmetric
# we can also use - operator for difference for reverse difference
print("Difference of numbers_5_9 and numbers_3_7", numbers_5_9 - numbers_3_7)

# now finally there is symmetric difference
# symmetric difference is all elements that are in one set or the other but not both
print("Symmetric difference of numbers_3_7 and numbers_5_9", numbers_3_7.symmetric_difference(numbers_5_9))
# there is a shorter way to write this
print("Symmetric difference of numbers_3_7 and numbers_5_9", numbers_3_7 ^ numbers_5_9)

# we can combine multiple sets
number_set = numbers_3_7 | numbers_5_9 | set(range(100,120)) | set(range(95,105)) | set(range(-5,5))
print(number_set)
# again if I need order then I convert to list or tuple(immutable list)

# so i can iterate over a set
for number in numbers_5_9:
    print(number)
# order is not guaranteed

# let's say I have a list of sets
list_of_sets = [numbers_3_7, numbers_5_9, numbers_0_11] # tuples would work too
# i can use set.union to combine all sets in the list
print(set.union(*list_of_sets)) # so this will UNROLL the list into separate arguments

# alternative would be to create a loop
empty_set = set()
for my_set in list_of_sets:
    empty_set = empty_set.union(my_set)
    # so here i can do something with each set
print(empty_set) #Not so empty anymore

# i have copy
empty_set_copy = empty_set.copy()
print(empty_set_copy)
# i have clear

empty_set.clear() # IN PLACE
print(empty_set)
print(empty_set_copy) # still full

# there is even set comprehension
# so we can create a set from a list or any other iterable/loopable
my_set = {number for number in range(10)} # very similar to dictionary comprehension
# i would have used set(range(10)) but this is just for demo
 
# i can update set with another set
my_set.update(set([1,5,15]))
print(my_set)