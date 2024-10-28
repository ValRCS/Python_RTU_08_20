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

# first let's see how we can iterate over a dictionary
# we can iterate over keys
print("Iterating over keys:")
for key in tel_dict:
    print("Key:", key, "Value:", tel_dict[key]) # no need for get here, we know the key is in the dictionary
    # i could use get but no need in this case

# we can iterate over values - this is less common
print("Iterating over values:")
for value in tel_dict.values():
    print("Value:", value) # we have no idea what the key is, but we have the value

# more common is both key and value
print("Iterating over key-value pairs:")
for key, value in tel_dict.items():
    print("Key:", key, "Value:", value, tel_dict[key]) # we have both key and value
    # tel_dict[key] is not needed, but just to show that we can use key to get value

# let's get rid of George
print(f"Length of tel_dict before removing George is {len(tel_dict)}")
del tel_dict["George"] # this will remove George from the dictionary
print(f"Length of tel_dict after removing George is {len(tel_dict)}")
# removal is also very fast (O(1)) on large dictionaries
# if i try again to remove George, I will get a KeyError
try:
    del tel_dict["George"]
except KeyError as e:
    print("KeyError:", e)

# instead of del we could use pop method
# pop will return the value and remove the key-value pair
popped_value = tel_dict.pop("Eve") # this will remove Eve from the dictionary
print("Eve is removed from the dictionary")
print("Popped value is", popped_value)
# if I try to pop Eve again, I will get a KeyError
try:
    popped_value = tel_dict.pop("Eve") # will raise a KeyError
except KeyError as e:
    print("KeyError:", e)

# print dictionary after popping Eve
print("Telephone book after popping Eve:")
print(tel_dict)

# let's add Eve with same number as Alice
tel_dict["Eve"] = 123456
print("Telephone book with Eve:")
print(tel_dict)

# we can add multiple key-value pairs at once with update method
tel_dict.update({"Frank": 111, "Grace": 222}) # we use a dictionary as argument
print("Telephone book with Frank and Grace:")
print(tel_dict)

# we could store the dictionary first
new_numbers = {"Helen": 123456, "Ivars": 444, "Janis": 555}
tel_dict.update(new_numbers) # note update is IN-PLACE operation modifies the dictionary tel_dict
print("Telephone book with Helen and Ivars:")
print(tel_dict)

# let's find out who has number 123456
# we could loop over the dictionary
for key, value in tel_dict.items(): # we have to go through all key-value pairs could be slow on large dictionaries
    if value == 123456:
        print(f"{key} has number 123456")

# let's generalize this with a function
# let the function return a new dictionary with names as keys and numbers as values

def get_number_dict(tel_dict, number): # number could be called needle in general
    result_dict = {} # I create a new dictionary
    for key, value in tel_dict.items():
        if value == number:
            result_dict[key] = value
    return result_dict

# let's test the function
print("Finding number 123456:")
tel_dict_123456 = get_number_dict(tel_dict, 123456)
print(tel_dict_123456)

# we could also create a function to return a list of names
# since we know the number is unique, we can return a list of names
def get_names_list(tel_dict, number):
    result_list = [] # I create a new list
    for key, value in tel_dict.items():
        if value == number:
            result_list.append(key)
    return result_list

# let's test the function
callers_123456 = get_names_list(tel_dict, 123456)
print("Callers with number 123456:")
print(callers_123456)

# i could extract these names (since those are keys) from dictionary
callers_123456_names = list(tel_dict_123456.keys())
print("Callers with number 123456:")
print(callers_123456_names)
# of course I could get the values as well
callers_123456_numbers = list(tel_dict_123456.values())
print("Callers with number 123456:") # all of these will be the same
print(callers_123456_numbers)

# let's try adding some values to the dictionary but only if the key does not exist

# we could check first if the key is in the dictionary
if "Kārlis" not in tel_dict:
    tel_dict["Kārlis"] = 123456
else:
    print("Kārlis is already in the dictionary")

print("Telephone book with Kārlis:")
print(tel_dict)

# we could also use setdefault method
# setdefault will only set value for key if the key is not in the dictionary
tel_dict.setdefault("Līga", 123456) # this will add Līga to the dictionary
print("Telephone book with Līga:")
print(tel_dict)
# trying it with different number
tel_dict.setdefault("Līga", 654321) # this will not change the value for Līga
print("Telephone book with Līga:")
print(tel_dict)

