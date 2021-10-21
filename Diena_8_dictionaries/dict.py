# # # # # # # # # # Python Dictionaries
# # # # # # # # # # https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# # # # # # # # # # key - value pairs
# # # # # # # # # # unordered
# # # # # # # # # # other languages - associative array, map, hashmap
# # # # # # # # # # O(1) value lookup - very quick
# # # # # # # mutable - can be changed
# # # # # # # dynamic can grow or shrink in size
# # # # ### iterable can loop through (order from 3.6+ is in order of insertion)
# # # # # # # can be nested - matroyshka principle
# # # # # # # from Python 3.6 dictionaries preserve insertion or der

# empty_dict = {} # another way is with dict()
empty_dict = {}
another_empty_dict = dict()

print(empty_dict)
print(another_empty_dict)

print(len(empty_dict))
print(type(empty_dict))

tel_dict = {'valdis': 2640, "līga": 2911}
print(tel_dict)
tel = {'valdis': 2640, 'līga': 2911}  #also a dictionary
print(tel)

print(tel['valdis'])  # so get value from key, very fast(O(1) even with millions and billions of items)

tel['maija'] = 2653 # i add a new key-value pair to the dictionary or overwrite the old one
print(tel)
print(type(tel))

# # # # this is why we use dictionaries very fast to look up
# print(tel['valdis']) # this lookup will be very fast O(1) even with huge dictionary

key = "maija"
print(tel[key], tel["maija"])

tel['valdis'] = 1188 #keys have to be unique, so here I will overwrite my old value
print(tel)
# # # if I have many phones well, then I have options, how about a list?
tel['valdis'] = [2640, 1188, 911]
print(tel)
print(tel['valdis'])
print(tel['valdis'][-1], tel['valdis'][2])

may_phone = tel[key] # we can always save values/reference in a new variable
print(may_phone) # once it is out no relation to dictionary
tel['ValdisZ'] = 1001 # case sensitive keys
tel['Valdisz'] = 1002 # case sensitive keys, not good style of course for such variables
print(tel)
# # # # # # # # # # # keys are unique, values can match for different keys
tel['valdis'] = 1001
print(tel) # so by givine new value to key we overwrote the old one
# # # # tel['valdis'] = [2900, 2911, 2640]
# # # # print(tel)
# # # # val_phones = tel['valdis'] # instant lookup
# # # # print(val_phones) # so this should be a list
# # # # tel['valdis'] = 2640
# # # # print(tel)
tel['petēris'] = 2911
# print(tel)
tel['visvaldis otrais pētera dēls'] = 1888
print(tel)
print(tel.keys(), type(tel.keys()))
key_list = list(tel.keys()) # so i can create a list of dictionary keys
print(key_list)

# # # # # similarly I can extract values from a dictionary
value_list = list(tel.values())
print(value_list)

key_list.append("rūta")
key_list.append("muris") # so just one more value for our list
value_list.append(1008)

print(key_list)
print(value_list)
# # # i can create a new dictionary from two lists(iterables actually)
print(list(zip(key_list, value_list))) # so list of two value pairs
new_dict = dict(zip(key_list,value_list)) # until one lists runs out so muris has no corresponding value
print(new_dict)
# # print(tel)
reversed_dict = dict(zip(value_list, key_list)) # so kyes will be integers and values will be strings
print(reversed_dict)

# # fast checkup on key existance
print('valdis' in tel) # so i check for key in my dictionary very quickly
print('Valdis' in tel) # case sensitive so False
print('joker' in tel)

# # this will take O(n) operations on n sized dictionary
print(1001 in tel.values()) # this will be slow

# tel[""] = "Should not work" # it but turns out it does
# print(tel.keys())
# # print(tel[""])
# tel["empty_string"]= "" # this is normal
# tel["none_value"] = None # this is normal to store unknown values
# print(tel)

# # print("THe next operation will be slow in a big dictionary")
# # print(1001 in tel.values()) # just in keep in mind this will be slow on big dictionaries

# tel["many_values"] = 4444, 5555, "Hmmm" # this will actually be a tuple(similar to fixed list) as a value
# print(tel["many_values"])
tel["my_dict"] = {"first phone":22222, "second phone" : 34322}
print(tel)
print(tel["my_dict"])  #inner dict
print(tel["my_dict"]["second phone"])  #inner dict value lookup

# num_1, num_2, msg_1 = tel["many_values"] # this is tuple unpacking
# print(num_1, num_2, msg_1)

# # # # # # # print(tel.keys()[2]) # not possible so we need list if we need index
# # print(list(tel.keys())[2]) #  we need list if we need index

# print(tel['my_dict'])
# print(tel['my_dict']['second phone'])  # so going down to the value of inner dictionary

# # # # # how do we handle bad keys?

# print(tel['badkey']) # this will be an error
# my_key = "valdis"
my_key = "notarealkey"
if my_key in tel:
    print("key:", my_key, "value:", tel[my_key])
