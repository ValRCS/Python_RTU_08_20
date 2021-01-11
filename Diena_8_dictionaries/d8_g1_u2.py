def replace_dict_value(d, bad_val, good_val):
    """
    Replaces Dictionary Values whenver bad_val is encountered with good_val
    """
    for k,v in d.items():
        if v == bad_val:
            d[k] = good_val
    return d
 
print(replace_dict_value({'a':5,'b':6,'c':5},5,10))