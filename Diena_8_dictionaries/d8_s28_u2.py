
# OUT OF PLACE retuns new different dictionary
def replace_dict_value(d, bad_val, good_val):
    new_dict = {}
    for key, value in d.items():
        if bad_val == value:
            new_dict[key] = good_val
        else:
           new_dict[key] = value
    return new_dict

og_dict =  {'a':5,'b':6,'c':5}
print(og_dict)
fresh_dict = replace_dict_value(og_dict , 5, 10)
print("Original dict:",og_dict)
print("New dict:", fresh_dict)

# IN PLACE version which modifies the original
def replace_dict_value_in_place(d, bad_val, good_val):
    for key in d:  #check a keys to correct bad values - will be the same as "i in d:
        if d[key] == bad_val: #check for bad value 5 in dictionary
            d[key] = good_val #set good value if i == 5
    return d  # returns alias for d we could even survive without this return since d is already changed

og_dict =  {'a':5,'b':6,'c':5}
print(og_dict)
fresh_dict = replace_dict_value_in_place(og_dict , 5, 10)
print("Original dict:",og_dict)
print("New dict:", fresh_dict)