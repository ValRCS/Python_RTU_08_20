# let's talk about Python dictionaries
# docs: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# dictionaries are also called maps or associative arrays in other languages
# also hash tables

# in other key->value pairs

# main properties of dictionaries in Python
# - unordered (order of key insertion is preserved in Python 3.7+)
# - mutable - content of values can change
# - dynamic - size (so number of keys) can change during runtime
# - indexed by keys
# - keys must be unique
# - keys must be immutable (strings, numbers, tuples)
# - values can be anything
# - keys are case sensitive
# - iterable/loopable
# - can be nested - dictionary in dictionary etc
# - can be stored in a list

# dictionaries are created using curly braces {}
# empty dictionary
d = {}
print(d)
# also using dict() function would work
d = dict()
print(d)
# length of our dictionary
print(f"Our dictionary is of length {len(d)}")

# let's add some data to our dictionary

d['name'] = 'Valdis'
d['age'] = 45
d['city'] = 'Rīga'
d['country'] = 'Latvia'

print(d)

# so we can access values by their keys
print(d['name']) # so we use square brackets to access values
key_to_get = 'age' # i can also use variables to access values
print(d[key_to_get])

# crucially access of values by keys is very fast 
# in computer science terms it is O(1) constant time
# this means that even if we have a million keys in our dictionary
# it will take the same time to access a value by key

# so by using dictionary we gain the following
# - fast access to values by key
# - we can use any immutable type as a key
# - readable code

# now let's make a dictionary with some data
phone_book = {
    'Valdis': '26451111', # so values could be anything here they are strings
    'Līga': '26452222',
    # 'Liene': '26453333',
    'Līva': '26454444',
    # 'Laima': '26455555',
}
print(phone_book)
# let's get Līga's phone number
print(phone_book['Līga'])

# let's add Laima to our phone book
phone_book['Laima'] = '26455555'
print(phone_book)

# what do we do if we have multiple Valdises in our phone book?
# key could Valdis and last name
phone_book['Valdis E.'] = '26451111'
print(phone_book)
# notice that we can have duplicate values

# how about if Valdis has multiple phone numbers?
# we could use a list as a value
phone_book['Valdis E.'] = ['26451111', '26452222', '26453333']

# so how could i get last phone number for Valdis E.?
print(phone_book['Valdis E.'][2])
# or
print(phone_book['Valdis E.'][-1])

# or how about all phone numbers for Valdis E.?
print(phone_book['Valdis E.']) # returns a list

# let's iterate over our phone book
for key in phone_book: # key could be any variable name
    print(key, phone_book[key]) # so we can use key to get value
# order of keys is same as insertion order in Python 3.7+

# now let's delete Valdis E. from our phone book
del phone_book['Valdis E.']
# will raise KeyError if key is not found
# could do this to avoid KeyError
if 'Valdis E.' in phone_book:
    del phone_book['Valdis E.']
    print("Deleted Valdis E. from phone book")
else:
    print("Valdis E. not found in phone book")
print(phone_book)

# let's deconstruct our phone book
# we can get all keys
print(phone_book.keys()) # looks like list but is not
keys = list(phone_book.keys()) # so we can convert to list
print(keys) # list not related to original dictionary
# same goes for values
print(phone_book.values()) # gain not a list but something similar
values = list(phone_book.values()) # so we can convert to list
print(values) # again not related to original dictionary

# let's add some data to keys and values
keys.append('Liene')
keys.append('Pēteris')
values.append('26453333')
print(keys, "length", len(keys))
print(values, "length", len(values))

# i will create a new dictionary from keys and values
new_phone_book = dict(zip(keys, values))
print(new_phone_book)
# notice missing Pēteris
# why? because zip will stop at shortest iterable

# let's add Pēteris to our phone book
phone_book['Pēteris'] = '26455555'
print(phone_book)

# so using this approach I could reverse my dictionary
reversed_phone_book = dict(zip(phone_book.values(), phone_book.keys()))
print(reversed_phone_book)
# in reversing we could lose some data if values are not unique

# let's get a bad key from phone book
try:
    print(phone_book['Jānis']) # will raise KeyError
except KeyError:
    print("Key not found in phone book")

# we could check first
if 'Jānis' in phone_book:
    print(phone_book['Jānis'])
else:
    print("Jānis not found in phone book")

