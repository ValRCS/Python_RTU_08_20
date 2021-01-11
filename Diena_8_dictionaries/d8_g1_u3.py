d={'a':5,'b':6,'c':5}
v_list = [3,4,5]
def clean_dict_value(d, bad_val):
    new_d = d.copy()
    for key,value in d.items():
        for i in v_list:
            if value == i: 
                del new_d[key] 
    return new_d

def clean_dict_values(d, bad_values):
    return {k:v for k,v in d.items() if v not in bad_values}

def clean_dict_values_long(d, bad_values):
    new_dict={}
    for k,v in d.items():
        if v not in bad_values:
            new_dict[k]=v
        else:
            new_dict[k]="BADDD"
            # pass # do nothing for now
    return new_dict

print(clean_dict_value(d, v_list))
print(clean_dict_values(d, v_list))
print(clean_dict_values_long(d, v_list))

