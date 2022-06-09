# IN PLACE - we do modify the dictionary coming in
def replace_dict_value(d, bad_val, good_val):
    for key, value in d.items():
        # my_value=d.get(key)
        if value==bad_val:
            d[key]=good_val
    return d # optional since this is in place

# keeps original intact, returns a new dictionary
def replace_dict_value_out_of_place(d, bad_val, good_val):
    # new_dict={}
    # for key, value in d.items():
    #     if value==bad_val:
    #         new_dict[key]=good_val
    #     else:
    #         new_dict[key]=value
    # return new_dict 
    # same as above in one line
    return {key: good_val if value==bad_val else value for key, value in d.items()}

my_dict={'a':5,'b':6,'c':5}
# my_dict['a']=5
# my_dict['b']=6
# my_dict['c']=5
print("ORIGINAL", my_dict)
n_dict = replace_dict_value_out_of_place(my_dict, 5, 8)
print("NEW", n_dict)
print("ORIGINAL", my_dict) # still unchanged
replace_dict_value(my_dict, 5, 10)
print("ORIGINAL but changed", my_dict)  # now changed


 