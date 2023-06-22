# Sets in Python

# Sets are unordered collections of unique elements
# somewhat similar to dictionaries but only keys
# plus we have set operations like union, intersection, difference etc
# sets are mutable
# sets are not hashable so we can't have sets of sets
# sets are not ordered so we can't index them
# sets are not sequences so we can't slice them
# sets are iterable / but order is not guaranteed
# sets are great for:
# - membership testing - quick O(1) operation instead of O(n) for lists, tuples
# - removing duplicates from sequences - convert to set and then back to original type
# - computing mathematical set operations like union, intersection, difference etc

# so let's create a set
my_set = {1, 2, 3, 4, 5, 3, 2, 2} # we run out of parentheses reusing {} for sets
print(my_set) # so we have only unique elements, order is not guaranteed!
# let's add some elements to my_set
my_set.add(6)
my_set.add(3) # nothing happens since 3 is already in the set
print(my_set)
# let's remove some elements from my_set
my_set.remove(3)
print(my_set)
# so removing non existing element will raise KeyError
try:
    my_set.remove(3)
except KeyError as e:
    print(f"KeyError: {e}")

# i can update my_set with any iterable
my_set.update([3,3,1,200,32,1,3])
print(my_set)
# so we have only unique elements, order is not guaranteed!
my_set.update("Valdis") # string is iterable why not
print(my_set)
# usually we want same type of elements in a set

# so if I want to get rid of duplicates in a list
my_list = [1, 2, 3, 4, 5, 3, 2, 2]
print(my_list)
my_set = set(my_list)
print(my_set)
# and if I want to get back to list
my_list = list(my_set) # i could have sorted here if I wanted
print(my_list)
# i could have done this in one line
my_list.append(5)
my_list.append(6)
print(my_list)
my_list = list(set(my_list))
print(my_list)

# again I can create set from any iterable with set(iterable)
# iterable - range, list, tuple, string, dictionary.keys(), dictionary.values(), etc
numbers_0_11 = set(range(12))
print(numbers_0_11)

# existance testing is very fast in sets
# constant time O(1) for sets vs O(n) for lists
print(5 in numbers_0_11) # even if set was 1000000 elements it would be fast
# for list it would be slow

# let's iterate over a set
for number in numbers_0_11: #again order is not guaranteed!
    print(number, end=' ')
print()

# turns out there is a set comprehension
# very similar to dictionary comprehension
# we can create a set from any iterable
# we can use any expression to create a set

# let's create a set from a list of numbers

numbers = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
my_set = {number for number in numbers} # so only unique elements
my_dict = {number : number**2 for number in numbers} # so only unique elements
# compare with list and dictionary comprehensions
# i would have used set(numbers) but this is just an example
print(my_set)
print(my_dict)

# now we get to set operations

# subset
# set1 <= set2
num_3_7 = {3, 4, 5, 6, 7}
print(num_3_7 <= numbers_0_11) # so all elements of num_3_7 are in numbers_0_11
print(num_3_7.issubset(numbers_0_11)) # same as above
# proper subset
# set1 < set2 
print(num_3_7 < numbers_0_11) # so all elements of num_3_7 are in numbers_0_11
# but num_3_7 is not equal to numbers_0_11
# so num_3_7 is a proper subset of numbers_0_11
print(num_3_7 < num_3_7) # so num_3_7 is not a proper subset of itself

# similarlly we have superset and proper superset
# set1 >= set2
print(numbers_0_11 >= num_3_7) # so all elements of num_3_7 are in numbers_0_11
print(numbers_0_11.issuperset(num_3_7)) # same as above
# proper superset
# set1 > set2
print(numbers_0_11 > num_3_7) # so all elements of num_3_7 are in numbers_0_11
# but num_3_7 is not equal to numbers_0_11
# so num_3_7 is a proper superset of numbers_3_7
print(num_3_7 > num_3_7) # so num_3_7 is not a proper subset of itself

num_5_9 = {5, 6, 7, 8, 9}
print(num_5_9 < numbers_0_11) # so all elements of num_5_9 are in numbers_0_11

# now let's go to union
# Latvian: apvienojums
# set1 | set2
# set1.union(set2)
print(num_3_7, num_5_9)
print(num_3_7 | num_5_9) # so we have all elements from either or both sets
print(num_3_7.union(num_5_9)) # same as above
num_3_9 = num_3_7 | num_5_9 # saving result to a new set
print(num_3_9)

# intersection 
# Latvian: šķēlums
# set1 & set2
# set1.intersection(set2)
print(num_3_7, num_5_9)
print(num_3_7 & num_5_9) # so we have only elements that are in both sets
print(num_3_7.intersection(num_5_9)) # same as above
num_5_7 = num_3_7 & num_5_9 # saving result to a new set
print(num_5_7)

# difference
# Latvian: starpība
# set1 - set2
# set1.difference(set2)
print(num_3_7, num_5_9)
print(num_3_7 - num_5_9) # so we have only elements that are in num_3_7 but not in num_5_9
print(num_3_7.difference(num_5_9)) # same as above
num_3_4 = num_3_7 - num_5_9 # saving result to a new set
print(num_3_4)
num_8_9 = num_5_9 - num_3_7 # saving result to a new set
# so difference is not symmetric!
print(num_8_9)

# we do have symmetric difference
# Latvian: simetriskā starpība
# set1 ^ set2
# set1.symmetric_difference(set2)
print(num_3_7, num_5_9)
print(num_3_7 ^ num_5_9) # so we have only elements that are in num_3_7 or num_5_9 but not in both
print(num_3_7.symmetric_difference(num_5_9)) # same as above
num_3_4_8_9 = num_3_7 ^ num_5_9 # saving result to a new set
print(num_3_4_8_9)
# same as union of differences
print((num_3_7 - num_5_9) | (num_5_9 - num_3_7)) # note that resulting order is not guaranteed


# what other operations do we have?
# we can check if two sets are disjoint
# Latvian: disjunkts
# set1.isdisjoint(set2)
print(num_3_7, num_5_9)
print(num_3_7.isdisjoint(num_5_9)) # so they are not disjoint
print(num_3_7.isdisjoint(num_8_9)) # so they are disjoint

# equality
# set1 == set2
print(num_3_7, num_5_9)
print(num_3_7 == num_5_9) # so they are not equal

num_3_7_copy = num_3_7.copy() # so we have a copy of num_3_7
print(num_3_7_copy)

print(num_3_7 == num_3_7_copy) # so they are equal contents but not the same object
print(num_3_7 is num_3_7_copy) # so they are not the same object
# reminder is checks for memory address (id)

num_3_7.clear() # so we have an empty set
print(num_3_7)
print(num_3_7_copy) # so num_3_7_copy is not affected