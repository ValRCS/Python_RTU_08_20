# 3. Vārdnīcu tīrītājs
# OUT OF PLACE returns new dictionary
def clean_dict_values(d, v_list):
    return {k:v for k,v in d.items() if v not in v_list}



og_dict = {'a':5,'b':6,'c':5, 'd':51}
new_dict = clean_dict_values(og_dict, [5,51])

print(og_dict)
print(new_dict)    

def clean_dict_value(d, bad_val):
    # return clean_dict_values(d, [bad_val])
    return {k:v for k,v in d.items() if v != bad_val}

clean_dict = clean_dict_value(og_dict, 5)
print(og_dict)
print(clean_dict)