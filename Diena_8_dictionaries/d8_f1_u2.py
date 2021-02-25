def replace_dict_value(d, bad_val, good_val):
    """
    IN PLACE replacement of bad_val to good_val ues
    """
    for key, val in d.items():
        if bad_val == val:
            d[key] = good_val
    print(d)
    return d


 
 
replace_dict_value({'a':5,'b':6,'c':5}, 5, 10)
replace_dict_value({'a':5,'b':6,'c':5, 'd':30}, 30, 44)

my_dict = {'a':5,'b':6,'c':5}
replace_dict_value(my_dict, 5, 10)
print(my_dict)

# 2 uzdevums
 
def replace_dict_value_op(my_dict,bad_val,good_val):
    """
    OUT OF PLACE bad value replacement with new dictionary created
    """
    clean_dict = {}
    for k,v in my_dict.items():
        if v == bad_val:
            v = good_val
        clean_dict[k] = v
    return clean_dict

new_dict = {'a':5,'b':6,'c':5}
clean_dict = replace_dict_value_op(new_dict, 5, 12)
print(new_dict) # so og version stays unchanged
print(clean_dict) # new version is returned modified

 
