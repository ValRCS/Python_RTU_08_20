def clean_dict_value(d, bad_val):
    # new_list = []
    new_dict = {}
    print(f"Incoming dictionary: {d}")
    for k, v in d.items():
        if v != bad_val:
            # new_list.append((k, v))
            new_dict[k] = v
    # return dict(new_list)
    return new_dict


my_dict = {'a': 5, 'b': 6, 'c': 5, 'd': 666}
val = 5
res_dict = clean_dict_value(my_dict, val)
clean_666 = clean_dict_value(my_dict, 666)
print(res_dict)
print(my_dict)
print(clean_666)


# # def clean_dict_value(d, bad_val):
# #     for key, value in d.copy().items():
# #         if value == bad_val:
# #             del d[key]
# #             # d.popitem()
# #             # d.update()
# #     return d


# def clean_dict_value(d, bad_val):
#     while bad_val in d.values():
#         del d[list(d.keys())[list(d.values()).index(bad_val)]]
#     return d


# # my_dict.copy()  # returns a shallow copy
# result = clean_dict_value({'a': 5, 'b': 6, 'c': 5}, 5)
# print(result)
