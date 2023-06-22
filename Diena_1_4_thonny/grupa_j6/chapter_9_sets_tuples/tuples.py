# tuples in Python

# what is a tuple?
# tuple is a collection of values
# tuple is immutable - so think fixed size list
# tuple is ordered - so we can access elements by index
# tuple can contain any type of data
# tuple is defined by comma separated values
# tuple is usually defined by () parentheses
# tuple can be defined without parentheses

# in LATVIAN we call it "kortežs"

# let's create a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
# in fact we can create a tuple without parentheses
my_tuple = 1, 2, 3, 4, 5
print(my_tuple)
# let's use tuple() to create a tuple from a string "ABCDEF"
my_tuple = tuple("ABCDAAEFGHIJK")
print(my_tuple)

# so when should tuples be uses vs lists?
# philosphical question
# tuples generally will hold heterogenous data - different types
# lists generally will hold homogenous data - same type
# tuples are immutable - so they are good for data that should not change
# there are some exceptions to this rule
# also tuples are faster then lists - not a big difference but still
# tuples are used as keys in dictionaries - not possible with lists

# so let's go over basic tuple operations
# first length
print(f"Length of my_tuple is {len(my_tuple)}")

# indexing
print(f"First element of my_tuple is {my_tuple[0]}")
print(f"Last element of my_tuple is {my_tuple[-1]}")
# also
print(f"First element of my_tuple is {my_tuple[-len(my_tuple)]}")
print(f"Last element of my_tuple is {my_tuple[len(my_tuple)-1]}") # this is not good

# slicing
print(f"First 3 elements of my_tuple are {my_tuple[:3]}")
print(f"Last 3 elements of my_tuple are {my_tuple[-3:]}")
# reversing
print(f"Reversed my_tuple is {my_tuple[::-1]}")
# again tuples are not mutable so we can't change them
# instead i would have to create a new tuple
# so let's create a new tuple with first 3 elements of my_tuple
first_3 = my_tuple[:3]
print(f"First 3 elements of my_tuple are {first_3}")

# we can use + to concatenate tuples
# so let's create a new tuple with last 3 elements of my_tuple
last_3 = my_tuple[-3:]
print(f"Last 3 elements of my_tuple are {last_3}")
# now let's concatenate first_3 and last_3
first_and_last_3 = first_3 + last_3
print(f"First and last 3 elements of my_tuple are {first_and_last_3}")
# and if i need string from this tuple just like lists we use join
new_string = "".join(first_and_last_3)
print(f"New string is {new_string}")

# if I have numeric tuple i can use min, max and sum
numbers = tuple(range(10, 100, 10)) # so 10, 20, 30, 40, 50, 60, 70, 80, 90
print(f"Numbers are {numbers}")
print(f"Min of numbers is {min(numbers)}")
print(f"Max of numbers is {max(numbers)}")
print(f"Sum of numbers is {sum(numbers)}")

# we can also use in and not in
print(f"Is 10 in numbers? {10 in numbers}")
print(f"Is 100 in numbers? {100 in numbers}")
print(f"Is 100 not in numbers? {100 not in numbers}")
# just like lists this existance check is linear (O(n)) operation
# sets and dictionaries have constant time (O(1)) existance check

# we can also use for loop to iterate over tuple
for element in my_tuple:
    print(f"Element is {element}")

# we have two methods for tuples
# count and index
# count will count how many times an element is in a tuple
print(f"Count of A in my_tuple is {my_tuple.count('A')}")
print(f"Count of Z in my_tuple is {my_tuple.count('Z')}")
# index will return index of first occurence of an element
print(f"Index of C in my_tuple is {my_tuple.index('C')}")
try: 
    print(f"Index of Z in my_tuple is {my_tuple.index('Z')}") # this will throw an error
except ValueError:
    print(f"Index of Z in my_tuple is not found")

# where else do we see tuples?
# from dictionary we get a list of tuples
# so let's create a dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
print(f"my_dict is {my_dict}")
# now let's get a list of tuples from my_dict
my_list = list(my_dict.items())
print(f"my_list is {my_list}") # so list of tuples
# i could pass this list of tuples back to dict() to create a new dictionary
my_list.append(("d", 4)) # append a new tuple to my_list
new_dict = dict(my_list)
print(f"new_dict is {new_dict}")
# often results from database queries are returned as list of tuples

# tuples are also used in functions
# when we return multiple values from a function
# we actually return a tuple
# so let's create a function that returns a tuple

def get_min_max(numbers):    
    return min(numbers), max(numbers), sum(numbers) # return a tuple size 3
# note parantheses are optional in the above return statement

# now let's call this function
# and assign the result to a tuple
# 
result = get_min_max(numbers)
print(f"Result is {result}")   

# we can unpack a tuple
# so let's unpack the result tuple
min_number, max_number, sum_number = result
# so i choose 3 variables to unpack the tuple
print(f"Min number is {min_number}")
print(f"Max number is {max_number}")
print(f"Sum number is {sum_number}")

# i can use this unpacking to swap values
# famous interview question
a = 10
b = 20 # these are just integers
print(f"a is {a}")
print(f"b is {b}")
# now let's swap them without temp variable
a, b = b, a # this is a tuple which we unpack
print(f"a is {a}")
print(f"b is {b}")
# so right side was evaluated first and then unpacked to left side

# we could use this to swap more than 2 variables
c = 30
d = 40
e = 50
f = 60
print(f"c is {c}")
print(f"d is {d}")
print(f"e is {e}")
print(f"f is {f}")
# now let's swap them without temp variable
c, d, e, f = f, e, d, c # this is a tuple which we unpack
print(f"c is {c}")
print(f"d is {d}")
print(f"e is {e}")
print(f"f is {f}")

# we can also use * to unpack a tuple when we are not sure how many elements are there

# so let's get first,second and last from numbers
first, second,  *middle, last = numbers # note the * in middle
print(f"First is {first}")
print(f"Second is {second}")
print(f"Middle is {middle}") # this is a list not tuple
print(f"Last is {last}")

# so above will work as long as we have at least 3 elements in numbers

# so while tuples are immutable
# we can have mutable elements in a tuple - such as list or dictionary
# so let's create a tuple with a list and a dictionary
my_tuple = ("Valdis", 150, [1, 2, 3], {"a": 1, "b": 2, "c": 3})
print(f"my_tuple is {my_tuple}")
# so we can not change any of the elements in my_tuple
# however if any of the elements are mutable we can adjust their contents
# using inplace methods
# so let's try to change the list
my_tuple[2].append(40)
print(f"my_tuple is {my_tuple}")
# similarly we can change the dictionary
my_tuple[3]["d"] = 4
print(f"my_tuple is {my_tuple}")

# finally we can use tuples as keys in dictionaries
# only requirement is that tuple elements are immutable - so no lists no dictionaries in those tuples
person = ("Valdis", "Programmer", 45)
print(f"person is {person}")
# now let's create a dictionary with person as key
my_dict = {person: 1, "other": 2}
print(f"my_dict is {my_dict}")

