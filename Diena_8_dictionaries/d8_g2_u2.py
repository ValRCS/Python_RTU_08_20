# def replace_dict_value(d,bad_val,good_val):
#     dict_new = {}
#     for key,val in d.items():
#         if val == bad_val:
#             dict_new[key]=good_val
#         else:
#             dict_new[key]=val
#     print(dict_new)

def replace_dict_value(d, bad_val, good_val):
    return {k: good_val if v == bad_val else v for k, v in d.items()}
print(replace_dict_value({'a':5,'b':6,'c':5}, 5, 10))