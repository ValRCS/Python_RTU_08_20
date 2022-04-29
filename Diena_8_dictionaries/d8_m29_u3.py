# 3 uzdevums
 
# out of place returns new d  
def clean_dict_value(d, bad_val):
    # new_d = d.copy() # TOP - Down approach
    # for key,value in d.items():
    #         if bad_val == value: 
    #             del new_d[key] 
    # return new_d
    return {key: value for key, value in d.items() if value != bad_val} # bottom-up approach build up
 
og_dict = {'a':5,'b':6,'c':5, 'd':51}
new_dict = clean_dict_value(og_dict, 5)

print(og_dict)
print(new_dict)

# in place modifies existing dictionary
def clean_dict_value_in_place(d, bad_val):
    for key,value in d.copy().items():
        if bad_val == value: 
            del d[key] 
    return d

og_dict = {'a':5,'b':6,'c':5, 'd':51}
new_dict = clean_dict_value_in_place(og_dict, 5)

print(og_dict)
print(new_dict)

def clean_dict_values(d, bad_values):
    # new_d = d.copy()
    # for key,value in d.items():
    #     for i in bad_values:
    #         if value == i: 
    #             del new_d[key] 
    # return new_d
    return {key: value for key, value in d.items() if value not in bad_values}

og_dict = {'a':5,'b':6,'c':5, 'd':51}
new_dict = clean_dict_values(og_dict, [5,7,51])

print(og_dict)
print(new_dict)
