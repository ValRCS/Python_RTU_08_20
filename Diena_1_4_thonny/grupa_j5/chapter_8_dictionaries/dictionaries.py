# Let's talk Python dictionaries
# Docs: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# so called key-value pairs

# main properties:
# - unordered
# - mutable
# - indexed by keys
# - keys must be unique
# - keys must be immutable (strings, numbers, tuples)
# - values can be anything
# - iterable/loopable
# - can be nested
# - can be stored in lists

# creating a dictionary
# empty dictionary
d = {}
print(d)
# we can also use dict() function
also_empty = dict()
print(also_empty)
# let's add some data to d 
d["name"] = "Valdis"
d["age"] = 44
d["city"] = "Rīga"
print(d)
# we can access data by key
print(d["name"])
# notice that we can not access by index - we use keys! 
# crucial difference from lists
# print(d[0]) # will not work - unless there was specifically made a key 0

# we gain readability 
# we keep our data together
# access is faster to specific data
# access by key is so called constant time O(1) - 
# no matter how large our dictionary is it will take the same time to access data

# we can also create a dictionary with data
# let's make a telephone book
phone_book = {
    "Valdis": 29292929,
    "Līga": 29292928,
    "Maija": 29292927
}
print(phone_book)
# let's look up my number
print(phone_book["Valdis"]) # again lookup is instant by key

# let's add a new entry
phone_book["Rūta"] = 29292926
print(phone_book)

# so how about multiple Valdises?
# we can only have one key Valdis - has to be unique
phone_book["Valdis"] = 29290000 # will overwrite previous value if it exists
print(phone_book)

# so if I want to add Valdis Zatlers I could do
phone_book["Valdis Zatlers"] = 29290001
print(phone_book)

# how about if I have multiple phone numbers?
# we could use a list as a value
phone_book["Valdis"] = [29290000, 29290002, 29290003]

print(phone_book)

# how do I get the last number from Valdis?
# so whole list would be 
print(phone_book["Valdis"])
# last number would be
print(phone_book["Valdis"][-1]) # 29290003

# how about iterating over a dictionary?
# we can iterate over keys
for key in phone_book: # this is the same as for key in phone_book.keys()
    print(f"Key is {key} and value is {phone_book[key]}")

# deconstruction of a dictionary
# i could extract keys as a list
my_keys = list(phone_book.keys()) # this list is not related to the dictionary
print(my_keys)
# i could extract all values as a list
my_values = list(phone_book.values()) # again the list is not related to the dictionary
print(my_values)

# let's add some data to my_keys
my_keys.append("Voldemārs")
print(my_keys)
print(phone_book) # phone_book is not affected by my_keys
# and again let's add some data to my_values
my_values.append(29290004)
# one more
my_values.append(29290005) # this number has no key my_keys
print(my_values)
print(phone_book) # phone_book is not affected by my_values

# constructing a dictionary from two lists
# we can use zip() function to combine two lists
# zip() will combine two lists into a list of tuples

new_phone_book = dict(zip(my_keys, my_values))
print(new_phone_book)

# now let's see what we can do about bad keys
# so if I check for a key that does not exist I get an error
try: 
    print(phone_book["Kristaps"])
except KeyError as e:
    print(f"Key {e} does not exist in our phone book")

# we could also check for existance first
if "Kristaps" in phone_book: # this check is O(1) constant time - very fast
    print(phone_book["Kristaps"])
else:
    print("Kristaps not found in phone book")

# we can also use get() method to get a value by key
# get() will return None if key does not exist

# first we can use it for me
print(phone_book.get("Valdis")) # 29290000
print(phone_book.get("Kristaps")) # None
# i can supply default value if key does not exist
print(phone_book.get("Kristaps", 1188)) # if no key Kristaps then return 1188

# how about checking for existance of some value?
# we can use values() method but it will be slower than keys()
# we could also write a loop
needle = 1188
for key in phone_book:
    if phone_book[key] == needle:
        print(f"Key {key} has value {needle}")
        break # no possible way to find more than one key
else: # no break happened
    print(f"Value {needle} not found")

# lets make a function of this
def find_key_by_value(d, needle):
    """
    Returns first key with if value is found in dictionary d,

    otherwise returns None"""	
    for key in d:
        if d[key] == needle:
            return key
    return None

