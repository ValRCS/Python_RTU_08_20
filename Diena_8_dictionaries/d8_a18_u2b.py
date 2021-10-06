# 2. Vārdnīcu labotājs
 
# OUT OF PLACE - new dictionary
def replace_dict_value(in_dict, bad_val, good_val):
    resulting_dict = {}
    for key, value in in_dict.items():
        if bad_val == value:
            resulting_dict[key] = good_val
        else:
            resulting_dict[key] = value
    return resulting_dict
 
old_dict = {'a':5,'b':6,'c':5}
out_dict = replace_dict_value(old_dict, 5, 10) 
print(old_dict)
print(out_dict)

#IN PLACE - changes d
def replace_dict_value_inplace(d, bad_val, good_val):
    for key,value in d.items():
        if value == bad_val:
            d[key] = good_val
    return d

new_alias = replace_dict_value_inplace(old_dict, 5, 10) 
print(old_dict)
print(new_alias)
print(old_dict is new_alias)