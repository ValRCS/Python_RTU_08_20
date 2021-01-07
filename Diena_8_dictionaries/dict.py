# # # # Python Dictionaries
# # # # https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# # # # key - value pairs
# # # # unordered
# # # # other languages - associative array, map, hashmap
# # # # O(1) value lookup - very quick
empty_dict = {} # 
print(len(empty_dict))
print(type(empty_dict))
tel = {'valdis': 2640, 'līga': 2911}
print(tel)
tel['maija'] = 2653 # i add a new key-value pair to the dictionary or overwrite the old one
print(tel)
print(tel['valdis']) # this lookup will be very fast O(1) even with huge dictionary
key = "maija"
print(tel[key])
may_phone = tel[key]
print(may_phone)
# # # # keys are unique, values can match for different keys
tel['valdis'] = 2900
print(tel)
tel['valdis'] = [2900, 2911, 2640]
print(tel)
tel['valdis'] = 2640
print(tel)
tel['petēris'] = 2911
print(tel)
print(tel.keys(), type(tel.keys()))
key_list = list(tel.keys()) # so i can create a list of dictionary keys

print(key_list)
value_list = list(tel.values())
print(value_list)
print('valdis' in tel) # so i check for key in my dictionary
print('joker' in tel)

print(2640 in tel.values()) # just in keep in mind this will be slow on big dictionaries

# print(tel['badkey'])
my_key = "petēris"
# my_key = "badpetēris"
if my_key in tel:
    print("key:", my_key, "value:",tel[my_key])
else:
    print("Couldn't find this key", my_key)
print(tel.get('valdis')) # so we get value by key 'valdis' similar to tel['valdis'] but without errors
print(tel.get('nevaldis'))  # default is None if not found
print(tel.get('nevaldis', "couldn't find the key"))


for key in tel: # so we can iterate over all keys in a dictionary
    print("key:", key, "value:",tel[key])

# # # # iterate over all items (key->value pairs) in dictionary
for key, value in tel.items():
    # it is important not to modify this dictionary while we are looping over it
    print(f"{key=}, {value=}")
    print(f"key={key}, value={value}")
    # do more stuff with each key value pair
# print(tel.items())
print(tel)

# # idea to set key value pair UNLESS it is already set
tel.setdefault("rūta", 2911)
print(tel)
tel.setdefault("rūta", 5555) # so this will not run because "rūta" is already set
print(tel)

tel["valdis"] = 2911 # so changing value
print(tel)

value_to_find = 2911
new_dict = {}

for key, value in tel.items():
    if value == value_to_find:
        new_dict[key] = value

print(new_dict)
# # delete
del tel['petēris']
print(tel)

# # # # set value for key if not set
# # # tel.setdefault('pēteris', 2911)
# # # # the above will not overwrite unlike tel['pēteris'] = 2911

# # complete clearing of dictionary
tel.clear()
print(tel)

common_phone = 1888
keys = ["Valdis","Līga","Rūta", "Maija"]
for key in keys:
    tel.setdefault(key, common_phone)
print(tel)

# dictionary comprehension to do the above loop
new_dict = {key:common_phone for key in keys}
print(new_dict)
squares = {f"Square-{n}":n*n for n in range(10)}
print(squares)

# so pop destroys key and returns its value,
# raises KeyError unless 2nd argument is given
my_4 = tel.pop('4', "couldnt find this key")
print(my_4)
ruta = tel.pop("Rūta", "no such key")
print(ruta)
print(tel)

tel.update({"Valdis":29000, '3': 500, "foo": "Bar"})
print(tel)
tel[3] = 3000
print(tel)

# 
shallow_copy = tel.copy()
print(shallow_copy)


def get_filtered_dict(in_dict, value_to_find):
    resulting_dict = {}
    for key, value in in_dict.items():
        if value_to_find == value:
        # if value_to_find in value:  # only check if there is some string in
            resulting_dict[key] = value
            # setdefault would also work here
    return resulting_dict

find_1888 = get_filtered_dict(tel, 1888)
print(find_1888)

find_1888_b = {k:v for k,v in tel.items() if v == 1888}
print(find_1888_b)

