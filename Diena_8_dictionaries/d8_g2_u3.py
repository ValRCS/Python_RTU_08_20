# def clean_dict_value(d, bad_val):
#     # r = dict(d)
#     # r = {**d} #alternative to above dict(d)
#     r = d.copy() # probably the most clear of the 3 methods 
#     for key, values in d.items():        
#             if values == bad_val:
#                 del r[key]
#     return r

def clean_dict_value(d,bad_v):
    return {k: v for k, v in d.items() if not v == bad_v} 
 
my_del = clean_dict_value({'a':5,'b':6,'c':5}, 5)
print(my_del)



#3b uzdevums
# def clean_dict_values(d, v_list):
#     r = dict(d)
#     for key, value in d.items():
#         if value in v_list:
#             del r[key]
#     return r
def clean_dict_values(d,v_list):
    return {k: v for k, v in d.items() if v not in v_list}
    
my_dels = clean_dict_values({'a':5,'b':6,'c':5, 'd': 3}, [4,5])
print(my_dels)