# we could use get method
print(phone_book.get('Valdis')) # returns None if key not found
print(phone_book.get('Jānis')) # returns None if key not found
# we could provide a default value
print(phone_book.get('Jānis', '1188')) # returns 1188 if key not found

# so we know we can check existance of keys
# it will very fast - O(1) constant time

# we can check for specific values
# it will be slow - O(n) linear time - needs to go through all values
print('26455555' in phone_book.values()) # True

# how about finding which keys have specific values?
needle = '26455555'
for key in phone_book:
    if phone_book[key] == needle:
        print(f"Found {needle} for key {key}")

# let's create a function out of the above
def find_keys_with_value(d, needle) -> list:
    """Returns list of keys that have needle as value"""
    found = []
    for key in d:
        if d[key] == needle:
            print(f"Found {needle} for key {key}")
            found.append(key)
    return found

print(find_keys_with_value(phone_book, '26455555'))

# how about deleting by value?
# have to be careful since values are not unique
# modifiying a dictionary while iterating over it is a bad idea

# we can use copy to store a copy of dictionary
phone_book_backup = phone_book.copy()


# careful! you need to use copy() to avoid modifying dictionary while iterating over it
for key in phone_book.copy():
    if phone_book[key] == '26455555':
        del phone_book[key]
        print(f"Deleted {key} from phone book")

print(phone_book)

# so if we expect to add or delete a key from dictionary while looping
# we should loop through a copy of dictionary

# now i can restore my phone book
phone_book = phone_book_backup.copy() # now phone_book points to a new copy of dictionary
# original phone_book is gone now
print(phone_book)

# we have dictionary comprehension
# we can create a dictionary from any iterable
# we can use any expression to create a dictionary
# we can use any function to create a dictionary

# let's create a dictionary from a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_dict = {n: n**2 for n in numbers}
print(numbers_dict)
# this is very similar to list comprehension
# also notice how we acccess dictionary values
print(numbers_dict[5]) # looks very similar to list access
# in fact here list would have been just as good
# only we skipped 0 index

# in general consequtive integers starting from 0 are not good keys
# list would be better then

# numbers as keys can be used when they are not consequtive
big_nums = [100, 200, 300, 400, 500]
big_nums_dict = {n: f"{n} squared {n**2}" for n in big_nums}
print(big_nums_dict)
# here we have int keys and string values

# we can use old dictionary to create a new one
# so here just like copy we are creating a new dictionary
# no modification of original dictionary
new_dict = {key: value for key, value in phone_book.items()}
print(new_dict)
# however we can modify values when creating a new dictionary
new_dict = {key: value + " is cool" for key, value in phone_book.items()}
print(new_dict)

# finally we can add a filter to our dictionary comprehension
# so we can filter out some keys
# here we are filtering out keys that start with V
filtered_dict = {key: value for key, value in phone_book.items() if not key.startswith('V')}
print(filtered_dict)

# we could have used regular loop to do this
filtered_dict = {}
for key, value in phone_book.items():
    if not key.startswith('V'):
        filtered_dict[key] = value
print(filtered_dict)

# again rule is similar to list comprehension
# if you need to modify values or filter out some keys
# then dictionary comprehension is a good choice
# for more complex logic use regular loop

# let's look at the few more methods
# we can clear a dictionary IN PLACE
print(phone_book)
phone_book.clear() # IN PLACE clears all values
# we could have used phone_book = {} to create a new empty dictionary
print(phone_book)

# let's use setdefault to add a new key value pair
# if key exists it will return the value
# if key does not exist it will create a new key value pair
# and return the value
print(phone_book.setdefault('Valdis', '26455555'))
print(phone_book.setdefault('Valdis', '9999'))
print(phone_book) # notice setdefault did not overwrite the value
# same as using if key in dictionary
if 'Valdis' not in phone_book:
    phone_book['Valdis'] = '26455555'

# let's add one more key value pair
phone_book['Pēteris'] = '26455555'
print(phone_book)

another_dict = {'Valdis': '1188', 'Pēteris': '1188', 'Jānis': '1188'}
phone_book.update(another_dict)
print(phone_book) # notice how update overwrites values

# finally we have pop method
# pop will return the value for the key and delete the key value pair
key, value = phone_book.popitem() # popitem will return a tuple
print(key, value)
print(phone_book)
# that brings us to tuples