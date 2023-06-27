# 2. Vārdnīcu labotājs

# Uzrakstīt replace_dict_value(d, bad_val, good_val), kas atgriež vārdnīcu ar nomainītām vērtībām

# Funkcijas parametri ir vārdnīca d, kas jāapstrādā, un vērtības bad_val kura jānomaina uz good_val

# replace_dict_value({'a':5,'b':6,'c':5}, 5, 10) -> {'a':10,'b':6,'c':10} , 
# jo 5 bija vērtība, kas jānomaina.

def replace_dict_value(d, bad_val, good_val):
    """Replaces bad_val with good_val in dictionary d
    This is IN-PLACE replacement, so the original dictionary is modified
    """	
    for key in d:
        if d[key] == bad_val:
            d[key] = good_val
    return d # this is optional, since we are modifying the original dictionary

my_dict = {'a':5,'b':6,'c':5}
print(my_dict)
my_alias = replace_dict_value(my_dict, 5, 10)
print(my_dict)
print("Result is actually same as original data", my_dict is my_alias)

# so if we want OUT OF PLACE replacement, we need to create a new dictionary
def replace_dict_value_out_of_place(d, bad_val, good_val):
    """Replaces bad_val with good_val in dictionary d
    This is OUT-OF-PLACE replacement, so the original dictionary is NOT modified
    """	
    new_dict = {} # start with empty dictionary
    for key in d:
        if d[key] == bad_val:
            new_dict[key] = good_val
        else:
            new_dict[key] = d[key]
    return new_dict # required, since we are creating a new dictionary

my_dict = {'a':5,'b':6,'c':5}
print(my_dict)
new_dict = replace_dict_value_out_of_place(my_dict, 5, 10)
print(my_dict)
print(new_dict)
print("Result is actually same as original data", my_dict is new_dict)

# we could also use dictionary comprehension
def replace_dict_value_out_of_place_2(d, bad_val, good_val):
    """Replaces bad_val with good_val in dictionary d
    This is OUT-OF-PLACE replacement, so the original dictionary is NOT modified
    """	
    # we use ternary operator to decide what value to put in the new dictionary
    return {key: good_val if d[key] == bad_val else d[key] for key in d}