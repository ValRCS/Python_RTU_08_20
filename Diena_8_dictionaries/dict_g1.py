# dictionary lets us access value using key in constant time
# other names for dictionary are associative array, HashMap and so no, key-value store
eng_2_lat = {}  # you could do my_dict = dict()
eng_2_lat['one'] = 'viens'
eng_2_lat['two'] = 2  # we can store in values including other dictionaries
eng_2_lat['three'] = "trīs"
print(eng_2_lat['one'])
# very very quick O(1) access by key -> value
print(eng_2_lat)
my_dict = {"dog": "Fido", "cat": "Tom", "mouse": "Jerry"}
print(my_dict['dog'])
# now Python 3.7+ guarantees insertion order for dictionaries

# keys for dictionary must be unique
my_dict['dog'] = "Fredo"
my_dict['dog']
my_dict

my_dict['chicken']  # KeyError error
my_dict.get('dog')
my_dict.get('chicken')  # get gives you None if no key found
my_dict.get('chicken', 'defaultchicken is ķekavas')
# get gives you default value if no key found
"dog" in my_dict
"chicken" in my_dict
# get does the same thing that below code does
if "chicken" in my_dict:
    print(my_dict["chicken"])
else:
    print("Neatradam")

len(my_dict)

# we could just get keys
my_keys = list(my_dict.keys())
my_keys
my_values = list(my_dict.values())
my_values
my_items = list(my_dict.items())
my_items

my_list = [["v", "VVV"], ["a", "AA"], ["l", "LLLL"], ["v", "last v wins!"]]
my_list
my_n_dict = dict(my_list)
my_n_dict

# keys can be any immutable type
my_dict[1] = "one"
my_dict
my_dict[1]
my_dict["1"] = "one too"
my_dict
# values can be duplicated
my_dict["I"] = "one"
my_dict

for key, value in my_dict.items():  # also popular is k,v
    print(f"{key=}, {value=}")


def find_needle(needle, haystack):
    res_list = []
    for key, value in haystack.items():
        if value == needle:
            print(f"Found {key=} which has value {needle=}")
            # i could even modify it here in dictionary
            res_list.append((key, value))
    return res_list


my_results = find_needle("one", my_dict)
my_results


new_list = [print(f"{key=},{value=}") or [key, value]
            for key, value in my_dict.items()]
# new_list

squares = {f"{x=} squared ->": x*x for x in range(10)}
squares

plain_dict = {str(x): 0 for x in range(10)}
plain_dict
# could be useful as a counter
my_nums = [5, 6, 1, 6, 7, 1, 5, 6]
for n in my_nums:
    plain_dict[str(n)] += 1

plain_dict.setdefault("mykey", "myvalue")
plain_dict
# so setdefault only works ONCE, will not overwrite
plain_dict.setdefault("mykey", "new value will not work myvalue")
last_item = plain_dict.popitem()
last_item
plain_dict
# so pop destroys key and returns its value,
# raises KeyError unless 2nd argument is given
my_4 = plain_dict.pop('4', "couldnt find this key")
my_4
plain_dict
plain_dict.update({'3': 500, "foo": "Bar"})
plain_dict

del plain_dict['2']
plain_dict
