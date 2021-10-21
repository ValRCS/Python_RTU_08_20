# IN PLACE replacement
def replace_dict_value(d, bad_val, good_val): 
    for key, value in d.items():
        if value == bad_val:
            d[key] = good_val
    return d

old_d = {'a':5,'b':6,'c':5}
print(replace_dict_value({'a':5,'b':6,'c':5}, 5, 10))
new_d = replace_dict_value(old_d, 5, 10)
print(old_d)
print(new_d)
print("is same dict?", old_d is new_d)

# OUT OF PLACE - creating a new dictionary
def replace_dict_value_out_of_place(d, bad_val, good_val):
    new_dict = {}
    for k,v in d.items():
        if v == bad_val:
            new_dict[k] = good_val
        else:
            new_dict[k] = v
    return new_dict

n_d = replace_dict_value_out_of_place(old_d, 10, 7)
print(old_d)
print(n_d)