# tuples in Python are immutable lists

# so anything we can do with lists we can do with tuples except change them
# in general tuples will be faster than lists
# Latviešu valodā: kortežs
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
# in fact we do not need to use () to create a tuple
my_other_tuple = 4, 5, 6, 7, 8
print(my_other_tuple)

# philosophically tuples should be used for data that might have different data types
# lists should be used for data that is of the same type
# in real life we will use lists more often than tuples
# tuples are used in Python for example when we want to return multiple values from a function

# so let's go over basic things we can do with tuples
# we can get the length of a tuple
print("Length", len(my_tuple))
# we can get the first element of a tuple
print(my_tuple[0]) # so first element is at index 0 - here it is a number 1
# we can get the last element of a tuple
print(my_tuple[-1])
# we can get a slice of a tuple
print(my_tuple[1:3]) # so 2nd and 3rd element
# how about reversing a tuple?
print(my_tuple[::-1]) # so we get a new tuple with elements in reverse order
# again original tuple is not affected
# so just like strings tuples are immutable
# we would need to save the reversed tuple to a new variable
reversed_tuple = my_tuple[::-1]
print(reversed_tuple)

# if all values are numbers we can do some math
print("Summa", sum(my_tuple))
print("Max", max(my_tuple))
print("Min", min(my_tuple))

# iterating over a tuple
for element in my_tuple:
    print(f"Element is {element}")

# we can also iterate over a tuple using index
# not Pythonic but sometimes useful
for index in range(len(my_tuple)):
    print(f"Element at index {index} is {my_tuple[index]}")

# instead I would use enumerate() function
for index, element in enumerate(my_tuple):
    print(f"Element at index {index} is {element}")

# tuples appear in many places in Python
# as list of tuples when we iterate over a dictionary
my_dict = {"Valdis": 29290000, "Līga": 29290001, "Zane": 29290002}
my_items = list(my_dict.items()) # so we get a list of tuples
print(my_items)
# so indexing for tuples works just like for lists
print(my_items[0]) # so first element is a tuple
print(my_items[0][-1]) # so last element of the first tuple is a number

# another use of tuples is returning multiple values from a function

def calc_min_max(number_list):
    return min(number_list), max(number_list)

my_min, my_max = calc_min_max(range(10)) # technically we are unpacking a tuple
print(my_min, my_max)

my_result_tuple = calc_min_max([3,2,6,1,7,8,9,0])
print(my_result_tuple)

# so if we have a number of values we can unpack them into a tuple
# we can also convert a tuple into a list
my_list = list(my_tuple)
print(my_list)
# so i could change some values in my list
my_list[0] = 100
print(my_list)
# then I could convert my list back to a tuple
my_tuple = tuple(my_list)
print(my_tuple)

# more on unpacking we can use it to swap values
a = 2000
b = 3000
print(a, b)
a, b = b, a # without temp variable which is the old way
print(a, b)
# in above example we created a tuple on the right side
#  and unpacked it into variables on the left side
# we could have used parentheses to make it more clear but it is not necessary

# we could unpack more values
a, b, c, d, e = my_tuple # i do need to know how many values are in my tuple
print(a, b, c, d, e)

# we can also use * to unpack a tuple
# so if we have a tuple with many values we can unpack some of them
# and then use * to get the rest of the values

first, *rest, last = my_tuple # *rest will be a list of values
print(first, last)
print(rest) # so rest is a list of values

# how about adding two tuples together?
print(my_tuple + my_other_tuple) # so we get a new tuple with all the values - original tuples are not affected

# we can use tuples as keys in dictionaries
my_tuple_key = "Valdis", "Latvia"
another_tuple_key = "Valdis", "USA"
my_dict = {my_tuple_key: 29290000, another_tuple_key: 29290001}
print(my_dict)

# it should be noted that to use tuples as keys in dictionaries you need to have immutable values

# yes tuples can hold mutable values such as list and dictionaries

my_tuple = (1, 2, 3, [4, 5, 6], {"Valdis": 29290000, "Līga": 29290001, "Zane": 29290002})
print(my_tuple)
# so my tuple holds a list and a dictionary as values and they can be changed
# tuple itself will hold references to those values - dictionary and list
# so tuple itself is immutable but the values it holds can be mutable

# we can use IN PLACE methods on mutable values in a tuple
my_tuple[-1]["Valdis"] = 29290003
print(my_tuple)
# i can even update my dictionary
my_tuple[-1].update({"Līga": 29290004, "Maija": 29290005})
print(my_tuple)
# similarly I can use IN PLACE methods on my list
my_tuple[-2].append(-5) # same as my_tuple[3].append(7)
my_tuple[-2].extend([10,-2,9000])
print(my_tuple)
# i can sort my list
my_tuple[-2].sort()
print(my_tuple)
# i can't reassign a  new list to my_tuple[3] but I can change the values in the list
# same goes for dictionary
# i can even clear all values from list and dictionary
my_tuple[-2].clear() # IN PLACE method for list
my_tuple[-1].clear() # IN PLACE method for dictionary
print(my_tuple)
# i can start adding new values to my list and dictionary
my_tuple[-2].append(100)
my_tuple[-1]["Valdis"] = 29290000
print(my_tuple)
