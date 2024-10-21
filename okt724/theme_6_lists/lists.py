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
shopping_list = ['apple', 'banana', 'milk', 'bread', 'butter', 'cheese', 'eggs'] # we create a list
print(shopping_list)
# how many elements are in the list?
print(f"Number of elements in the list: {len(shopping_list)}")

# so syntax for creating lists is as follows:
# we use square brackets
# we separate elements by commas

# let's see number_list
# we could do this
fibonacci_sequence = [1, 2, 3, 5, 8, 13]
print(fibonacci_sequence)
# how many elements are in the list?
print(f"Number of elements in the list: {len(fibonacci_sequence)}")

# we can have mixed lists - Python places no restrictions on the data types
mixed_list = [1, 'apple', 3.14, True] # we have 4 different data types in one list
# generally it is not recommended to mix data types - it is better to have lists of the same data type
print(mixed_list)
# how many elements are in the list?
print(f"Number of elements in the list: {len(mixed_list)}")

# we can use list function to create list from range
number_list = list(range(10)) # we create a list from 0 to 9
print(number_list)
# how many elements are in the list?
print(f"Number of elements in the list: {len(number_list)}")

# i can create a list out of a string
name = "Valdis"
name_list = list(name) # we create a list from the string
print(name_list)
# how many elements are in the list?
print(f"Number of elements in the list: {len(name_list)}")

# let's go back to our shopping list
print(shopping_list)

# indexing in lists
# indexing starts at 0 - just like in strings
# we can access elements by index

print(f"First element in shopping_list: {shopping_list[0]}")
# how about last element?
# easiest way is to use negative index
print(f"Last element in shopping_list: {shopping_list[-1]}")
# of course I could have used len(shopping_list) - 1
# here it would have been 3
print(f"Last element in shopping_list: {shopping_list[len(shopping_list) - 1]}")
# above is not recommended way to get last element

# again use whichever indexing method you are most comfortable with

# similar to strings we can slice lists

# let's get first 2 elements of our shopping list
print(f"First 2 elements in shopping_list: {shopping_list[:2]}")

# how about last 2 elements?
print(f"Last 2 elements in shopping_list: {shopping_list[-2:]}")

# how about 2nd and 3rd element
# we could do this
print(f"2nd and 3rd element in shopping_list: {shopping_list[1:3]}")
# above example we use 1:3 because we want elements at index 1 and 2 (index 3 is not included)

# we can also use step
# let's get every second element
print(f"Every second element in shopping_list: {shopping_list[::2]}")

# how every element except first and last?
print(f"Every element except first and last in shopping_list: {shopping_list[1:-1]}")

# of course we can reverse the list using same method as with strings
print(f"Reversed shopping_list: {shopping_list[::-1]}")
reversed_list = shopping_list[::-1] # we can store the reversed list in a new variable
print(reversed_list)
# original is not changed!
print(shopping_list)

# let's see how we can modify lists
# we can change elements by index
# let's change milk to orange juice
# first let's find the index of milk (we know it is 2 but let's go with it)
print(shopping_list)
print(f"Index of milk: {shopping_list.index('milk')}")
shopping_list[2] = 'orange juice' # we change the element at index 2
print(shopping_list)
# so lists are mutable - we can change individual elements!

# how about adding elements?
# let's imagine our other half added coffee to the list
shopping_list.append('coffee') # we add coffee to the end of the list
print(shopping_list) # notice something?

# append is our first instruction that changes the list in place 
# IN PLACE means that the original list is changed

# compare to index method which does not change the list - that would not be a good idea

# i can add another item to the end
shopping_list.append('tea')
print(shopping_list)

# let's try using append to add two items at once
try:
    shopping_list.append('sugar', 'salt') # we try to add two items at once
except TypeError as e:
    print(f"Error: {e}")

# we are smart so we will put sugar and salt in a list
shopping_list.append(['sugar', 'salt']) # we add a list to the end of the list
# however the result is not what we expected
print(shopping_list)
# we've gotten a nested list - not what we wanted most likely

# let's see how could we get to salt here
# we could do this
print(shopping_list[-1]) # we get the last element 
print(shopping_list[-1][-1]) # we get the last element of the last element

# okay let's get rid of this nested list
# we could simply return the list without last element
# two ways
new_shopping_list = shopping_list[:-1] # we remove the last element by overwriting the list
print("NEW", new_shopping_list)
# notice the original list is unchanged
print("OLD", shopping_list)
# instead we could also use pop method - which removes and returns the last element
popped_item = shopping_list.pop() # we remove the last element IN PLACE and also return it
# it is not required to save the popped item but we can
print(f"Popped item: {popped_item}")
print(shopping_list) # now our original list is without the last element
# let's pop first element - it is a bit slower
also_popped_item = shopping_list.pop(0) # we remove the first element IN PLACE and also return it
print(f"Popped item: {also_popped_item}")
print(shopping_list) # now our original list is without the

