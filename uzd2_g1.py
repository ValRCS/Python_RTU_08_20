# Māras risinājums
vardnica = {'a': 5, 'b': 6, 'c': 5}


def replace_dict_value(d, bad_val, good_val):
    for key, value in d.items():
        # in this case we dont need to make a copy because no size change
        if value == bad_val:
            d[key] = good_val
    return d


replace_dict_value(vardnica, 5, 10)
print(vardnica)
replace_dict_value(vardnica, 6, 33)
print(vardnica)
replace_dict_value(vardnica, 0, 66)
print(vardnica)
