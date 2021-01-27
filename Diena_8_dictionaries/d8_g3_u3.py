test = {'a': 5, 'b': 6, 'c' :5}
print("initial ", test)
def clean_dict_value(d, bad_val):
    # for k in list(d):
    for k in d.copy():
        if d[k] == bad_val:
            del d[k]
 
print("before changes ",test) 
print(list(test)) # so list(test) is actually shorthand for list(test.keys())

clean_dict_value(test, 5)
 


print("after changes ",test)

# 3b #out of place
def clean_dict_values(d, bad_value_list):
    return {k:v for k,v in d.items() if v not in bad_value_list}

# we can zip together two sequences and use them as we wish
new_dict = {k:v*v for k,v in zip("kartupelis", range(10))}
print(new_dict)

cleaned_dict = clean_dict_values(new_dict, [4,64,25])
print(cleaned_dict)