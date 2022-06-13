# # # # # # # # # # # # # # # Sets (kopas)
# # # # # # # # # # # # # # # unordered
# # # # # # # # # # # # # # # unique items
# # # # # # # # # # # ### mutable
# # # # # # # # # # # # # # # use: get rid of duplicates, membership testing, set operations
# # # # # # # # # # # # # # # https://docs.python.org/3/tutorial/datastructures.html#sets
# # # # # # # # # # # # # # # https://realpython.com/python-sets/

chars = set("abracadabra")  # you pass an iterable to set(iterablehere)
print(chars)
print(len(chars))
# # # use set for membership testing if you need to check for multiple values in a large data set
print('a' in chars) # set membership check will be O(1) so faster than in lists and tuples
print('e' in chars)
# print('bl' in chars)
print(str(chars)) # not quite what we need
print("".join(chars)) # so with join we will create a string from set
# # # # # # # print(sorted("".join(chars))) # not quite
print("".join(sorted(chars))) # so use this if we want sorted unique characters from our string
print(list(chars))
print(tuple(chars))
# # # # # # # # # # # # # # # # # # # recipe to sort characters unique characters into a list an then make a string
# # # # # # print("".join(sorted(set("abraValdiscadbra")))) # we staret from inner parenthesis
# # # # # # # # # # # # # # # # str(chars)  # not much point in this one
words = ['potato', 'potatoes', 'tomato', 'Valdis', 'potato', 'Valdis', 2002,2002,2022]
unique_words = set(words)
print(unique_words)
# # print(unique_words[1]) # 'set' object is not subscriptable
# # list_unique_words = list(unique_words)
# # print(list_unique_words)
# # print(list_unique_words[1])

# # # # # # # # # # # # # # # # # difference between set() and {setitem}
new_set = {'kartupelis'} # so not a dictionary but set
print(new_set)
food_item_set = set(['kartupelis']) # same as above i passed a list with one element
print(food_item_set)
chars = set("kartupelis")  # you pass an iterable to set(iterablehere)
print(chars)
# orig_list = [1,2,4,6,7,1,26,1,26, 3,4, "Valdis", "alus", "alus", True , True, True, False] # better to put same types
# # # # here True will dissappear since we already have 1 True
# # # # typical way of getting uniques
# uniq_item_list = list(set(orig_list))
# print(orig_list)
# print(uniq_item_list)


# # # # # # # # # # # Set operations
# # # # == will compare sets by items inside
print(new_set)
print(food_item_set)
print("Sets have same contents?", new_set == food_item_set)
print("Sets are actually same object in memory?", new_set is food_item_set) # is checks if variables point to same memory structure
# # # # # # # # # # # # # # above two sets are equal in content  but are two distinct data sets


numbers = set(range(12))  # from 0 to 11
print(numbers) # might print in order but the order is not guaranteed
n3_7 = set(range(3, 8))
print(n3_7)
print(4 in numbers) # remember membership testing is O(1) - very quick
print(4 in n3_7)
print("set is a subset of itself", numbers.issubset(numbers))
# # # # # # # # # # # # # # # # below two are equal
print("set 3to7 is subset of 0 to 11", n3_7.issubset(numbers))
print(n3_7 <= numbers)  # this lets you have equal sets, same as above
print(n3_7 < numbers ) # this will be false if both sets are equal
print(numbers < numbers) # this should be false
n_8_15 = set(range(8,16))
print(n_8_15 < numbers) # False because not all of n_8_15 is in numbers
# # # # # # # # # # # # # # # numbers <= numbers
# # # # # # # # # # # # # # # numbers < numbers
# # # # # # # # # # # # # # # # below two are euqal
print("0 TO 11 IS SUPERSET over 3 to 7 ", numbers.issuperset(n3_7))
print(numbers >= n3_7) # same as above just shorter
print(numbers > n3_7)

n5_9 = set(range(5, 10))
print(n5_9)
print(n3_7)
# # # # # # # # # # # # # # # below two are equal
# # with union we create a new set with ALL items from both sets
print(n3_7 | n5_9) # union of sets (all items)
print(n3_7.union(n5_9)) # same as above
n3_15 = n3_7 | n5_9 | n_8_15 # i could chain union more sets here
print(n3_15)
# # print(type(n3_9))
print(n3_7 | n5_9 | set(range(30, 35))) # i can chain |

