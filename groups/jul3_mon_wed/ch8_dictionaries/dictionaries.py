# let's talk about dictionaries in Python
# docs: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# dictionaries are key-value pairs
# other languages might call them maps, hashes, associative arrays

# main idea is that we can quickly find a value by a key - so called O(1) operation
# even if I have billions of key-value pairs I can find a value by key in one step

# main properties of dictionaries 
# 1. unordered - we cannot rely on order of keys in dictionary 
# ( technically order of insertion is preserved in Python 3.7+)
# 2. mutable - we can change the contents of dictionary values
# 3. keys are unique - we cannot have two keys with same name
# 4. dynamic - we can add new keys to dictionary on the fly also delete keys
# 5. keys are immutable - we cannot use lists as keys, but we can use tuples, strings, numbers
# 6. values can be anything - we can have lists, dictionaries, numbers, strings, tuples as values
# 7. keys are case sensitive - "Valdis" is not the same as "valdis"
# 8. iterable/loopable - we can loop over keys, values or both
# 9. we can have dictionaries of dictionaries
# 10. we can have list of dictionaries

# so blank dictionary is just {} - curly braces
my_dict = {}
print(my_dict, type(my_dict))
# also we can use dict() constructor blank_dict = dict()

# let's find out length of dictionary
print(f"I have {len(my_dict)} items my_dict") # note different use of curly braces

# let's add some key-value pairs to our dictionary
my_dict["name"] = "Valdis"
my_dict["age"] = 50
my_dict["city"] = "Rīga"
my_dict["country"] = "Latvia"
# in this case all keys are strings - but they could also be numbers or tuples other immutable types

print(my_dict, len(my_dict))

# so I can get a value by key - this is a very fast operation
print(my_dict["name"], my_dict["age"])

# let's make a phone book dictionary - with some fake data
# i will strings as keys and numbers as values
# for phone numbers values could have been strings if 0 in front is important

phone_book = {
    "Valdis" : 26451112,
    "Līga" : 29111111,
    "Līva" : 29222222,
    "Līvija" : 29333333
}

print(phone_book)

# what happens if I know another Valdis?
phone_book["Valdis"] = 22112211 # this will overwrite the previous value
print(phone_book)
# so if I truly have two Valdise I could use their first and last names as keys

# add Valdis Z.
phone_book["Valdis Z."] = 22112211
print(phone_book)

# it so happens both Valdis have the same phone number
# again values can be anything and they can overlap

# so how about if Valdis has 3 phone numbers?
# then I use list as value
phone_book["Valdis"] = [26451112, 22112211, 29292929]
print(phone_book)

# let me go back to single phone number for Valdis
phone_book["Valdis"] = 26451112 # overwrites the list
print(phone_book)

# so how about a loop over dictionary
# we can loop over keys
for key in phone_book: # this is same as phone_book.keys()
    print(key, phone_book[key]) # we know for sure that key exists in dictionary

# we can also loop over values
for value in phone_book.values():
    print(value) # we do not know the key her

# in fact we can get a list of keys or values separately
phone_names = list(phone_book.keys()) # keys is not a list but we can make it into a list
print(phone_names) # this list has nothing to do with original dictionary

# similarly we can get a list of values
phone_numbers = list(phone_book.values())
print(phone_numbers)

# let's add a two new names to our phone_names
phone_names.append("Rūta")
phone_names.append("Rūdolfs")
print(phone_names) # just a list

# I will add also a single phone number to our phone_numbers
phone_numbers.append(29292929)
print(phone_numbers)

# let's length of our lists
print("Length of phone_names", len(phone_names))
print("Length of phone_numbers", len(phone_numbers))

# we can create a dictionary from two lists using zip
new_phone_book = dict(zip(phone_names, phone_numbers))
print(new_phone_book)
# length of new_phone_book should be same as length of smaller list

# we can also loop over both keys and values at the same time
for key, value in phone_book.items(): # key, value are just variable names - could k,v or anything else
    print(key, value)

# how about getting some non existing key?
try:
    print(phone_book["Voldemārs"])
except KeyError as e:
    print("Sorry I do not have that key", e)

# i can check for existence of key in dictionary
if "Voldemārs" in phone_book:
    print("I have Voldemārs and its value i,", phone_book["Voldemārs"])
else:
    print("I do not have Voldemārs in my phone book")

needle = "Valdis"
if needle in phone_book:
    print(f"I have {needle} in my phone book and its value is {phone_book[needle]}")
else:
    print(f"I do not have {needle} in my phone book")

# if i have to do this often there is a built in method get
print(phone_book.get("Valdis")) # same as phone_book["Valdis"]
print(phone_book.get("Voldemārs")) # same as phone_book["Voldemārs"] but without error - returns None
# i can even provide a default value for when there is no key
print(phone_book.get("Voldemārs", 11881188)) # same as phone_book["Voldemārs"] but without error - returns None

# get is slightly slower than direct access but it is safer

# so checking for key with in is very fast O(1) operation
# checking for some specific value is much slower O(n) operation - need to check all values

# let's check some specific value
if 26451112 in phone_book.values(): # again this would be slow in a large dictionary
    print("I have 26451112 in my phone book")
else:
    print("I do not have 26451112 in my phone book")

# how about deleting a key-value pair
print(phone_book)
del phone_book["Valdis Z."] # this will delete the key-value pair 
print(phone_book)
# however it will throw an error if key does not exist
try:
    del phone_book["Voldemārs"]
except KeyError as e:
    print("Sorry I do not have that key", e)

# we can also use pop method to delete a key-value pair
deleted_value = phone_book.pop("Valdis") # this will delete the key-value pair and return the value IN PLACE
print(deleted_value)
print(phone_book)

# we can also use popitem to delete a random key-value pair
# no idea where this would be useful - ideas?

# one thing we have to be careful when looping through dictionary
# if we change the dictionary size during the loop we will get an error - or unexpected results
# so if i I add or delete keys then I should loop over copy of dictionary

# so let's delete keys over 5 characters long
for key in list(phone_book.keys()): # we need to make a copy of keys
    if len(key) > 5:
        del phone_book[key]

# alternatively I could iterate copy of keys

for key in phone_book.copy().keys(): # we need to make a copy of keys
    if len(key) > 5:
        del phone_book[key]

print(phone_book)

# i can change values as much as I want, but keys should be immutable
phone_book["Valdis"] = 26451112
print(phone_book)
# so let's multiple all values by 100

for key in phone_book: # no need for copy since I am mutating values not keys
    phone_book[key] *= 100

bad_value = 26451112
# let's delete all values that are equal to bad_value
for key in list(phone_book.keys()): # we need to make a copy of keys
    if phone_book[key] == bad_value:
        del phone_book[key] # this will change the size of dictionary


