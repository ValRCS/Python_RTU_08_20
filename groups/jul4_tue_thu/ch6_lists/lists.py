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
blank_list = []
print(blank_list)
# type
print(type(blank_list))