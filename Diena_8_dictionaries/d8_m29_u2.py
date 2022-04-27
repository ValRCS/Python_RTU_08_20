# IN PLACE
def replace_dict_value(d: dict, bad_val=5, good_val=42) -> dict:
    """
    Atgriež iedoto vārdnīcu ar nomainītām vērtībām
    :param d: vārdnīca, kas jāapstrādā
    :param bad_val: vērtība kura jānomaina
    :param good_val: vērtība uz kuru jānomaina
    :return: Atgriež vārdnīcu ar nomainītām vērtībām
    """
    for key_f, value_f in d.items():  # Ejam cauri vārdnīcai
        if value_f == bad_val:  # Pārbaudam katra atslēgas vārda vērtību uz sakrītību ar bad_val
            d[key_f] = good_val  # Ja sakrīt, tad nomainām atslēgas vārda vērtību pret good_val
    return d

og_dict = {'a':5,'b':6,'c':5, 'd':51}
new_dict = replace_dict_value(og_dict)

print(og_dict)
print(new_dict)

# out of place returns new d
def replace_dict_value_out_of_place(d: dict, bad_val=5, good_val=42) -> dict:
    return {key: (good_val if val == bad_val else val) for key, val in d.items()}

og_dict = {'a':5,'b':6,'c':5, 'd':51}
new_dict = replace_dict_value_out_of_place(og_dict)

print(og_dict)
print(new_dict)
