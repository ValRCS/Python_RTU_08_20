def replace_dict_value(d, bad_values):    
    """
    IN PLACE removal of key-values from bad values list
    """         
    for key, value in d.copy().items():         
        for n in bad_values:                       
            if n == value:                      
                del d[key]  

d = {'a':5,'b':6,'c':5, 'd':4, 'e':55}  
bad_list = [3,4,5]      

replace_dict_value(d, bad_list)                  
print(d)  

d2 = {'a':5,'b':6,'c':5, 'd':4, 'e':55}  
def clean_dict_values(d: dict, rogue_values: list) -> dict:
    """
    OUT OF PLACE bad value removal
    """
    return {key: value for key, value in d.items() if not value in rogue_values}
d2_clean = clean_dict_values(d2, bad_list)
print(d2)
print(d2_clean)