def clean_dict_value(d,bad_value,good_value):
    dictionary= {} # so this will be OUT OF PLACE - we will not modify original dictionary
    for key in d:
        # value = d.get(key) no need for get since we know key exists
        value = d[key] # 100% sure key exists
        if  value == bad_value:
            value = good_value
        dictionary[key] = value
    return dictionary
print(clean_dict_value({'a':5, 'b':6, 'c':5},5,10))

my_dict = {'a':5, 'b':6, 'c':5}
result_dict = clean_dict_value(my_dict,5,10)
print(my_dict)
print(result_dict)

# one liner using dictionary comprehension
def clean_dict_value_2(d,bad_value,good_value):
    return {key: good_value if d[key] == bad_value else d[key] for key in d}

def replace_dict_value_3(d, bad_val, good_val):
    return {key: good_val if val == bad_val else val for key, val in d.items()}

# Dictionaries - 2. uzdevums #
 
def replace_dict_value_4(d, bad_val, good_val):
    result = {} # uztaisām vārdnīcu, kur glabāt vērtības
    for key, value in d.items(): # .items() metode, lai dabūtu key-value pārus
        if value == bad_val:
            result[key] = good_val
        else:
            result[key] = value
    return result

print(clean_dict_value_2({'a':5, 'b':6, 'c':5},5,10))
print(replace_dict_value_3({'a':5, 'b':6, 'c':5},5,10))

# all 4 functions are OUT OF PLACE - they do not modify original dictionary

# how about IN PLACE - modifying original dictionary
def clean_dict_value_in_place(d,bad_value,good_value):
    for key in d:
        # value = d.get(key) no need for get since we know key exists
        value = d[key] # 100% sure key exists
        if  value == bad_value:
            d[key] = good_value
    return d    

new_alias = clean_dict_value_in_place(my_dict,5,10)

print(my_dict)
print(new_alias)
print(my_dict is new_alias)