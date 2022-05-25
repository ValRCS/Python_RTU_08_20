# 2 replace bad values to good values in a dictionary
def replace_dict_value(d, bad_val, good_val):
    """OUT OF PLACE REPLACEMENT"""
    return {key: val if val != bad_val else good_val for key, val in d.items()}

d = {'a':5,'b':6,'c':5, 'd':6, 'e':5}

new_d = replace_dict_value(d, 5, 10)
print(d)
print(new_d)

# 2. uzdevums
# - = - = - = - = - = - = - = - = - = - = - = - =
def replace_dict_value_in_place(d: dict, bad_val, good_val) -> dict:
    """IN PLACE REPLACEMENT"""   
    for val in d:
        if d[val] == bad_val:
            d[val] = good_val  
    return d # so this is purely optional, but it is a good habit to return the dictionary

print("OriginaL", d)
d_alias = replace_dict_value_in_place(d, 5, 10)
print("Alias", d_alias)
print("Original", d)
print(d is d_alias)

