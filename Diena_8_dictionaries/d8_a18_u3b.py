#3.a
# OUT OF PLACE returns new clean dictionary
def clean_dict_value(d,bad_val):
    clean_dict = {}
    for key in d:
        if d[key] != bad_val:
            clean_dict[key] = d[key]
    return clean_dict

old_dict = {'a':5,'b':6,'c':5, 'd':5, 'e':4}
print(old_dict)
new_dict = clean_dict_value(old_dict, 5)
print(old_dict)
print(new_dict)

# IN PLACE - changes original
def clean_dict_value_inplace(in_dict, bad_val):
    for key, value in in_dict.copy().items():
        if bad_val == value:
            del in_dict[key]
    return in_dict

new_alias =  clean_dict_value_inplace(old_dict, 5)
print(old_dict)
print(new_alias)
print(old_dict is new_alias)

old_dict = {'a':5,'b':6,'c':5, 'd':5, 'e':4}
# :dict and :list are so called type hints - for type checker tools, Python itself ignores them
# IN PLACE modifies existing dictionary 
def clean_dict_values(d:dict, v_list:list):
    for key, value in d.copy().items():
        if value in v_list:
            del d[key]
    print(d)

clean_dict_values(old_dict, [4,5])
print(old_dict)

old_dict = {'a':5,'b':6,'c':5, 'd':5, 'e':4}
def clean_dict_values_outofplace(d, v_list):
    return {k:v for k,v in d.items() if v not in v_list}

clean_dict = clean_dict_values_outofplace(old_dict, [4,5])
print(old_dict)
print(clean_dict)