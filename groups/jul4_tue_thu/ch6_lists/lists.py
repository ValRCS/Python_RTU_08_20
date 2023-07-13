# let's talk about list in Python
# we use list to store multiple values - preferably of the same type
# in many languages lists are called arrays - usually fixed size and fixed type

# why do we need lists at all?
# let's store some variables
a1 = 5
a2 = 10
a3 = 15
a4 = 20
# ...
a100 = 500
# let's not go there
# what do we do when we need to store 1000 variables? or 1 million?
# lists are a way to store multiple values in one variable

# as soon as we have two or more similar variables we should consider using a list

# philosophically lists should be used for similar values
# in practice Python lets you store different types in the same list
# we can store strings, numbers, booleans, even other lists, and other data structures, even functions

# let's start with a simple blank list
my_list = []
print(my_list)
print(type(my_list))

# unlike strings lists are mutable - we can change contents of elements in the list
# also we lists have dynamic size - we can add and remove elements

my_list.append(5) # adds 5 to the end of the list - import - IN PLACE - modifies the list itself
print(my_list)
my_list.append(10)
print(my_list)
# i can add other types
my_list.append("Valdis")
print(my_list)
my_list.append(True)
print(my_list)
# we can add other lists
my_list.append([1,2,3])
print(my_list) # in general let's not store too many different types in one list

# we can start with some values
# let's make a list of beers
beers = ["Tērvetes", "Brālis", "Piebalgas", "Bauskas", "Valmiermuižas"]
# name of the list in plural - typical name for a list
# we can print the whole list
print(beers)
# let's add another beer
beers.append("Užavas")
print(beers)

# how many beers do we have?
print(len(beers)) # len is a function that returns the length of the list
# we can access individual elements of the list by their index
# index starts at 0 - so first element is at index 0
print(beers[0]) # Tērvetes
# just like for strings we have negative indexing as well starting from -1 and going backwards
print(beers[-1]) # last element - Užavas
# let's get last 6 letters of 2nd to the last beer
print(beers[-2][-6:]) # muižas - we acces the second to last beer and then get last 6 letters

# slicing also works on lists
print(beers[1:3]) # Brālis, Piebalgas # because those are 2nd and 3rd elements, 
# 4th element with index 3 is not included

# we can also reverse using slicing
reversed_beers = beers[::-1] # and save the result in a new variable
print(reversed_beers)

# what happens if we try to access out of bounds index?
try:
    print(beers[100]) # IndexError: list index out of range
except IndexError as ie: # ie is just a variable name
    print(ie)

# but just like with strings we can use slicing to get a part of the list not worrying about the length
print(beers[1:100]) # we get all the beers from 1 to the end (as long as we have less than 100 beers)

# we can iterate/loop over lists
for beer in beers: # typical to name the list in plural and element in singular
    print(f"I am drinking {beer} alus")

# we can change elements in the list
beers[0] = "Cēsu" # we can change the first beer
print(beers)
# but I want Tērvetes back
# i can also insert new elements in the list at any position not just append to the end
beers.insert(3, "Tērvetes") # we insert Tērvetes at index 3 - so 4th element
# all the elements that were after index 3 are shifted to the right by one
print(beers)

# we can add add multiple elements to the list
beers.extend(["Aldaris", "Bauskas"]) # we add two elements to the end of the list
# so extend added elements flat to the end of the list
print(beers)
# compare to append
beers.append(["Aldaris", "Bauskas"]) # we add one element to the end of the list
# so append added a list as one element to the end of the list
print(beers)

# we can remove elements from the list
last_beers = beers.pop() # pop removes the last element from the list and returns it
# in this case last element was a list as well
print(last_beers)
print(beers)
# so if we want to pop first element we need to specify index
first_beer = beers.pop(0) # we remove the first element from the list and return it
print(first_beer)
print(beers) # first element is gone
# there is also del keyword to delete elements from the list
# delete just deletes does not return the element
# let's delete 2nd to last
del beers[-2]
print(beers)
# in general operations towards the end of a list will be faster than towards the beginning
# TODO run some tests on timing

# we can also remove elements by value
beers.remove("Bauskas") # removes the first element with value "Bauskas"
print(beers)

# we can look up methods with dot point notation beers. will show us all the methods in VS Code and most IDEs

# we can also use + to add elements to the list
beers = beers + ["Labietis", "Mītavas"] # we add two elements to the end of the list
# so we created a new list and assigned it to the same variable name this is OUT OF PLACE 
print(beers)
# i could have cut the list with slice and added new elements in the middle
new_beers = beers[:3] + ["Aldaris", "Bauskas"] + beers[3:]
print(new_beers) # this is a new list

