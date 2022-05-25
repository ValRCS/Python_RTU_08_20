# 3. uzdevums
# - = - = - = - = - = - = - = - = - = - = - = - =
def clean_dict_values(d: dict, v_list: list) -> dict:
    """OUT OF PLACE REPLACEMENT"""
    temp_dict = d.copy()
 
    # for key_name in d:
    #     if d[key_name] in v_list:
    #         del temp_dict[key_name]
    for key,value in d.items():
        if value in v_list: # so value is in bad values list
            del temp_dict[key]
 
    return temp_dict

     
d = {'a':5,'b':6,'c':5, 'd':6, 'e':5, 'f':2, 'g':3, 'h':2, 'i':4}

new_d = clean_dict_values(d, [3,4,5])
print(d)
print(new_d)

def clean_dict_values_in_place(d: dict, v_list: list) -> dict:
    """IN PLACE REPLACEMENT"""   
    for key,value in d.copy().items():
        if value in v_list: # so value is in bad values list
            del d[key]
 
    return d # so this is purely optional, but it is a good habit to return the dictionary

print(d)
d_alias = clean_dict_values_in_place(d, [3,4,5])
print(d)
print(d_alias)
print(d is d_alias)


def clean_dict_values_out_of_place(d: dict, v_list: list) -> dict:
    """OUT OF PLACE REPLACEMENT"""
    return {key: val for key, val in d.items() if val not in v_list}

d = {'a':5,'b':6,'c':5, 'd':6, 'e':5, 'f':2, 'g':3, 'h':2, 'i':4}

new_d = clean_dict_values_out_of_place(d, [3,4,5])
print(d)
print(new_d)

# i could replace old dictionary with new one
d = clean_dict_values_out_of_place(d, [3,4,5])
print(d)