# # 3. Vārdnīcu tīrītājs

# 3.a  Uzrakstīt clean_dict_value(d, bad_val), kas atgriež attīrītu vārdnīcu

# Funkcijas parametri ir vārdnīca d, kas jāapstrādā, un vērtība  bad_val 
# no kuras jāatbrīvojas kopā ar ar tās atslēgu.

# clean_dict_value({'a':5,'b':6,'c':5}, 5) -> {'b':6} , 
# jo 5 bija vērtība gan a gan c atslēgām no kurām jāatbrīvojas.

# 3.b Uzrakstīt clean_dict_values(d, v_list), kas atgriež attīrītu vārdnīcu

# Funkcijas parametri ir vārdnīca d, kas jāapstrādā, un vērtību saraksts v_list no kurām jāatbrīvojas.

# clean_dict_values({'a':5,'b':6,'c':5}, [3,4,5]) -> {'b':6} , jo 5 bija vieno no vērtībām no kurām jāatbrīvojas.

# PS. Tīram mēs are del d['a'] protams tikai tad ja atslēga 'a' eksistē.

# !! Mainot vārdnīcas izmēru mēs nedrīkstam vienlaicīgi pa šo vārdnīcu staigāt(iterate)!

# Divi varianti: vai nu staigājam pa kopiju my_dict.copy.items(), vai arī būvējam jaunu vārdnīcu.
# # 

def clean_dict_value(d, bad_value) -> dict:
    """Removes all keys from dictionary d, that have value bad_value
    This is IN-PLACE removal, so the original dictionary is modified
    """	
    for key in d.copy(): # very important to iterate over a copy of the dictionary if we change keys
        if d[key] == bad_value:
            del d[key]
    return d # this is optional, since we are modifying the original dictionary

my_dict = {'a':5,'b':6,'c':5}
print(my_dict)
my_alias = clean_dict_value(my_dict, 5)
print(my_dict)
print(my_alias)
print("Result is actually same as original data", my_dict is my_alias)

# let's make a OUT OF PLACE version
def clean_dict_value_out_of_place(d, bad_value) -> dict:
    """Removes all keys from dictionary d, that have value bad_value
    This is OUT-OF-PLACE removal, so the original dictionary is NOT modified
    """	
    new_dict = {} # bottom up approach, we will build a new dictionary
    for key in d:
        if d[key] != bad_value:
            new_dict[key] = d[key]
    return new_dict # required, since we are creating a new dictionary

my_dict = {'a':5,'b':6,'c':5}
print(my_dict)
new_dict = clean_dict_value_out_of_place(my_dict, 5)
print(my_dict)
print(new_dict)
print("Result is actually same as original data", my_dict is new_dict)

# let's do a dictionary comprehension version
def clean_dict_value_comprehension(d, bad_value) -> dict:
    """Removes all keys from dictionary d, that have value bad_value
    This is OUT-OF-PLACE removal, so the original dictionary is NOT modified
    """	
    return {key: d[key] for key in d if d[key] != bad_value}

my_dict = {'a':5,'b':6,'c':5}
print(my_dict)
new_dict = clean_dict_value_comprehension(my_dict, 5)
print(my_dict)
print(new_dict)
print("Result is actually same as original data", my_dict is new_dict)

# finally let's do clean dict values
def clean_dict_values(d, bad_values) -> dict:
    """Removes all keys from dictionary d, that have value bad_value
    This is OUT-OF-PLACE removal, so the original dictionary is NOT modified
    """	
    return {key: d[key] for key in d if d[key] not in bad_values}

# alternative we could do this with a loop
def clean_dict_values_loop(d, bad_values) -> dict:
    """Removes all keys from dictionary d, that have value bad_value
    This is OUT-OF-PLACE removal, so the original dictionary is NOT modified
    """	
    new_dict = {}
    for key in d:
        if d[key] not in bad_values: # potentially slow on lists and tuples, since we are iterating over bad_values, set would be nice
            new_dict[key] = d[key]
    return new_dict