# let's count how many Bauskas we have
print(new_beers.count("Bauskas")) # 2 # counts only exact matches

# how bout I wanted to count which beers start with B
count = 0
for beer in new_beers:
    if beer.startswith("B"):
        print(f"Found {beer} starting with B")
        count += 1
print(count)

# how about saving those beers in a new list
b_beers = []
for beer in new_beers:
    if beer.startswith("B"): # can use any logic you want here
        b_beers.append(beer)
# note there is also a shorter way to do this with list comprehension
print(b_beers)

# besides counting we could just check if something is in a list
print("Bauskas" in new_beers) # True

# I should mention that checking for existence in a list is slow for large lists if no match is found early
# in computer science terms this is O(n) operation

# we can sort lists
# let's sort OUT OF PLACE first
sorted_beers = sorted(new_beers) # we create a new list and assign it to a new variable
print(sorted_beers)
print(new_beers) # original list is unchanged
# so sorted is OUT OF PLACE
# also note strings were sorted alphabetically - lexicographically
# how about we sort by length - simple we add a key
sorted_by_len = sorted(new_beers, key=len) # we create a new list and assign it to a new variable
print(sorted_by_len)

# we can also sort IN PLACE
new_beers.sort() # we sort the list in place - this modifies the original list!!
print(new_beers)

# we can also reverse the list - IN PLACE
new_beers.reverse() # we reverse the list in place - this modifies the original list!!
print(new_beers)

# there is also reversed function that returns a reversed iterator - it does not modify the original list
# also it does not return a list but an iterator!
# we use that on large lists when itereating over the list
for beer in reversed(new_beers):  # waster than new_beers[::-1] - which creates a new list
    print(beer)

# for iterating it is tempting to use range(len(beers)) but that is not pythonic
# we can iterate over the list directly
for index, beer in enumerate(new_beers): # index and beer are just variable names
    print(f"Beer at index {index} is {beer}")

# again we could use range(len)
for index in range(len(new_beers)):
    print(f"Beer at index {index} is {new_beers[index]}")
# possible but not Pythonic - more C like

# now let's talk about copy versus alias
# let's create a new list overwriting the old one
beers = ["Brālis", "Piebalgas", "Tērvetes", "Valmiermuižas", "Bauskas", "Aldaris", "Bauskas"]
# now let's create a true copy
beers_copy = beers.copy() # we create a new list and assign it to a new variable - so call shallow copy
# now beers and beers_copy are two different lists in two different places in memory
# so if we change one the other is not affected
beers_copy[0] = "Cēsu"
print(beers_copy)
print(beers)
# compare with alias
beers_alias = beers # we assign beers to beers_alias - basically we have two names for the same list
# so if we change one the other is affected
beers_alias.append("Labietis")
print(beers_alias)
print(beers) # is affected
# beers copy is not affected
print(beers_copy)

# we can compare lists
print("Are contents the same", beers == beers_copy) # False
beers_copy.append("Labietis")
# get Brālis back into beers_copy
beers_copy[0] = "Brālis"
print("Are contents the same", beers == beers_copy) # True
# however they are still different lists
print("Are they the same list", beers is beers_copy) # False
# now with alias
print("Are they the same list", beers is beers_alias) # True because they are the same list

# finally we can clear the list IN PLACE
beers.clear() # we clear the list in place - this modifies the original list!!
print(beers)

# now let's talk about list function 
# we can create a list from a string
characters = list("Valdis")# we create a new list and assign it to a new variable
print(characters)
# i can change the last letter to m
characters[-1] = "m"
print(characters)
# i can create a new string from the list
new_string = "".join(characters) # we join the list into a string by joining each character with "" - nothing
print(new_string)

# we can use list to get a list of numbers from range - range is a generator - not a list
numbers = list(range(10)) # we create a new list and assign it to a new variable
print(numbers)
# we can find the smallest number in the list
print(min(numbers))
# we can find the largest number in the list
print(max(numbers))
# we can find the sum of all numbers in the list - again this requires a list of numbers - floats are ok
print(sum(numbers)) # tehcnically I could pass start value to sum but let's not go there

# i could get min and max from list of strings as well... it will use lexigraphical order
print(min(new_beers))
print(max(new_beers))
# sum will not work on strings
# print(sum(new_beers)) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# int because 0 is the start value for sum
# use join for string lists


