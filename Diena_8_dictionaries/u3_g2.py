def clean_dict_value(d,bad_v):
    return {k: v for k, v in d.items() if not v == bad_v} 

result = clean_dict_value({'a': 5, 'b': 6, 'c': 5, 'd':3}, 5)
print(result)

def clean_dict_values(d,v_list):
    return {k: v for k, v in d.items() if v not in v_list}

print(clean_dict_values({'a': 5, 'b': 6, 'c': 5, 'd':3},[3,4,5]))   