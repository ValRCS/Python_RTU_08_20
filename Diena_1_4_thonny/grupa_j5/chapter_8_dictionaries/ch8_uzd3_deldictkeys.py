d={'a':5,'b':6,'c':5}
bad_val=5
 
def clean_dict_value(d, bad_val):
    """Modifies dictionary in place"""	
    print(f"clean_dict_value({d}, {bad_val})", end="")
    for key in d.copy() :
        if d[key]==bad_val :
            del d[key]
    print(f" -> {d}" )
    # i could return d but it is not necessary since i modify in place
    return d

print(d)
clean_dict_value(d, bad_val)
print(d)

# how about out of place
def clean_dict_value_out_of_place(d, bad_val):
    """Returns new dictionary"""
    print(f"clean_dict_value_out_of_place({d}, {bad_val})", end="")
    result = {}
    for key, value in d.items():
        if value != bad_val:
            result[key] = value
    print(f" -> {result}" )
    return result # crucial that we return result since we do not modify original dictionary

def clean_dict_value_out_of_place_2(d, bad_val):
    '''Returns new dictionary - OUT OF PLACE - using dictionary comprehension'''	
    return {key: value for key, value in d.items() if value != bad_val}  

# out of place
#8.nodarbîba 3.b uzd 
def clean_dict_values(d, v_list):
    '''Returns new dictionary - OUT OF PLACE'''	
    f_dict = d.copy()
    for key,value in d.items():
        if value in v_list:
            del f_dict[key] # so we modify f_dict, not d!
    return f_dict

# how about dictionary comprehension version
def clean_dict_values_2(d, v_list):
    '''Returns new dictionary - OUT OF PLACE - using dictionary comprehension'''	
    return {key: value for key, value in d.items() if value not in v_list}