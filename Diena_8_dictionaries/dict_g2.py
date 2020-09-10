eng_2_lat = {}  # alternative būtu dict()
eng_2_lat['dog'] = 'suns'  # mapping key "dog" to "suns"
# what can be a key?
# pretty much anything immutable
eng_2_lat['cat'] = 'kaķis'
eng_2_lat['mouse'] = 'pele'
print(eng_2_lat)
print(eng_2_lat['dog'])

# with dictionary keys have to be unique
eng_2_lat['dog'] = 'šunelis'
print(eng_2_lat)
# order of elements in dictionary is in original insertion order
# dictionary is not meant to be ordered

print('dog' in eng_2_lat)
'cat' in eng_2_lat
'human' in eng_2_lat
# eng_2_lat['human']
eng_2_lat.get('dog')
# print(eng_2_lat.get('human'))
mykey = "robot"
if mykey in eng_2_lat:
    print(eng_2_lat[mykey])
else:
    print("Not Found")
eng_2_lat.get(mykey, "Not Found")
mykey = "cat"
eng_2_lat.get(mykey, "Not Found")
len(eng_2_lat)
list(eng_2_lat.items())
list(eng_2_lat.keys())
list(eng_2_lat.values())

my_list = [['dog', 'suns'], ['cat', 'kaķis'], ['mouse', 'pele']]
print(my_list)
dict_from_list = dict(my_list)
print(dict_from_list)

dict_from_list[1] = "viens"
dict_from_list[3] = "three"
print(dict_from_list)
dict_from_list['1'] = "viens"  # remember values can be duplicates
print(dict_from_list)

for key in eng_2_lat:  # only keys
    print(f"{key=} : {eng_2_lat[key]=}")

for key, value in eng_2_lat.items():  # key with corresponding value
    print(f"{key=} : {value=}")

result_dict = {}
result_list = []
my_value = "viens"
for key, value in dict_from_list.items():
    if my_value == value:
        result_dict[key] = value
        result_list.append([key, value])

print(result_dict)
print(result_list)


def get_filtered_dict(in_dict, value_to_find):
    resulting_dict = {}
    for key, value in in_dict.items():
        # if value_to_find == value:
        if value_to_find in value:  # only check if there is some string in
            resulting_dict[key] = value
    return resulting_dict


new_d = get_filtered_dict(eng_2_lat, "suns")
print(new_d)
new_d = get_filtered_dict(eng_2_lat, "šunelis")
print(new_d)
new_d = get_filtered_dict(eng_2_lat, "el")
print(new_d)

del eng_2_lat["dog"]
print(eng_2_lat)

for key, value in eng_2_lat.copy().items():
    # now we can delete from eng_2_lat
    pass  # empty loop

eng_2_lat.update({'fish': 'zivs', 'cat': 'kaķēns'})
print(eng_2_lat)
gen_dict = {'dog': {'lat': 'suns', 'esp': 'perro',
                    'rus': 'sobaka'}, 'cat': 'kakis'}
print(gen_dict['dog']['lat'])
print(gen_dict['dog']['rus'])
print(gen_dict.get('dog').get('esp'))