else:
    print("Couldn't find this key", my_key)


print(tel.get('valdis')) # so we get value by key 'valdis' similar to tel['valdis'] but without errors
print(tel.get('nevaldis'))  # default is None if not found
# # print(tel.get('none_value')) # here we actually get a value but it is None no way to tell without if :)
print(tel.get('valdis', "couldn't find the key")) # returns value for the key if found
print(tel.get('nevaldis', "couldn't find the key")) # or second argument if key is not found



# # # # # how about looping?

for key in tel: # so we can iterate over all keys in a dictionary
    print("key:", key, "value:", tel[key]) # no need for get since we are guaranteed key 
    # just remember NOT to modify dictionary size(delete or add) when looping over it

# for key in tel.keys(): # SAME as above loop iterate through keys in a dictionary
#     print("key:", key, "value:", tel[key]) # no need for get since we are guaranteed key 
#     # just remember NOT to modify dictionary size(delete or add) when looping over it

print(tel.items()) #special dict_items collection
# # # # # # # # # # # iterate over all items (key->value pairs) in dictionary
for key, value in tel.items(): # also common is k,v
    # it is important not to modify this dictionary size while we are looping over it
    
    print(f"{key=}, {value=}") # this Python 3.8+ syntax good for debugging
    print(f"key={key}, value={value}, {tel[key]}")
#     # do more stuff with each key value pair
# # # # # print(tel.items())
# # # # # # # print(tel)

tel_copy = tel.copy()
print("Same contents for dictionaries", tel_copy == tel)
print("Same physical dictionary in memory?", tel_copy is tel)

# # if we need to iterate through dictionary and change its size then we loop through its copy
for key, value in tel.copy().items(): # also common is k,v
    # it is important not to modify this dictionary size while we are looping over it
    # now it is safe to add or delete original tel entries
    print(f"{key=}, {value=}") # this Python 3.8+ syntax good for debugging
    print(f"key={key}, value={value}")

# print(tel)
# # # # # # # # # idea to set key value pair UNLESS it is already set
# tel.setdefault("rūta", 2911)
# print(tel)
# tel.setdefault("rūta", 5555) # so this will not run because "rūta" is already set
# print(tel)
# # # in other words I save one if (it is done by Python)
# tel["rūta"] = 1001 # so this will always work, overwriting or not
# print(tel)

# # # # tel["valdis"] = 2911 # so changing value
# # # # print(tel)

value_to_find = 1001
new_dict = {} # empty dict to hold both key and value
names_with_1001 = [] # empty list to hold just the names/keys

# # # so filtering for values in a dictionary
for key, value in tel.items():  #no need for copy() since I am modifying different dict
    if value == value_to_find:
        print(f"Match for {value} found! The key to be added is {key}")
        new_dict[key] = value # setdefault would also work
        names_with_1001.append(key) # saving just the names in a list

print(new_dict)
print(names_with_1001, list(new_dict.keys()))

# # # # # # # # delete
# del tel["my_dict"]
del tel['petēris']
print(tel)
# del tel['petēris'] # should be KeyError
# # # # # no shortcut se we might want to check before deleting
if "petēris" in tel:
    print("Deleting")
    del tel['petēris']
else:
    print("Nothing to delete")

# # # # how to delete multiple keys from dict
bad_key_list = ["none_value", "many_values", "Valdisz", "nosuchkey","my_dict","", "empty_string"]
for key in bad_key_list: # we are not going through our dictionary, so it is okay to delete
    if key in tel:
        print("Deleting", key)
        del tel[key]
    else:
        print("Nothing to delete did not find", key)

print(tel)


# # # # # # same as below but creating a new dictionary with a filter
# # # # so new dictionary without keys which containe "aldis"
no_aldis_dict = {k:v for k,v in tel.items() if "aldis" not in k} # if is not required
print("Dict comprehension", no_aldis_dict)
no_aldis_dict_also = {k:tel[k] for k in tel if "aldis" not in k} # if is not required
print("Dict comprehension", no_aldis_dict_also)
# # i can modify keys and values in the new dictionary while creating it
no_aldis_dict = {k+" S":v*1_000 for k,v in tel.items() if "aldis" not in k} # if is not required
print("Dict comprehension", no_aldis_dict)

# full_dict = {k:v for k,v in tel.items()} # so same as tel.copy()
# print(full_dict) # just a copy (shallow one)
# # print(tel == full_dict, tel is full_dict) # contents == are equal, but we have two different dictionaries

print(tel)

# # # # # withotu dictionary comprehension
# # # # # so looping and deleting we want to use copy
for key in tel.copy(): # we use copy to go through if we want to delete from original
    if "aldis" in key:
        del tel[key] # careful here we need iterate over copy then or use dictionary comprehension
print(tel)

