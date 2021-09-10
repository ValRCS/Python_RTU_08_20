def replace_dict_value(d, bad_val, good_val, verbose=True):
    """
    OUT OF PLACE replacement returns a new dictionary
    """
    new_dict = d.copy()
    for key, value in d.items():
        if value == bad_val:
            new_dict[key] = good_val
    clean_dict_value = new_dict # this is just a shortcut to new_dict
    if verbose:
        print(f"{d}, {bad_val}, {good_val} -> {clean_dict_value}")
    return new_dict
   
print(replace_dict_value({"a": 5, "b": 6, "c": 5}, 5, 10))
old_dict = {"a": 5, "b": 6, "c": 5, "d":11}
new_dict = replace_dict_value(old_dict, 5, 20)
print(old_dict)
print(new_dict)

def replace_dict_value_inplace(d, bad_val, good_val):
    """
    IN PLACE replaces values in the original dictionary
    """
    for key, value in d.items():
        if value == bad_val: 
            d[key] = good_val
    return d # could work without return

old_dict = {"a": 5, "b": 6, "c": 5, "d":11}
new_dict = replace_dict_value_inplace(old_dict, 5, 20)
print(old_dict)
print(new_dict)
print(old_dict is new_dict)