def clean_dict_value(d, bad_val):
    """
    IN-PLACE cleaner
    """
    for key in d.copy():
        if d[key] == bad_val: 
            del d[key]
    return d
 
print(clean_dict_value({'a':5,'b':6,'c':5}, 5))

old_dict = {"a": 5, "b": 6, "c": 5, "d":11}
new_dict = clean_dict_value(old_dict, 5)
print(old_dict)
print(new_dict)
print(old_dict is new_dict)

#3A
def clean_dict_value_outofplace(d, bad_val):
    """Returns a dictionary without unwanted values OUT OF PLACE"""
    return {k:v for k,v in d.items() if v != bad_val}

old_dict = {"a": 5, "b": 6, "c": 5, "d":11}
new_dict = clean_dict_value_outofplace(old_dict, 5)
print(old_dict)
print(new_dict)
print(old_dict is new_dict)

#3B
def clean_dict_values(d, v_list):
    """Returns a NEW dictionary cleaned from values provided in a list"""
    return {k:v for k,v in d.items() if v not in v_list}

old_dict = {"a": 5, "b": 6, "c": 5, "d":11}
new_dict = clean_dict_values(old_dict, [5,11])
print(old_dict)
print(new_dict)
print(old_dict is new_dict)