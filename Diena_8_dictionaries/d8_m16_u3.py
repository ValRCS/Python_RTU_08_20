# 3a.uzdevums
# IN PLACE we modify the dictionary coming in
def clean_dict_value(d, bad_val):
    # temp_dict = d.copy()
    for key in d.copy():
        if d[key] == bad_val:
            d.pop(key) # or del d[key]
    return d

# 3a.uzd.
def clean_dict_value_out_of_place(d, bad_val):
    # d = {k: v for k, v in d.items() if v != bad_val} # this creates a pointer to different dictionary
    return {k: v for k, v in d.items() if v != bad_val}

my_dict = {'a':5,'b':6,'c':5, 'd':5}	
clean_dict = clean_dict_value_out_of_place(my_dict, 5)
print(my_dict)
print(clean_dict)
print("Dictionaries are actually same object? ", my_dict is clean_dict)

print("ORIGINAL", my_dict)
also_dict = clean_dict_value(my_dict, 5)
print(my_dict)
print(also_dict)
print("Dictionaries are actually same object? ", my_dict is also_dict)

# 3b.uzd.
def clean_dict_values(d, bad_value_list):
    # for bad_value in bad_value_list:
    #     clean_dict_value(d, bad_value)  # in place
    # return d
    # simpler
    return {k: v for k, v in d.items() if v not in bad_value_list}

og_dict = {'a':5,'b':6,'c':5, 'd':5, 'e':5, 'f':7, 'g':5, 'h':8}
clean_dict = clean_dict_values(og_dict, [5,7])
print(og_dict)
print(clean_dict)
