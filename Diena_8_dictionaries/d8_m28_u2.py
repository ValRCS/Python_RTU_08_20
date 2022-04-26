# 2. Vārdnīcu labotājs
 
# OUT OF PLACE returns new dictionary 
def replace_dict_value(d, bad_val=5, good_val=10):
    # good_dict = {key: (good_val if val == bad_val else val) for key, val in d.items()}
 
    # # good_dict = {}
    # # for key, value in d.items():
    # #     if value == bad_val:
    # #         good_dict[key] = good_val
    # #     else:
    # #         good_dict[key] = value
    # return good_dict
    # same as above
    return {key: (good_val if val == bad_val else val) for key, val in d.items()}

og_dict = {'a':5,'b':6,'c':5, 'd':51}
new_dict = replace_dict_value(og_dict)

print(og_dict)
print(new_dict)

# in place , changes the original dictionary
def replace_dict_value_inplace(d, bad_val=5, good_val=10):
    for key, val in d.items():
        if val == bad_val:
            d[key] = good_val # this is ok, because we are changing the original dictionary
    return d

newish_dict = replace_dict_value_inplace(og_dict)
print(og_dict)
print(newish_dict)
print(og_dict is newish_dict) # this is true, because we are changing the original dictionary
# so newish_dict is just a pointer to og_dict, rather both point to the same dictionary