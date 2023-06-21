# Sets in Python

# Sets are unordered collections of unique elements
# in some ways similar to just keys in a dictionary
# sets are mutable
# sets are unordered
# sets are unique ! - well suited for finding unique elements
# sets are iterable - we can loop over them in unpredictable order
# sets are not indexed - we cannot access elements by index
# sets are not sliced - we cannot slice them
# sets are great for membership testing - is element in set or not
# sets are great for removing duplicates from lists
# sets are great for mathematical set  operations like union, 
# intersection, difference

# creating a set
s = set() # empty set
print(s)
# how to add elements to a set
s.add(1)
print(s)
# notice that we do not have a key value pair
# we can add multiple elements at once
s.update([1,2, 2,3,4,5,6,7,8,9,10,9])
print(s) # loosk ordered but it is not!

# we can also create a set from a list
my_list = [1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3]
print(my_list)
my_set = set(my_list)
print(my_set) # so unique elements only
# i can go back to list from set
my_new_list = list(my_set)
print(my_new_list) # i could do usual list operations on my_new_list, 
# sort, reverse etc.

# i can create a set from a string
my_string = "Valdis Saulespurēns"
my_string_set = set(my_string)
print(my_string_set) # notice order is not preserved!
# so if i wanted a list of unique letters in my string
my_unique_letters = list(my_string_set)
print(my_unique_letters)
# i could also sort my_unique_letters
my_unique_letters.sort() # or sorted(my_unique_letters)
print(my_unique_letters)
# then i could join my_unique_letters back into a string
my_unique_string = "".join(my_unique_letters)
print(my_unique_string)

# i can use curly braces to create a set
my_set = {1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3}
# again unique elements only
print(my_set)
# {} expects individual elements
# set expects iterable (list,string,tuple, range, etc.)

# we can check if element is in a set
print(1 in my_set) # THIS is FASTER(O(1) - constant time) than list or tuple
# in list or tuple we would have to loop over all elements(O(n) - linear time)
# if you need to check if element is in a collection many times
# then set will be faster than list or tuple
# downside you need to create a set first
# this becomes important once you have many elements in your collection

# we can also check if element is not in a set
print(1 not in my_set) # again faster than list or tuple

# we can loop over a set
for element in my_set:
    print(f"Element {element} is in my_set") # order is not guaranteed!!

# we can also use set comprehension -rarely used
my_set = {x for x in range(1,11)}
print(my_set)

# now we move onto set operations
# we can check if some set is subset of another set
num_3_7 = set(range(3,8))
print(num_3_7)
print(f"Is {num_3_7} subset of {my_set}? {num_3_7.issubset(my_set)}")
num_6_12 = set(range(6,13))
print(num_6_12)
print(f"Is {num_6_12} subset of {my_set}? {num_6_12.issubset(my_set)}")
# we have shorter syntax for subset
print(f"Is {num_3_7} subset of {my_set}? {num_3_7 <= my_set}")
# how about set itself
print(f"Is {my_set} subset of {my_set}? {my_set <= my_set}")
# however we can use proper subset
print(f"Is {my_set} proper subset of {my_set}? {my_set < my_set}")

# we can check if some set is superset of another set
print(f"Is {my_set} superset of {num_3_7}? {my_set.issuperset(num_3_7)}")
print(f"Is {my_set} superset of {num_6_12}? {my_set.issuperset(num_6_12)}")
# again we have shorter syntax
print(f"Is {my_set} superset of {num_3_7}? {my_set >= num_3_7}")
# how about set itself
print(f"Is {my_set} superset of {my_set}? {my_set >= my_set}")
# however we can use proper superset
print(f"Is {my_set} proper superset of {my_set}? {my_set > my_set}")

# let's do union of two sets
# UNION Latviešu valodā apvienojums
# union means all elements from both sets
num_5_9 = set(range(5,10))
print(num_5_9)
print(f"Union of {num_3_7} and {num_5_9} is {num_3_7.union(num_5_9)}")
# we can also use | operator
print(f"Union of {num_3_7} and {num_5_9} is {num_3_7 | num_5_9}")

# let's do intersection of two sets
# INTERSECTION Latviešu valodā šķēlums
# intersection means elements that are in both sets, but not just one
print(f"Intersection of {num_3_7} and {num_5_9} is {num_3_7.intersection(num_5_9)}")
# we can also use & operator
num_5_7 = num_3_7 & num_5_9
print(f"Intersection of {num_3_7} and {num_5_9} is {num_5_7}")

# again elements of set could be anything

# let's do difference of two sets
# DIFFERENCE Latviešu valodā starpība
# difference means elements that are in one set but not in another
print(f"Difference of {num_3_7} and {num_5_9} is {num_3_7.difference(num_5_9)}")
# how about vice versa
print(f"Difference of {num_5_9} and {num_3_7} is {num_5_9.difference(num_3_7)}")
# this means difference is not symmetric!!
# we can also use - operator
num_3_4 = num_3_7 - num_5_9
print(f"Difference of {num_3_7} and {num_5_9} is {num_3_4}")
num_8_9 = num_5_9 - num_3_7

# let's do symmetric difference of two sets
# SYMMETRIC DIFFERENCE Latviešu valodā simetriskā starpība
# symmetric difference means elements that are in one set or another but not both
print(f"Symmetric difference of {num_3_7} and {num_5_9} is {num_3_7.symmetric_difference(num_5_9)}")
# we can also use ^ operator
num_3_4_8_9 = num_3_7 ^ num_5_9 # same as symmetric_difference
print(f"Symmetric difference of {num_3_7} and {num_5_9} is {num_3_4_8_9}")

# so union of set differences is symmetric difference
# let's compare union of set differences and symmetric difference
union_of_differences = num_3_4.union(num_8_9)
print(f"Union of differences {union_of_differences}")
print(f"Symmetric difference {num_3_4_8_9}")
print(f"Union of differences {union_of_differences == num_3_4_8_9}") # True even if order is different

# more set methods
print(f"Are sets {num_3_7} and {num_5_9} disjoint? {num_3_7.isdisjoint(num_5_9)}") # False

# finally we can clear a set
num_3_7.clear() # IN PLACE
print(num_3_7) # set()
