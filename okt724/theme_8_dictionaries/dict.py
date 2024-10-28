# Mēs zinam par virknēm - sarakstiem un kortežiem. 
# Bet mēs nezinām par vēl vienu datu struktūru, kas saucas "vārdnīca" (dictionary).

# Pamatdoma vārdnīcai ir tāda, ka tā sastāv no pāriem "atslēga: vērtība".
# So in English dictionary is a collection of key-value pairs.
# Primary purpose of dictionary is to quickly find a value by its key.
# In Computer Science terms it is a hash table with O(1) complexity for main operations.
# In normal language terms it is like a real dictionary where you look up a word and find its definition.
# It does not matter how big the dictionary is, it will always take the same time to find a word.
# It could be million or even billion words, but it will still take the same time to find a word.

# some properties of dictionaries:
# - they are unordered - technically in Python 3.7+ they are ordered by insertion order, but do not rely on this
# in other languages dictionaries are called maps or associative arrays, hashmaps
# keys have to be unique, values do not have to be unique
# mutable - you can change them
# dictionaries are dynamic - they can grow and shrink as needed
# dictionaries are iterable - you can loop over them
# dictionaries can be nested - you can have a dictionary inside a dictionary and so on
# keys have to be immutable - so you can use strings, numbers, tuples as keys, but not lists or other dictionaries
# dictionaries are enclosed in curly braces {}

# let's start with empty_dict
empty_dict = {} # this is an empty dictionary
# another way is with dict() constructor
empty_dict_also = dict() # less used because we are lazy to type, so {} is more common
# dict() can be used to populate dictionary with key-value pairs

print("Empty dictionaries:")
print(empty_dict)
print(empty_dict_also)

# let's check out length
print("Length of empty_dict is", len(empty_dict))

# let's make a telephone book
# keys are names, values are phone numbers
tel_dict = {"Alice": 123456, "Bob": 654321, "Charlie": 987654}
print("Telephone book:")
print(tel_dict)
# length of dictionary
print("Length of tel_dict is", len(tel_dict))

# main use is to get a value by key
# so let's get Alice's number
print("Alice's number is", tel_dict["Alice"]) # this will be very fast (O(1)) even if we have million entries

# imagine if we had a list of tuples with phone numbers
# this would be very slow to find a number
phone_list = [("Alice", 123456), ("Bob", 654321), ("Charlie", 987654)]
# here to find Charlie's number we would have to loop over the list
# not so with dictionary

# let's add a new entry
tel_dict["David"] = 111222
print("Telephone book with David:")
print(tel_dict)
# we can add key with already existing value
tel_dict["Eve"] = 123456
print("Telephone book with Eve:")
print(tel_dict)

# what will happend if I have another Eve and I try to add her number
tel_dict["Eve"] = 999999 # this will overwrite the old value!
print("Telephone book with new Eve:")
print(tel_dict)

# what do we do if George has multiple numbers?
# we could use a list as value
tel_dict["George"] = [111, 222, 333] # Python lets us use lists as values
print("Telephone book with George:")
print(tel_dict)

# what will happen if I try to get a number for someone who is not in the dictionary for example eve
# print(tel_dict["eve"]) # this will raise a KeyError
# we could ask for forgiveness instead of permission
try:
    print(tel_dict["eve"]) # keys are case sensitive!
except KeyError as e:
    print("KeyError:", e)

# we could also check first if the key is in the dictionary
if "eve" in tel_dict: # this check for key is very fast (O(1)) again same as adding or getting a value
    print("Eve's number is", tel_dict["eve"])
else:
    print("Eve is not in the dictionary")


# best approach if we are not sure if the key is in the dictionary is to use get method
# so let's try to get eve's number
# if the key is not in the dictionary, get will return None
print("Eve's number is", tel_dict.get("Eve")) # this will return 999999
print("eve's number is", tel_dict.get("eve")) # this will return None
# we can also specify a default value
print("eve's number is", tel_dict.get("eve", "No number")) # this will return "No number"
