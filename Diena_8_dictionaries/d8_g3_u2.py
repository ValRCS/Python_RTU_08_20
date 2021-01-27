def replace_dict_value(d, bad_val, good_val):
    """
    Out of place dictionary value replacement
    Returns new dictionary
    """
    new_dict = {}
    for key, value in d.items():
        if value == bad_val:
            new_dict[key] = good_val
        else:
            new_dict[key] = value
 
    print(new_dict)
    return(new_dict)


def replace_dict_value_inplace(zzz, bad_val, good_val):
    for key, value in zzz.items():
        if value == bad_val:
            zzz.update({key: good_val})
    return zzz

replace_dict_value({'a': 5, 'b': 6, 'c': 5}, 5, 10)

some_dict = {'a': 5, 'b': 6, 'c': 5, 'ddd': 5}
print(some_dict)
replace_dict_value_inplace(some_dict, bad_val=5, good_val=10)
print(some_dict)
