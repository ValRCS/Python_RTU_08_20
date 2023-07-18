# Let's talk about Python dictionaries
# Documentation: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Dictionaries are a data structure that allow us to store data in key-value pairs
# in other languages they are called maps, associative arrays, hashes, hashmaps, etc.

# main idea is to find value by key very quickly in constant time O(1)
# no matter how large the dictionary
# so one way lookup is very fast

# main properties of dictionaries:
# 1. unordered - technically in Python 3.7+ dictionaries are ordered by insertion order
# 2. mutable - we can change the values
# 3. keys must be unique - if we add new key-value pair with existing key, the old value is overwritten
# 4. keys must be immutable - we can't use lists as keys, but we can use tuples, strings, integers, floats, etc.
# 5. values can be anything - lists, tuples, strings, integers, floats, dictionaries, etc.
# 6. dynamic - we can add/delete new key-value pairs at any time
# 7. iterable/loopable - we can loop over keys, values, or key-value pairs
# 8. nesting - we can nest dictionaries inside dictionaries
# 9. no duplicates - we can't have duplicate keys, but we can have duplicate values
# 10. no slicing - we can't slice dictionaries, because they are unordered
# 11. we can have list of dictionaries, or dictionary of dictionaries, etc.

# so dictionaries are very flexible data structure
# some say that most of Python is written in dictionaries

# so let's create a dictionary
my_dict = {} # empty dictionary
print(my_dict)
print(type(my_dict))
# alternative would be blank_dict = dict()

# let's find out length of dictionary
print(f"Length of my_dict is {len(my_dict)}")

# let's add some key-value pairs
my_dict["name"] = "Valdis"
my_dict["age"] = 48
my_dict["city"] = "Rīga"
my_dict["country"] = "Latvia"
my_dict["food"] = "potatoes"
# so keys here are all strings
# values are a mixture of strings and integers
print(my_dict)
print(f"Length of my_dict is {len(my_dict)}")

# let's get some values out of dictionary
print(my_dict["name"]) # so lookup by key is very fast
print(my_dict["age"])

# we can start with some key-value pairs already built
# let's make a phone book
phone_book = {
    "Valdis": 12345678,
    "Līga": 87654321,
    "Maija": 55555555,
    "Ēvalds": 11111111
}
# here keys are strings, values are integers (phone numbers)
# if phone numbers could have 0 in front we would need to store them as strings
print(phone_book)

# what happens if I know another Līga?
phone_book["Līga"] = 99999999
print(phone_book)
# so keys have to be unique, if we add new key-value pair with existing key, 
# the old value is overwritten
# so for two Ligas we would need to use some other key
# so Liga Z and Liga K

# let's add some new key-value pairs
phone_book["Līga Z"] = 88888888
phone_book["Līga K"] = 77777777
print(phone_book)
# values do not have to be unique
# so we can have duplicate values, but not duplicate keys
# for example
phone_book["Līga K"] = 99999999
print(phone_book)

# how about if one user(key) has multiple phone numbers(values)?
# we can use lists as values
phone_book["Valdis"] = [12345678, 87654321,33333333]
print(phone_book)
# so lookup by key for Valdis
print(phone_book["Valdis"]) # list of phone numbers
# how about 2nd phone number for Valdis?
print(phone_book["Valdis"][1]) # so we get list and then we get 2nd element from list
# in general we want similar data types for values as well but not required

# let'' go back to single number for Valdis
phone_book["Valdis"] = 12345678
print(phone_book)

# what happens if we try to get a key that does not exist?
try:
    print(phone_book["Voldemārs"])
except KeyError as e:
    print(f"KeyError {e} happened")

# let's check for existance of some key
needle = "Valdis"
if needle in phone_book:
    print(f"Found {needle} in phone_book")
    print(f"Value for {needle} is {phone_book[needle]}")
else:
    print(f"Did not find {needle} in phone_book")

# let's make a function for this
def find_in_phonebook(phonebook, name):
    if name in phonebook:
        print(f"Found {name} in phone_book")
        print(f"Value for {name} is {phonebook[name]}")
        return phonebook[name]
    else:
        print(f"Did not find {name} in phone_book")
        return None

find_in_phonebook(phone_book, "Valdis")
find_in_phonebook(phone_book, "Voldemārs")

# turns out this is such a frequent operation that we have a method for it
# get(key, default_value) - returns value if key exists, otherwise returns default_value

print(phone_book.get("Valdis"))
print(phone_book.get("Voldemārs")) # returns None by default
# we can also provide default value
print(phone_book.get("Voldemārs", 11880000)) # returns 11880000 if key does not exist

# get is not needed if we know that key exists
# get is a bit slower than direct lookup by key

# so for example we can loop through keys
for key in phone_book: # same as phone_book.keys()
    print(f"Phone for {key} is {phone_book[key]}")
    # no need for get here because we know that key exists

# how about looping through values only - less common
for value in phone_book.values():
    print(f"Phone number is {value}")
    # we have no way of getting key here

# finally we can loop through both keys and values
for key, value in phone_book.items(): # key,value are just variable names, k,v is also common
    print(f"Phone for {key} is {value} same as {phone_book[key]}")
    # we can get both key and value

# we can create a list of keys
name_list = list(phone_book.keys()) # keys is not a list but we can make it into one
print(name_list)
# we can create a list of values
phone_list = list(phone_book.values()) # values is not a list but we can make it into one
print(phone_list)
# these lists are not attached to dictionary so if we change dictionary these lists will not change

# let's add two names to name_list
name_list.append("Rūta")
name_list.append("Rūdolfs")
print(name_list, "length is", len(name_list))
# let's add a single phone number to phone_list
phone_list.append(77777777)
print(phone_list, "length is", len(phone_list))

# let's create a new dictionary from our lists
# we zip together two iterables into one and pass to dict() constructor
new_phone_book = dict(zip(name_list, phone_list))

print(new_phone_book)
# so Rudolf did not have a matching phone number 
# so he was not added to the new_phone_book

# how about deleting some key-value pairs
del new_phone_book["Valdis"]
print(new_phone_book)
# let's delete a key that does not exist
try:
    del new_phone_book["Valdis"]
except KeyError as e:
    print(f"KeyError {e} happened")

# so we could check if key exists before deleting
if "Valdis" in new_phone_book:
    del new_phone_book["Valdis"]
else:
    print("Valdis not found in new_phone_book")

# so there is no exact counterpart to get() for deleting
# similar is pop(key) which returns value and deletes key-value pair
# let's pop Liga K
popped_number = new_phone_book.pop("Līga K")
print(popped_number)
print(new_phone_book)

# so with pop I need to provide a default value if key does not exist
popped_number = new_phone_book.pop("Līga K", 11880000)
print(popped_number) # so we get default value 11880000

# when looping and changing size of dictionary we need to be careful
# if I go through dictionary and delete some keys 
# the loop will not go through all keys

# solution loop through a copy of keys or copy of items

# let's delete all keys that start with Līg 
# we can use startswith() method for strings

for key in new_phone_book.copy().keys():
    if key.startswith("Līg"):
        del new_phone_book[key]

print(new_phone_book)
# we still have original phone_book
print(phone_book)

# also you might want to create a dictionary that contains certain values from another dictionary

# so for example I want to create a new dictionary
# that has only key-value pairs where value contain digit 1

# we will use a constructive approach start with blank dictionary 
# and add key-value pairs
# let's create a new dictionary
phone_book_1 = {}
needle = "1"
for key, value in phone_book.items(): # no copy needed because we are not deleting or adding
    if needle in str(value): # we need str() because value is a number
        phone_book_1[key] = value

print(phone_book_1)