# okay let's go back to adding sugar and salt at once to the list
# we could use extend method
# so extend will flatten the list and add all elements to the end of the list
shopping_list.extend(['sugar', 'salt']) # we add all elements from the list to the end of the list
print(shopping_list)

# look what happens when we extend with a string instead of appending
shopping_list.extend('pepper') # we add all elements from the string to the end of the list
print(shopping_list)
# let's get rid of last 6 elements
shopping_list = shopping_list[:-6] # we remove the last 6 elements by overwriting the list with a slice

# slicing creates a new list so that is usually a good way to remove elements
print(shopping_list)

shopping_list.append('banana') # we add banana to the end of the list
print(shopping_list)
# let's count how many bananas we have
print(f"Number of bananas: {shopping_list.count('banana')}")

# we can also use + to combine lists
new_items = ['cookies', 'chocolate']
shopping_list = shopping_list + new_items # we combine the lists and overwrite the original list
# so similar to extend but we create a new list and then overwrite the original list
print(shopping_list)

# let's keep only foods that start with b
foods_starting_with_b = [] # we create an empty list
for item in shopping_list: # for each item in the list
    if item.startswith('b'): # if the item starts with b
        # crucially we need to know that item is a string
        foods_starting_with_b.append(item) # we add the item to the new list

print(foods_starting_with_b)

# let's see if we have mixed list of strings and numbers
mixed_list = ['apple', 3.14, 'banana', 42, 'cherry']
# we want to only keep strings
string_list = [] # we create an empty list
for item in mixed_list: # for each item in the list
    if isinstance(item, str): # if the item is a string
        # of course I could add another if statement for strings of certain length etc
        string_list.append(item) # we add the item to the new list
print(string_list)

foods_starting_with_b_alias = foods_starting_with_b # this is not a copy but an alias, data is not copied
# so we have two names for the same list
foods_starting_with_b_copy = foods_starting_with_b.copy() # we create a copy of the list, so called shallow copy
# from now on foods_starting_with_b_copy is a separate list from foods_starting_with_b not related to the original list
# we did not need copy for primitive data types because they are immutable
# but lists are mutable so we need to be careful
# now we can change the copy without changing the original

# let's add biscuits to the original list
foods_starting_with_b.append('biscuits') # we add biscuits to the end of the list

# let's see all 3 lists
print("Original", foods_starting_with_b)
print("Alias", foods_starting_with_b_alias) # alias changes because it is the same list!
print("Copy", foods_starting_with_b_copy) # copy stays the same

# let's add to alias and see what happens
foods_starting_with_b_alias.append('blueberries') # we add blueberries to the end of the list
# let's see all 3 lists
print("Original", foods_starting_with_b)
print("Alias", foods_starting_with_b_alias) # alias changes because it is the same list!
print("Copy", foods_starting_with_b_copy) # copy stays the same

# let's do some sorting
# first let's do a backup of our shopping list
shopping_list_backup = shopping_list.copy() # we create a copy of the list

# let's sort our shopping list
shopping_list.sort() # we sort the list IN PLACE - we lose the original order!
# we sort using lexicographical order for strings
print("Original sorted", shopping_list)
print("Backup", shopping_list_backup) # backup is unchanged

# i can also sort in reverse
shopping_list.sort(reverse=True) # we sort the list IN PLACE in reverse order
# we sort using lexicographical order for strings
print("Original sorted reverse", shopping_list)
# of course we could have used [::-1] to reverse the list as well but sort is more general

# now let's clear the shopping list
shopping_list.clear() # we remove all elements from the list IN PLACE - destroys whole list
# instead I could have also used shopping_list = [] but clear is more explicit
print("Cleared shopping list", shopping_list)

# let's do a restore from backup
shopping_list = shopping_list_backup.copy() # we restore the original list from the backup
print("Restored shopping list", shopping_list)

# we can insert elements at specific index
# let's say we want to insert spread after bread
# let's find index of bread
bread_index = shopping_list.index('bread') # we find the index of bread
print(f"Will insert spread after bread at index {bread_index}")
shopping_list.insert(bread_index + 1, 'spread') # we insert spread AFTER bread
# if we skipped + 1 we would insert spread BEFORE bread
print(shopping_list)

# insert is not very efficient for large lists because it has to move all elements after the index
# append at the end is much faster


