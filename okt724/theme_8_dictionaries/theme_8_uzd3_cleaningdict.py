# 3.a
# clean_dict_value({'a':5,'b':6,'c':5}, 5) -> {'b':6} , jo 5 bija vērtība gan a gan c atslēgām no kurām jāatbrīvojas.
def clean_dict_value(d:dict, bad_val):
    """
     # we delete keys from dictionary - here it is IN PLACE operation
    """
    # so called TOP-DOWN approach   
    for key, value in d.copy().items():
        if value == bad_val:
            del d[key]
    return d

original_dict = {'a':5,'b':6,'c':5}
clean_dict = clean_dict_value(original_dict, 5)
print(original_dict)
print(clean_dict)
# check if the objects are same
print("Dictionaries are the same object?", original_dict is clean_dict)

# we have another appproach to do this BOTTOM-UP
# this will lead to OUT OF PLACE operation - new dictionary will be created
def clean_dict_value_out_of_place(d:dict, bad_val):
    """
    # we create a new dictionary - here it is OUT OF PLACE operation
    # original dictionary is not changed
    """
    new_dict = {} # in BOTTOM UP approach we create new dictionary
    for key, value in d.items():
        if value != bad_val:
            new_dict[key] = value
        # no else needed here this is for the bad values
    return new_dict

original_dict = {'a':5,'b':6,'c':5}
clean_dict = clean_dict_value_out_of_place(original_dict, 5)
print(original_dict)
print(clean_dict)
# check if the objects are same
print("Dictionaries are the same object?", original_dict is clean_dict)

def clean_dict_values(d:dict, bad_values:list) -> dict:
    """
    IN PLACE cleaning of dictionary values
    MODIFIES original dictionary
    """
    for key, value in d.copy().items():
        if value in bad_values: # check if current value is in bad_values list(set or tuple)
            del d[key]
    return d

original_dict = {'a':5,'b':6,'c':5, 'd': 10, "egle": 15, "f": 15}
clean_dict = clean_dict_values(original_dict, [5, 15])
print(original_dict)
print(clean_dict)
# check if the objects are same
print("Dictionaries are the same object?", original_dict is clean_dict)

def clean_dict_values_out_of_place(d:dict, bad_values:list) -> dict:
    """
    OUT OF PLACE cleaning of dictionary values
    Does not modify original dictionary
    """
    new_dict = {} # AGAIN BOTTOM UP approach start with blank dictionary
    for key, value in d.items():
        if value not in bad_values: # check if current value is not in bad_values list(set or tuple)
            new_dict[key] = value
    return new_dict

original_dict = {'a':5,'b':6,'c':5, 'd': 10, "egle": 15, "f": 15}
clean_dict = clean_dict_values_out_of_place(original_dict, [5, 15])
print(original_dict)
print(clean_dict)
# check if the objects are same
print("Dictionaries are the same object?", original_dict is clean_dict)
