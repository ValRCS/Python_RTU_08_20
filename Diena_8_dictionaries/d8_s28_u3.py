#3.a
# OUT OF PLACE - returns new dictionary via dictionary comprehension
def clean_dict_value(d, bad_val):
    return {key:value for key,value in d.items() if value != bad_val}        
 
og_dict =  {'a':5,'b':6,'c':5, 'd':3}
new_dict = clean_dict_value(og_dict, 5)
print(og_dict)
print(new_dict)

# 3B
# OUT OF PLACE
def clean_dict_values(d, v_list):
    return {key:value for key,value in d.items() if value not in v_list}
 
print(clean_dict_values({'a':5,'b':6,'c':5}, [3,4,5]))

og_dict =  {'a':5,'b':6,'c':5, 'd':3}
new_dict = clean_dict_values(og_dict, [3,4,5])
print(og_dict)
print(new_dict)