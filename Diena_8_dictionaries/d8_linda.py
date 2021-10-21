# count_letters = input(f"Ievadi savu tekstu")
from collections import Counter


count_letters = "Hubba bubba"

def get_char_count(text: str) -> dict:
    new_dict = {}
    for i in text.upper():
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1
    return new_dict
print(get_char_count(count_letters))
print(get_char_count("Abracadabra magija mana"))

n_dict = {n:0 for n in range(10)}
print(n_dict)

# using Python standard library
count = Counter(count_letters)
print(count)
print(count.most_common())
