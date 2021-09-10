def clean_dict_value(d, bad_val):
    # return {k: v for k, v in d.items() if v != bad_val}
    new_dic = {k: v for k, v in d.items() if v != bad_val}
    if new_dic != d:
        d = new_dic
    return d
 
print(clean_dict_value({"a": 5, "b": 6, "c": 5}, 5))