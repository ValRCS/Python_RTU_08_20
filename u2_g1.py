# def replace_dict_value(d, bad_val, good_val):
#     for key, value in d.items() :
#         if value == bad_val:
#            d[key] = good_val
#     return d


# my_dict = {'h': 1, 'u': 2, 'b': 5, 'a': 2}
# print(replace_dict_value(my_dict, 2, 7))
# print(my_dict)

# def clean_dict_valuesOR(d: dict, v_list: list) -> dict:
#     temp_dict = d.copy()
#     for k in temp_dict:
#         if d[k] in v_list:
#             deleted_value = d.pop(k) # deletes the key  but returns value, here works the same as del
#             print(f"We deleted {deleted_value=}")
#     return d


def clean_dict_valuesOR(d: dict, v_list: list) -> dict:
    return {k:v for k,v in d.items() if d.get(k) not in v_list}

# print(clean_dict_valuesOR("Valdis", [3,4,5]))
print(clean_dict_valuesOR({'a':5,'b':6,'c':5, 'd':4}, [3,4,5]))