# let's talk about Python list data structure
# we use lists to store multiple values in a single variable in order to work with them

# what happens if we do not have a list...
a1 = 1
a2 = 2
a3 = 3
a4 = 4
#...
a100 = 100
# let's not do that..
# it will not scale well if we need to work with 1000 or 1000000 values
# in general as soon as we have two or more similar variables we should consider using a list

# philosophically lists are meant for similar values
# however we can store different values in a list - anything we want
# we can store strings, numbers, other lists, dictionaries, objects, functions, etc.

# we can create a list by using square brackets []
my_list = []
print(my_list)
# type
print(type(my_list))

# unlike strings lists are mutable
# we can change the values in a list
# we can change list length - that is add or remove values

# we can append values to a list
my_list.append(10) # crucially append returns None and modifies the list in place
# this is so called IN PLACE modification
print(my_list)
# we can append multiple values
my_list.append(20)
my_list.append(30)
print(my_list)
# I can append any type of value
my_list.append('hello')
my_list.append(True)
my_list.append([1,2,3])
my_list.append(None)
my_list.append(3.1415926)
print(my_list) # not a great list we have a potpourri of values - mixed types

# we can of course iterate over a list
for element in my_list: # element is just an arbitrary name - could be any valid variable name
    # let's print element and its type
    print(f"element: {element} type: {type(element)}")

# i could start with a ready list
# let's create a list of numbers
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)
# how about a larger list of numbers
# let's use range function and convert range to a list
big_numbers = list(range(1,1_000_001)) # so from 1 to 1 million
# note creating truly big lists will take time and memory - be careful with 100s of millions of elements
# print length of big_numbers
print(len(big_numbers))

# we can access elements in a list by using index
# index is a number that represents position of an element in a list
# index starts at 0 just like in strings

# let's access first element in numbers list
print(numbers[0]) # 1
# let's access last element in numbers list
print(numbers[9], numbers[-1]) # 10

# same out of range rules apply as with strings
# print(numbers[10]) # IndexError: list index out of range
try:
    print(numbers[10]) # this would be 11th element in the list
except IndexError as e:
    print(e)

# we can use list to convert string to a list of characters - ministrings
name = 'Valdis'
name_list = list(name)
print(name_list) # ['V', 'a', 'l', 'd', 'i', 's']

# lists are mutable - we can change individual elements
# let's change first element in numbers list
numbers[0] = 100
print(numbers)

# let's change last element in name_list to m
name_list[-1] = 'm'
print(name_list)
# lets create a new string from name_list
name_dative = ''.join(name_list) # so joining by empty string
print(name_dative) # for join to work list had to have all string elements

# let's remove some number from numbers
# i can remove by value - first one to be found
numbers.remove(5) # will look for 5 and remove it
# again remove is IN PLACE - it modifies the list
print(numbers)
# raises ValueError if value not found
try:
    numbers.remove(5)
except ValueError as e:
    print(e)

# so we could check before if we do not want to use try except
if 5 in numbers:
    print(f"Fives are in {numbers}")
    numbers.remove(5)
else:
    print(f"No fives in {numbers}")

# be a bit careful with checking for values in lists
# it takes linear time to check for values in a list
# meaning Python potentially has to go through the whole list to check if value is there

# we can also remove by index
# let's remove 3rd element
del numbers[2] # here 3rd element holds 3
print(numbers)
# again raises IndexError if index is out of range
try:
    del numbers[100]
except IndexError as e:
    print(e)

# we can also use pop method to remove by index
last_value = numbers.pop() # by default pop removes last element
print(last_value) # so we popped 10
print(numbers) # 10 is gone
# pop modifies the list IN PLACE - by removing last element
# pop also returns the value that was removed
# pop also has optional index parameter
# so we can pop by index
third_value = numbers.pop(2) # so we pop 3rd element here it is 4
# so i could use pop instead of del and just not save the value
print(third_value)
print(numbers)

# we can also insert values in a list
# insert takes two parameters - index and value
numbers.insert(2, 300) # so we insert 300 at index 2
# values to the right of index will be shifted to the right
print(numbers)

# we can insert multiple values at once
numbers.append([1,2,3]) # so we append a list as a single element
print(numbers) # not quite what we wanted
# we could access last element and change it
# lets just delete it
numbers.pop() # same as del numbers[-1]
print(numbers)

# so I want to add a list and add it flatly
numbers.extend([1,2,3]) # so we extend by a list
print(numbers)
# extend again is IN PLACE - it modifies the list

# we can also use + operator to add lists
numbers = numbers + [4,5,6] # so we add two lists together
# so works similar to extend but is OUT OF PLACE
# difference is that I am creating a new list and assigning it to numbers
# i could also use shorthand
numbers += [7,8,9]
print(numbers)

# let's sort our list
sorted_list = sorted(numbers) # so we sort numbers and assign it to sorted_list
print(sorted_list)
# original
print(numbers)
# i can also use sort method - IN PLACE modification
numbers.sort() # changes the list in place
print(numbers)

# now we can compare our lists by values inside
print("Lists hold same values", numbers == sorted_list) # True - same values in our lists
# however the lists are not the same in memory
print("List are actualy same in memory", numbers is sorted_list) # False - different objects in memory

# let's try sorting list of different types
mixed_list = [1,2,3,4,5,6,7,8,9,10,'Valdis','Ala','Zorro','Batman']
print(mixed_list)
# so we can sort this list
try:
    mixed_list.sort() 
except TypeError as e:
    print(e) # TypeError: '<' not supported between instances of 'str' and 'int'

# we could sort by their string conversion
mixed_list.sort(key=str) # str conversion is unlikely to fail
print(mixed_list) # notice 10 after 1 but before 2 
# so we can sort by string representation of numbers

# more about list copying and aliases
list_alias = numbers # so we assign numbers to list_alias , both point to same list
# print whether lists have same values and same identity
print("Lists hold same values", numbers == list_alias) # True - same values in our lists
print("List are actualy same in memory", numbers is list_alias) # True - same object in memory

list_copy = numbers.copy() # so we copy numbers to list_copy - so called shallow copy
print("Lists hold same values", numbers == list_copy) # True - same values in our lists
print("List are actualy same in memory", numbers is list_copy) # False - different objects in memory

# so we can modify list_copy without affecting numbers
list_copy.append(1000)
print(list_copy) # this will be changed
print(numbers) # this will not be changed
# print alias
print(list_alias) # this will not be changed

# now let's append to alias
list_alias.append(2000)
print(list_alias) # this will be changed
print(numbers) # this will be changed
print(list_copy) # this will not be changed

# of course normal slicing will work with lists
# lets make numbers from 10 to 200 with step 10
numbers = list(range(0, 201, 10))
print(numbers)
# so we can slice
print(numbers[2:5]) # so we get 20,30,40 and 6th element with index 5 is not included
# we can also slice with step
print(numbers[::2]) # so we get every second element 0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200

# we can also slice with negative step
# so we can reverse
print(numbers[::-1]) # so we get reversed list
reversed_list = numbers[::-1] # so we assign reversed list to reversed_list
print(reversed_list)
# print original list
print(numbers)
# also I can use reverse in place with reverse method
numbers.reverse() # so we reverse the list IN PLACE - modifies the list
print(numbers)

numbers.append(110)
numbers.append(110)
print(numbers)
 # should be 3 since we had 1 and added 2 more
print(numbers.count(110)) # so we get 3

# finally we can clear our list
# we end up with empty list
numbers.clear()
print(numbers) 