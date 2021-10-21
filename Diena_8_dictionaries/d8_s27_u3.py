# 3. uzdevums
def clean_dict_value(d, bad_val):
    d_copy = d.copy()
    for k,v in d_copy.items():
        if v == bad_val:
            if k in d.keys():
                del d[k]
    return d


print(clean_dict_value({'a':5,'b':6,'c':5}, 5))

old_d = {'a':5,'b':6,'c':5, 'd':20}

import random
import string

random_d = {k:random.randint(1,6) for k in string.ascii_lowercase}
print(random_d)

clean_d = clean_dict_value(random_d, 6)
print(random_d)
print(clean_d)
print("same dict?", random_d is clean_d)

# in place
def clean_dict_values(d, v_list):
    d_copy = d.copy()
    # if we wanted to have out of place we would iterate over old dict and change the new one
    for k,v in d_copy.items():
        if v in v_list:
            if k in d.keys():
                del d[k]
    return d

no_34 = clean_dict_values(clean_d, [3,4])
print(no_34)
print("Same dict for all 3 ", random_d is clean_d is no_34)

# OUT OF PLACE makeing a new dict
def clean_dict_values_oop(d, v_list):
    return {k:v for k,v in d.items() if v not in v_list}

no_12 = clean_dict_values_oop(no_34, [1,2])

print(no_34)
print(no_12)

dict_size = 10_000_000

# so huge dictionary of completely random key and completely random value

big_dict = {random.randint(1, 100_000_000):random.randint(1, 100_000_000) for _ in range(dict_size)}
# birthday paradox says we will have some collissions
# https://en.wikipedia.org/wiki/Birthday_problem
print(len(big_dict))