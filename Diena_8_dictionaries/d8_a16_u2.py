# 2. Vārdnīcu labotājs
# Uzrakstīt replace_dict_value(d, bad_val, good_val), kas atgriež vārdnīcu ar nomainītām vērtībām
# Funkcijas parametri ir vārdnīca d, kas jāapstrādā, un vērtības bad_val kura jānomaina uz good_val
# clean_dict_value({'a':5,'b':6,'c':5}, 5, 10) -> {'a':10,'b':6,'c':10} , jo 5 bija vērtība, kas jānomaina.
import string
 
# def replace_dict_value(d, bad_val, good_val):
#     newDic = {} # with this we do not destory the old dictionary
#     for i in d:
#         if d[i] == bad_val:
#             newDic[i] = good_val
#         else:
#             newDic[i] = d[i]
#     print(newDic)
#     return newDic

def replace_dict_value(d, bad_val, good_val):
    d = {"a": 5, "b": 6, "c": 5}
    key_list = list(d.keys())
    val_list = list(d.values())
    new_val_list = [good_val if x == bad_val else x for x in val_list]
    new_d = dict(zip(key_list, new_val_list))
    return new_d
 
print(replace_dict_value({"a": 5, "b": 6, "c": 5}, 5, 10))
 
 
replace_dict_value({'a': 5, 'b': 6, 'c': 5}, 5, 10)

alpha_dict = dict(zip(string.ascii_lowercase, string.ascii_uppercase))
print(alpha_dict)