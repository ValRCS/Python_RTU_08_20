# # # # # # Sets (kopas)
# # # # # # unordered
# # # # # # unique items
# # ### mutable
# # # # # # use: get rid of duplicates, membership testing
# # # # # # https://docs.python.org/3/tutorial/datastructures.html#sets
# # # # # # https://realpython.com/python-sets/

chars = set("abracadabra")  # you pass an iterable to set(iterablehere)
print(chars)
print(len(chars))
print('a' in chars) # set membership check will be O(1) so faster than in lists and tuples
print('e' in chars)
print('bl' in chars)
print("".join(chars)) # so with join we will create a string from set
# print(sorted("".join(chars))) # not quite
print("".join(sorted(chars)))
# # # # # # # # print(list(chars))
# # # # # # # # # # recipe to sort characters unique characters into a list an then make a string
# print("".join(sorted(set("abraValdiscadbra"))))
# # # # # # # str(chars)  # not much point in this one
words = ['potato', 'potatoes', 'tomato', 'Valdis', 'potato']
unique_words = set(words)
print(unique_words)
# print(unique_words[1]) # 'set' object is not subscriptable
list_unique_words = list(unique_words)
print(list_unique_words)
print(list_unique_words[1])

# # # # # # # # difference between set() and {setitem}
new_set = {'kartupelis'} # so not a dictionary but set
print(new_set)
food_item_set = set(['kartupelis']) # same as above 
print(food_item_set)
chars = set("kartupelis")  # you pass an iterable to set(iterablehere)
print(chars)

# # # Set operations
print(new_set == food_item_set)
# # # # # # above two sets are equal


numbers = set(range(12))
print(numbers) # might print in order but the order is not guaranteed
n3_7 = set(range(3, 8))
print(n3_7)
print(4 in numbers)
print(4 in n3_7)
# # # # # # # below two are equal
print(n3_7.issubset(numbers))
print(numbers.issubset(numbers))
print(n3_7 <= numbers)  # this lets you have equal sets
print(n3_7 < numbers ) # this will be false if both sets are equal
print(numbers < numbers) # this should be false
n_8_15 = set(range(8,16))
print(n_8_15 < numbers) # False because not all of n_8_15 is in numbers
# # # # # # numbers <= numbers
# # # # # # numbers < numbers
# # # # # # # below two are euqal
print(numbers.issuperset(n3_7))
print(numbers >= n3_7)
print(numbers > n3_7)

n5_9 = set(range(5, 10))
print(n5_9)
# # # # # # # below two are equal
print(n3_7 | n5_9)
print(n3_7.union(n5_9))
# n3_9 = n3_7 | n5_9  # i could chain union more sets here
# print(n3_9)
print(n3_7 | n5_9 | set(range(30, 35)))
# # # # # # # below two are equal
n5_7 = n3_7 & n5_9
print(n3_7.intersection(n5_9))
print(n5_7)

n3_4 = n3_7 - n5_9  # this is not simmetrical
print(n3_4)
n8_9 = n5_9 - n3_7  # this is not simmetrical
print(n8_9, n5_9.difference(n3_7))
# # # # # # # simmetrical difference
n_sim = n3_7 ^ n5_9
print(n_sim, n3_7.symmetric_difference(n5_9))
print(n3_4.isdisjoint(n8_9))

print(n_sim)
n_sim.update([4, 1, 6, 1, 6, 13, 2]) # so n_sim update is IN PLACE
print(n_sim)
n_sim.update([-5, 5, 3, 6, 6, 8, 99, 9, 9])
print(n_sim)
n_sim.remove(13)  # Raises KeyError if you try to remove nonexistant value
print(n_sim)
# n_sim.remove(13)  # Raises KeyError if you try to remove nonexistant value
# print(n_sim)
n_sim.discard(13)  # No error
print(n_sim)
new_set = n3_4 | n5_9 | set([45,7,4,7,6]) | n_sim
print(new_set)
unsorted_list = list(new_set)
print(unsorted_list)
new_list = sorted(new_set)
print(new_list)
# new_set = set(new_list) # going back to set does not guarantee order!
# print(new_set)


random_pop = n_sim.pop()
print(random_pop, n_sim)
# # random_pop = n_sim.pop()
# # print(random_pop, n_sim)
n_sim.clear() # can clear contents completely
print(n_sim)
# # # # # # there is also a frozenset which is just like set, but immutable
# # # n_sim.
