# tuples in Python
# documentation: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
# tuples are immutable lists
# Latviski: korteži

# so tuples is just a list whose size cannot be changed
# elements themselves can not be changed
# the exception is if the element is a list or dictionary or some other mutable object

# tuples are ordered
# tuples can contain duplicates
# tuples can be used as keys in dictionaries (immutable)
# tuples can be used for returning multiple values from functions
# tuples can be used for unpacking
# tuples can be used for swapping values

# philosphical question - why do we need tuples if we have lists?
# tuples are faster than lists
# tuples are safer than lists
# tuples are more memory efficient than lists
# tuples should be used when mixed data types are needed
# if you need to store a sequence of values that never change, use a tuple

# ok let's create some tuples
# we can use tuple() function to create a tuple from an iterable

empty_tuple = tuple() # empty tuple
print(empty_tuple) # () - not very useful sometimes we need a good default value
single_el_tuple = (100,) # notice the comma
print(single_el_tuple) # (100,)

normal_tuple = (1,2,3,4,5,6,7,8,9,10) # parentheses are optional
print(normal_tuple) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# i could have used range for this
normal_tuple = tuple(range(1,11))
print(normal_tuple) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# so we can not change the tuple itself
try:
    normal_tuple[3] = 300
except TypeError as e:
    print(f"Error {e} - we can not change tuple elements")

# so we can convert tuple to a list change the list and convert back to tuple
normal_list = list(normal_tuple)
print(normal_list)
normal_list[3] = 300
# let's add one more number to the list
normal_list.append(110)
print(normal_list)
# now we can convert back to tuple
normal_tuple = tuple(normal_list) 
print(normal_tuple)

# i can do usual things with tuples as with list that do not change the list
# existance

print(300 in normal_tuple) # True

# length
print(len(normal_tuple)) # 11

# if all values are numeric we also have min,max,sum functions
print(min(normal_tuple)) # 1
print(max(normal_tuple)) # 300
print(sum(normal_tuple)) # 461

# we can use slicing to get new tuples from existing tuples
# so we can slice and then combine slices
print(normal_tuple[2:6]) # (3,300, 5, 6)
# so similar to strings i could combine slices with +

# so combine's first 3 elements with number 5000 and then last 3 elements 
new_tuple = normal_tuple[:3] + (5000,) + normal_tuple[-3:]
# notice the comma after 5000 - it is important
print(new_tuple) # (1, 2, 3, 5000,  9, 10, 110)

# we can use tuples to return multiple values from functions
def min_max_sum_seq(sequence):
    return min(sequence), max(sequence), sum(sequence)
# remember last lecture!

# test
print(min_max_sum_seq(normal_tuple)) # (1, 300, 461)
print(min_max_sum_seq(range(1,11))) # (1, 10, 55)

# alternative would be to use *args to allow unlimited number of arguments
def min_max_sum_args(*args):
    return min(args), max(args), sum(args)

# test - we will need to unroll any sequence into individual arguments
print(min_max_sum_args(*normal_tuple)) # (1, 300, 461)
print(min_max_sum_args(*range(1,11))) # (1, 10, 55)
# we can provide any number of arguments
print(min_max_sum_args(1,2,3,4,5,6,7,8,9,10)) # (1, 10, 55)

# we can use tuples to unpack values
# let's inspect normal tuple again
print(normal_tuple) # (1, 2, 3, 300, 5, 6, 7, 8, 9, 10, 110)
# so we can unpack it like this
first, second, third, *rest, last = normal_tuple # notice *rest for any number of elements
# so rest will be a list of elements
# only requrement here that we have 4 elements in the tuple
# names of variables do not matter

# if we know to unpack
# we can use it to swap values without temporary variable
a = 100
b = 200
print(a,b) # 100 200
a,b = b,a # swap - technically right side is a tuple and left side is unpacking
print(a,b) # 200 100
# we can use more variables
c = 300
d = 400
e = 500
print(c,d,e) # 300 400 500
c,d,e = e,d,c # rotation, I made a tuple from 3 variables and unpacked it
# in this example d stays in the middle and unchanged

# we only have two tuple methods
# count and index
# count returns number of occurences of a value
print(normal_tuple.count(300)) # 1
# index returns index of the first occurence of a value
print(normal_tuple.index(300)) # 3

# finally let's use a tuple as a key in a dictionary

person = ("Jānis", "Bērziņš", 1980) # tuple of 3 elements
# very common to use tuples for storing data from database
# another john Bērziņš
person2 = ("Jānis", "Bērziņš", 1993) # tuple of 3 elements
# let's create a dictionary
people = {person: "Brīvibas 342", person2: "Valdemāra 118"}
# let's print it
print(people) # {('John', 'Doe', 1980): 'Brīvibas 342', ('John', 'Doe', 1993): 'Valdemāra 118'}

# there are also named tuples
# where we can access elements by name and index as well
# docs: https://docs.python.org/3/library/collections.html#collections.namedtuple