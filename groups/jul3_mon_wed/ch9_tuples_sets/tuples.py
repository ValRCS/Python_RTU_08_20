# tuples in Python
# docs: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
# Latviski: kortēži

# easiest way to think of tuple is as fixed size list
# whose contents cannot be changed (with some exceptions)
# tuples are immutable
# tuples are faster than lists
# tuples are ordered
# tuples can be used as keys in dictionaries (immutable tuples)
# tuples can be used as default values for function arguments
# tuples can be used as return values for functions
# tuples are usually created with comma separated values

# philosophically tuples are for collection of unrelated items
# lists are for collection of similar items

# let's make a simple tuple
my_tuple = (1, 2, 3, 4, 5) # parentheses are optional
print(my_tuple, type(my_tuple))

# let's make a tuple from a list
my_list = list(range(10))
print(my_list, type(my_list))
my_tuple = tuple(my_list) # we can use tuple on any iterable (strings, lists, dictionaries)
print(my_tuple, type(my_tuple))

# typically we could convert to list to change contents
# then back to tuple if we need to
my_list = list(my_tuple)
my_list[3]  = 100
print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)

# i can not change tuple contents
try:
    my_tuple[4] = 200
except TypeError as err:
    print(err)

# we can check for existence of value in tuple
print(100 in my_tuple)

# i can loop over tuple
for item in my_tuple:
    print(item, end=" ")
print()

# i can slice tuple into a new tuple
# so i could use the same idea we used for strings to concat tuples

# let's keep only first 3 plus new value 1000 plus last 3
new_tuple = my_tuple[:3] + (1000,) + my_tuple[-3:]
# notice (1000,) is a tuple with one value
print(new_tuple)
# usual min max sum len functions work on tuples
print(min(new_tuple), max(new_tuple), sum(new_tuple), len(new_tuple))
# as long as we have numbers in tuple we can sort it
print(sorted(new_tuple)) # this will be list

# we can use tuples to return multiple values from functions
def min_max_sum(numbers):
    return min(numbers), max(numbers), sum(numbers)

print(min_max_sum(new_tuple))

# we can unpack tuples
my_min, my_max, my_sum = min_max_sum(new_tuple)

# we can use tuples to swap values

a = 10
b = 20
print(a, b)
a, b = b, a # so we created a tuple on the right side and immediately unpacked it
print(a, b)
# so above trick avoids the need for a temporary variable

# i could use it for as many variables as i want
c = 30
d = 40
e = 50
print(c, d, e)

# here I rotate the values
c, d, e = e, c, d # so we created a tuple on the right side and immediately unpacked it
print(c, d, e)

# we can use tuples as keys in dictionaries
# so we can use tuples to represent coordinates
# and use them as keys in dictionaries

# let's make a dictionary of robots

robots = {
    ("R2D2", "metal"): 10,
    ("C3PO", "metal"): 5,
    ("Wall-E", "metal"): 1
}

# access a robot
print(robots[("R2D2", "metal")])

# we could use a tuple to represent person
# and use it as a key in a dictionary
# we could use tuple to represent a point in 2D space (x, y) and so on

# now there is one tricky thing with tuples
# if tuple is storing a mutable object like a list or dictionary
# we can use IN PLACE methods on those objects and modify them
# we are not changing tuple, we are changing the object stored in tuple
# these type of tuples can not be keys in dictionaries

# let's make a tuple with some number and list and dictionary
my_tuple = (1, 2, 3, [4, 5, 6], {"name": "Valdis", "age": 99})
# size of my tuple is 5
print("Length of my tuple is", len(my_tuple), id(my_tuple))

# so my list would be 2nd to last element
print(my_tuple[-2])
# let's try to change the list
my_tuple[-2].append(7) # this works because we are not changing tuple
print(my_tuple)
# similary I can add key value pair to dictionary
# -1 refers to last element of tuple
my_tuple[-1]["city"] = "Rīga"
print(my_tuple)
# i can even clear the list
my_tuple[-2].clear()
print(my_tuple)
# i can again add to the list
my_tuple[-2].append(100)
# extend some more values
my_tuple[-2].extend([200, -300, 50])
print(my_tuple)
# i can sort them IN PLACE only
my_tuple[-2].sort()
print(my_tuple)

# so tuple is serving just as a container for other objects here

# there is also named tuple which is a bit more advanced
# docs: https://docs.python.org/3/library/collections.html#collections.namedtuple
# it lets you have names for your tuple elements as well as index

print("Length of my tuple is", len(my_tuple), id(my_tuple))
