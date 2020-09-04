# Python Dictionaries
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# key - value pairs
# unordered
# other languages - associative array, map, hashmap
# O(1) value lookup - very quick
empty_dict = {}
len(empty_dict)
type(empty_dict)
tel = {'valdis': 2640, 'līga': 2911}
print(tel)
tel['maija'] = 2653
print(tel)
tel['valdis']
# keys are unique, values can match for different keys
tel['petēris'] = 2911
print(tel)
print(tel.keys())
key_list = list(tel.keys())
print(key_list)
value_list = list(tel.values())
print(value_list)
'valdis' in tel
'joker' in tel
print(tel['badkey'])
my_key = "petēris"
if my_key in tel:
    print(tel[my_key])
else:
    print("Couldn't find this key")
print(tel.get('valdis'))
print(tel.get('nevaldis'))  # default is None if not found
print(tel.get('nevaldis', "couldn't find the key"))

# iterate over all items (key->value pairs) in dictionary
for key, value in tel.items():
    print(f"{key=}, {value=}")
    # do more stuff with each key value pair
print(tel.items())

# delete
del tel['petēris']
print(tel)

# set value for key if not set
tel.setdefault('pēteris', 2911)
# the above will not overwrite unlike tel['pēteris'] = 2911
tel.clear()
print(tel)
