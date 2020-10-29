# def replace_dict_value(d, bad_val, good_val):
#     myDict = d
#     for x in myDict: # same as going through x in myDict.keys()
#         if myDict[x] == bad_val:
#             myDict[x] = good_val
#     return myDict

# if i do not want to mutate the original dictionary
# then dictionary comprehension will be easiest and fastest
# 2. Vārdnīcu labotājs

def replace_dict_value(d, bad_val, good_val):
    return {k: good_val if v == bad_val else v for k, v in d.items()}
 


print(replace_dict_value({'a':5,'b':6,'c':5}, 5, 10))