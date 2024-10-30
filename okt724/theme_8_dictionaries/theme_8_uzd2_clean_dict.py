# 2. Vārdnīcu labotājs
# clean_dict_value({'a':5,'b':6,'c':5}, 5, 10) -> {'a':10,'b':6,'c':10} , jo 5 bija vērtība, kas jānomaina.
def replace_dict_value_in_place(d:dict, bad_val, good_val):
    # if I wanted this OUT OF PLACE
    # I would have to create a new dictionary
    # we could simply copy the dictionary here
    # d = d.copy() # this would not overwrite the original dictionary!
    # we would have a copy of the dictionary inside the function
    for key, value in d.items(): # we do not need copy of keys
        # because we do not change the size of the dictionary
        if value == bad_val:
            d[key] = good_val
    return d # since this was IN PLACE operation we do not need to return anything
 
print(replace_dict_value_in_place({'a':5,'b':6,'c':5}, 5, 10))
old_dict = {'a':5,'b':6,'c':5,'d':5,'egle':15}
new_dict = replace_dict_value_in_place(old_dict, 5, 10)
# first let's check if contents match
print("Are contents of old and new dict the same?", old_dict == new_dict)
# we can check if old_dict and new_dict are the same object
print("Are old and new dict the same object?", old_dict is new_dict)
# is check if two objects are the same object in memory

# let's do the same out of place
def replace_dict_value(d:dict, bad_val, good_val):
    # so called bottom up approach
    new_dict = {}
    for key, value in d.items(): # loop through old one
        if value == bad_val:
            new_dict[key] = good_val
        else:
            new_dict[key] = value
    return new_dict # here we NEED to return the new dictionary else it is lost
    # also we could do the same with dictionary comprehension
    # return {key: good_val if value == bad_val else value for key, value in d.items()}
# this utilizes ternary operator (conditional expression)

really_new_dict = replace_dict_value(old_dict, 10, 20)
# print contents of both dictionaries
print(old_dict)
print(really_new_dict)
# we can see that dictionaries are different now