# # # # # # Python Dictionaries
# # # # # # https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# # # # # # key - value pairs
# # # # # # unordered
# # # # # # other languages - associative array, map, hashmap
# # # # # # O(1) value lookup - very quick
# # # mutable - can be changed
# # # dynamic can grow or shrink
# # # can be nested - matroyshka principle
# # # from Python 3.6 dictionaries preserve insertion or der

# empty_dict = {} # another way is with dict()

# print(len(empty_dict))
# print(type(empty_dict))


# tel = {'valdis': 2640, 'līga': 2911}
# print(tel)
# tel['maija'] = 2653 # i add a new key-value pair to the dictionary or overwrite the old one
# print(tel)
# print(tel['valdis']) # this lookup will be very fast O(1) even with huge dictionary
# key = "maija"
# print(tel[key])
# may_phone = tel[key] # we can always save values/reference in a new variable
# print(may_phone)
# # # # # # # keys are unique, values can match for different keys
# tel['valdis'] = 2900
# print(tel)
# tel['valdis'] = [2900, 2911, 2640]
# print(tel)
# val_phones = tel['valdis']
# print(val_phones) # so this should be a list
# tel['valdis'] = 2640
# print(tel)
# tel['petēris'] = 2911
# print(tel)
# tel['visvaldis otrais pētera dēls'] = 1888
# print(tel)
# print(tel.keys(), type(tel.keys()))
# key_list = list(tel.keys()) # so i can create a list of dictionary keys
# print(key_list)

# # similarly I can extract values from a dictionary
# value_list = list(tel.values())
# print(value_list)

# print('valdis' in tel) # so i check for key in my dictionary very quickly
# print('Valdis' in tel) # case sensitive so False
# print('joker' in tel)

# tel[""] = "Should not work" # it 
# print(tel.keys())
# print(tel[""])
# tel["empty_string"]= "" # this is normal
# tel["none_value"] = None # this is normal
# print(tel)

# print(2640 in tel.values()) # just in keep in mind this will be slow on big dictionaries

# tel["many_values"] = 4444, 5555, "Hmmm" # this will actually be a tuple(similar to fixed list) as a value
# print(tel["many_values"])
# tel["my_dict"] = {"first phone":22222, "second phone" : 34322}
# print(tel)

# # # print(tel.keys()[2]) # not possible so we need list if we need index
# print(list(tel.keys())[2]) #  we need list if we need index
# # print(tel['badkey']) # this will be an error
# # my_key = "petēris"
# my_key = "badpetēris"
# if my_key in tel:
#     print("key:", my_key, "value:",tel[my_key])
# else:
#     print("Couldn't find this key", my_key)
# print(tel.get('valdis')) # so we get value by key 'valdis' similar to tel['valdis'] but without errors
# print(tel.get('nevaldis'))  # default is None if not found
# print(tel.get('valdis', "couldn't find the key")) # returns value for the key if found
# print(tel.get('nevaldis', "couldn't find the key")) # or second argument if key is not found


# for key in tel: # so we can iterate over all keys in a dictionary
#     print("key:", key, "value:",tel[key]) # no need for get since we are guaranteed key 
#     # just remember NOT to modify dictionary size when looping over it

# # # # # # # iterate over all items (key->value pairs) in dictionary
# for key, value in tel.items(): # also common is k,v
#     # it is important not to modify this dictionary while we are looping over it
#     print(f"{key=}, {value=}") # this Python 3.8+ syntax
#     print(f"key={key}, value={value}")
#     # do more stuff with each key value pair
# print(tel.items())
# # # print(tel)

# # # # # idea to set key value pair UNLESS it is already set
# tel.setdefault("rūta", 2911)
# print(tel)
# tel.setdefault("rūta", 5555) # so this will not run because "rūta" is already set
# print(tel)

# tel["valdis"] = 2911 # so changing value
# print(tel)

# value_to_find = 2911
# new_dict = {}
# names_with_2911 = []

# for key, value in tel.items():
#     if value == value_to_find:
#         new_dict[key] = value # setdefault would also work
#         names_with_2911.append(key) # saving just the names in a list

# print(new_dict)
# print(names_with_2911, list(new_dict.keys()))

# # # # delete
# del tel['petēris']
# print(tel)
# # del tel['petēris'] # should be KeyError
# # # no shortcut se we might want to check before deleting
# if "petēris" in tel:
#     print("Deleting")
#     del tel['petēris']
# else:
#     print("Nothing to delete")

# # same as below but creating a new dictionary with a filter
# no_aldis_dict = {k:v for k,v in tel.items() if "aldis" not in k}
# print("Dict comprehension", no_aldis_dict)

# for key in tel.copy():
#     if "aldis" in key:
#         del tel[key] # careful here we need iterate over copy then or use dictionary comprehension
# print(tel)

# # # # # # # set value for key if not set
# # # # # # tel.setdefault('pēteris', 2911)
# # # # # # # the above will not overwrite unlike tel['pēteris'] = 2911

# # # # complete clearing of dictionary
# tel.clear()
# print(tel)

# common_phone = 1888
# keys = ["Valdis","Līga","Rūta", "Maija"]
# for key in keys:
#     tel.setdefault(key, common_phone) # could also use tel[key] = common_phone
# print(tel)

# # # # dictionary comprehension to do the above loop
# new_dict = {key:common_phone for key in keys}
# print(new_dict)
# import random # this should go up top generally
# rand_dict = {key:random.randint(1000, 9999) for key in keys}
# print(rand_dict)
# squares = {f"Square-{n}":n*n for n in range(10)}
# print(squares)

# # # # so pop destroys key and returns its value,
# # # # raises KeyError unless 2nd argument is given
# ede = tel.pop('Ede', "couldnt find this key")
# print(ede)
# ruta = tel.pop("Rūta", "no such key")
# print(ruta)
# print(tel)

# tel.update({"Valdis":29000, '3': 500, "foo": "Bar"})
# print(tel)
# tel[3] = 3000 # looks like list syntax but it is not 
# print(tel)
# # # better to stick with one type of key and one data type for values if possible
# tel["emergency"] = [112,113,114,115]
# # # # 
# tel_alias = tel # still points to same data NOT A COPY!
# print(tel is tel_alias)
# shallow_copy = tel.copy() # this does creat a new dictionary with same values in 1st level
# print(shallow_copy)
# print(tel is shallow_copy)
# tel["emergency"][3]=1188
# print(tel)
# print(shallow_copy)
# # # so with shallow copy the 2nd level references stay the same



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


list_of_dicts = []
for n in range(10):
    list_of_dicts.append({"n":n,"sq":n*n})
print(list_of_dicts)

# so list comprehension outside
# dictionary comprehension inside
list_dicts = [{f"i{i}":i for i in range(n)} for n in range(10)]
print(list_dicts)