# # # # # # # # # # # # # # # # below two are equal
# # with intersection we create a new set with items that are in both sets ONLY but not in just one
n5_7 = n3_7 & n5_9  # intersection of sets (common items) šķēlums
print(n5_7)
print(n3_7.intersection(n5_9)) # so same as above

print(n3_7 & n5_9 & {7,22,56,1,5,4,7})  # {5,7} are only values common across all 3 sets
# # careful with intersection of sets with different types
print(set() & {1,3,3,65,67,7} & {1,2,3,6,7,6}) # a gotcha what will happend when intersection with empty set?

n3_4 = n3_7 - n5_9  # difference of sets (items in first set but not in second)
print(n3_4)
n8_9 = n5_9 - n3_7  # difference is not symmetric ! elements unique to first set
print(n8_9, n5_9.difference(n3_7)) # same as above
# # # # # # # # # # # # # # # # simmetrical difference so values unique to either of the sets
n_sim = n3_7 ^ n5_9 # symmetric difference of sets (items in either set but not both)
print(n_sim, n3_7.symmetric_difference(n5_9))
print(n3_4 | n8_9) # union of sets (all items)

print(f"Sets {n3_4} and {n8_9} are disjoint? ", n3_4.isdisjoint(n8_9)) # are sets completely disjoint(different)
print(f"Sets {n3_4} and {n3_7} are disjoint?", n3_4.isdisjoint(n3_7)) # are sets completely disjoint(different)

# # # remember sets are mutable
print(n_sim)
n_sim.update([4, 1, 6, 1, 6, 13, 2]) # so n_sim update is IN PLACE using any iterable
print(n_sim)
n_sim.update([-5, 5, 3, 6, 6, 8, 99, 9, 9])
print(n_sim)
n_sim.remove(13)  # Raises KeyError if you try to remove nonexistant value
print(n_sim)
# # # # # # # # n_sim.remove(13)  # Raises KeyError if you try to remove nonexistant value
# # # # # # # # print(n_sim)
n_sim.discard(13)  # No error
print(n_sim)
# new_set = n3_4 | n5_9 | set([45,7,4,7,6]) | n_sim
# print(new_set)
new_set.clear() # clears the set IN PLACE
print(new_set)
# # # # unsorted_list = list(new_set)
# # # # print(unsorted_list)
# # # # unsorted_list.sort() # in place sort of list
# # # # print(unsorted_list)
# # # # sorted_list = sorted(new_set)
# # # # print(sorted_list)
# # # # # new_set = set(sorted_list) # going back to set does not guarantee order!
new_set = set([3,3,6,1,9,5,199,3,3,65,2])
print(new_set)


for item in new_set: # remember no order guaranteed for set, so if you want make it sorted first
    print(item)

for item in sorted(new_set): # remember no order guaranteed for set, so if you want make it sorted first
    print(item)



# # # # # # print(n_sim)
# random_pop = n_sim.pop() # removes and returns a random item from set, do not use for completely random pop
# print(random_pop, n_sim)
# # # # # # random_pop = n_sim.pop()
# # # # # # print(random_pop, n_sim)
# # my_set_copy = n_sim.copy() # shallow copy of set
# # print(my_set_copy == n_sim, my_set_copy is n_sim) # so True, False because is check for same data location
# # my_set_alias = n_sim # this is just a shortcut to original data
# # print(my_set_alias == n_sim, my_set_alias is n_sim) # so True and True since we point to same data

# # # # # n_sim.clear() # can clear contents completely
# # # # # print(n_sim)
# # # # # print(my_set_alias) # should be empty, since it points to same set we just cleared
# # # # # print(my_set_copy) # still full of data
# # # # # # # # # # # # # # # there is also a frozenset which is just like set, but immutable
# # # # # # # # # # # # n_sim.

# # # # # # # print(set(range(12)) < n3_7)
# # # # # # # print(set(range(12)).issubset(n3_7))

# # # # # # # print(set(range(12)).issuperset(n3_7))
# # # # # # # print(set(range(12)) > n3_7)