print(find_key_by_value(phone_book, 1188))
# let's add 1188 value for key "info"
phone_book["info"] = 1188
print(find_key_by_value(phone_book, 1188))


# how about getting all keys with a specific value?
# lets make a function
def find_keys_by_value(d, needle):
    """
    Returns list of keys if value is found in dictionary d,

    otherwise returns empty list"""	
    keys = []
    for key in d:
        if d[key] == needle:
            keys.append(key)
    return keys # so empty list will be returned if no keys found

print(find_keys_by_value(phone_book, 1188))
# let's add 1188 value for key "zaļā lapa"
phone_book["zaļā lapa"] = 1188
print(find_keys_by_value(phone_book, 1188))

# so dictionary can contain multiple keys with the same value
# but keys have to be unique
print(phone_book)
# we can delete a key with del keyword
del phone_book["zaļā lapa"]
print(phone_book)

# now careful - potential pitfall
# now there is a question of modification of keyswhile looping through a dictionary
# let's say we want to remove all keys with value 1188
# if we need to modify a dictionary while looping through it we need to make a copy
for key in phone_book.copy(): # otherwise we would get a runtime error or unpredictable results
    if phone_book[key] == 1188:
        del phone_book[key]

print(phone_book)
# similar thing would happen if we tried to add keys while looping through a dictionary
# so we need to make a copy of keys if we want to add keys while looping through a dictionary
for key in phone_book.copy():
    if phone_book[key] == 29292928:
        phone_book[key + "2"] = phone_book[key]
print(phone_book)

# alternatively we could make a new dictionary and add keys there
new_phone_book = {"Valdis":8675309, "Valdis2": 29292928, "Rūta2": 29292926}
# then we can update our phone_book with new_phone_book
phone_book.update(new_phone_book)
# what will happen if both dictionaries have the same key?
# the value from the new dictionary will overwrite the old one
print(phone_book)

# notice since Python 3.7 dictionaries are ordered by insertion order
# if I wanted to somehow sort my dictionary by keys or values
#  I would need to make a new dictionary

# looping through keys and values at the same time
for key, value in phone_book.items(): # items() returns a list of tuples
    print(f"Key is {key} and value is {value}")


# now let's talk about dictionary comprehensions
# let's say I want a new dictionary with all values doubled
# we can use dictionary comprehension
new_phone_book = {key: value*2 for key, value in phone_book.items()}
print(new_phone_book)
# i could add some conditionals
new_phone_book = {key: value*2 for key, value in phone_book.items() if value % 2 == 0}
# above will work as long as values are numbers
print(new_phone_book)
# so all even values were doubled
# how could have we done this with a regular loop?
new_phone_book = {}
for key, value in phone_book.items():
    if value % 2 == 0:
        new_phone_book[key] = value * 2
print(new_phone_book)

# again dictionary comprehension is more compact and easier to read
# but for more complex cases we can use a regular loop

# let's look at some more dictionary methods

phone_book.clear() # clears all keys and values from dictionary IN PLACE!
print(phone_book)

# now let's set some default values
phone_book.setdefault("Valdis", 29292929) # if key exists it will not be changed
print(phone_book)
# one more time
phone_book.setdefault("Valdis", 9999) # if key exists it will not be changed
print(phone_book) # value is still 29292929

# there is also pop() method which will return a value and remove a key
saved_value = phone_book.pop("Valdis") # 29292929
# so similar to get() but pop() will remove the key just like del
print(phone_book) # empty dictionary
print(saved_value) # 29292929

# we can also popitem() which will return a random key value pair
phone_book = {"Valdis": 29292929, 
              "Rūta": 29292926, 
              "Līga": 29292927,
              "Maija": 29292925
              }
print(phone_book)
key, value = phone_book.popitem() # certain Python versions will return last item
print(key, value)
print(phone_book)

# to conclude we use dictionaries when we need to map keys to values
# keys have to be unique but values can be the same
# some say that Python is mostly written in dictionaries
# compare storing some data in a list vs dictionary

# also it is normal to have a list of dictionaries

dict_lict = [{"name": "Valdis", "phone": 29292929},
             {"name": "Rūta", "phone": 29292926},
             {"name": "Līga", "phone": 29292927}]
print(dict_lict)
# access will be fast if we know index of the dictionary we need