# about shallow copies
tel["my_list"] = [1,2,3]
print(tel)
tel_copy = tel.copy() # shallow copy meaning deeper(lists, dictionaries as values) structures are not copied just shortcuts
print(tel_copy)
tel_copy["my_list"].append(5000)
print(tel_copy)
print(tel)
print(tel == tel_copy, tel is tel_copy)
tel_copy["maija"] = 2000
print(tel_copy)
print(tel)
print(tel == tel_copy, tel is tel_copy)
tel_copy["my_list"] = tel_copy["my_list"][:2]
print(tel_copy)
print(tel)
print(tel == tel_copy, tel is tel_copy)


# # # # # # # # # # # set value for key if not set
# # # # # tel.setdefault('pēteris', 2911)
# # # # # # # # # # # the above will not overwrite unlike tel['pēteris'] = 2911

# # # # # # # complete clearing of dictionary
tel.clear()
print(tel)

common_phone = 1888
keys = ["Valdis","Līga","Rūta", "Maija"]

for key in keys:
    tel.setdefault(key, common_phone) # could also use tel[key] = common_phone
print(tel)

# # # # # # # # dictionary comprehension to do the above loop
new_dict = {key:common_phone for key in keys}
print(new_dict)

# # # # # #how about making a dictionary of each character and their ASCII/UNICODE codes
print(ord("a"))
import string
letters = string.ascii_letters
print(letters)

letter_dictionary = {k:ord(k) for k in letters }
print(letter_dictionary)

# # reverse key values (which we could also do with dict(zip )) trick earlier
reverse_letter_dictionary = {value:key for key,value in letter_dictionary.items()}
print(reverse_letter_dictionary)

# # why I do not like numbers as dictionary keys
print(reverse_letter_dictionary[101]) # looks like a list does it not ? but it is a dictionary

# # so we could use numbers when they are big or infrequent 

# # letter_dictionary_2 = {k:ord(k) for k in "Raibi ruņči rīgā rūc"}
# # print(letter_dictionary_2)



# # import random # this should go up top generally
# # rand_dict = {key:random.randint(10_000_000, 99_999_999) for key in keys}
# # print(rand_dict)
# # squares = {f"Square-{n}":n*n for n in range(10)}
# # print(squares)

# # # # # # # # so pop destroys key and returns its value,
# # # # # # # # raises KeyError unless 2nd argument is given
# ede = tel.pop('Ede', "couldnt find this key")
# print(ede)
# ruta = tel.pop("Rūta", "no such key")
# print(ruta)
# print(tel)

# tel.update({"Valdis":29000, "3": 500, "foo": "Bar"}) # so merging dictionaries
# print(tel)
# tel[3] = 3000 # looks like list syntax but it is not 
# print(tel)
# # # # # # # better to stick with one type of key and one data type for values if possible
# # # # tel["emergency"] = [112,113,114,115]
# # # # print(tel)
# # # # # # # # 
# tel_alias = tel # still points to same data NOT A COPY!
# print(tel is tel_alias) # so tel and tel_alias are both shortcuts to same dictionary
# tel["ede"] = 9000
# print(tel_alias) # so what we change in one will change in another

# shallow_copy = tel.copy() # this does creat a new dictionary with same values in 1st level
# print(shallow_copy)
# print(tel is shallow_copy)
# shallow_copy["demogorgs"] = 5000
# print(tel)
# print(shallow_copy)
# # # tel["emergency"][3]=1188
# # # print(tel)
# # # print(shallow_copy)
# # # # # # # so with shallow copy the 2nd level references stay the same



# def get_filtered_dict(in_dict, value_to_find):
#     resulting_dict = {}
#     for key, value in in_dict.items():
#         if value_to_find == value:
#         # if value_to_find in value:  # only check if there is some string in
#             resulting_dict[key] = value
#             # setdefault would also work here
#     return resulting_dict

# find_1888 = get_filtered_dict(tel, 1888)
# print(find_1888)

# def get_filtered_dict_2(in_dict, value_to_find):
#     return {k:v for k,v in in_dict.items() if v == value_to_find}

# find_1888_2 = get_filtered_dict_2(tel, 1888)
# print(find_1888_2)


# # # # list_of_dicts = []
# # # # for n in range(10):
# # # #     list_of_dicts.append({"n":n,"sq":n*n})
# # # # print(list_of_dicts)

# # # # # # so list comprehension outside
# # # # # # dictionary comprehension inside
# # # # list_dicts = [{f"i{i}":i for i in range(n)} for n in range(10)]
# # # # print(list_dicts)

# tel["Valdis"] += 1 # increase the value for key Valdis by 1
# print(tel)
# tel["Valdis"] = tel["Valdis"] + 20  # shorter would be tel["Valdis"] += 20
# print(tel)

numbers = list(range(8))

new_dict = {}
for n in numbers:
    if n > 4:
        if "over4" in new_dict:
            new_dict["over4"] +=1 # add 1 to existing value
        else:
            new_dict["over4"] = 1 # could also do this with setdefault
    else:
        if "under5" in new_dict:
            new_dict["under5"] +=1
        else:
            new_dict["under5"] = 1
print(new_dict)