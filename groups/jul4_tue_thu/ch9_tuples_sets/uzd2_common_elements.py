# 2.2 Kopējie Elementi
# Uzrakstiet funkciju,kas atgriež tuple ar kopējiem elementiem trijās virknēs. Virknes var būt list,tuple,string.
 
def get_common_elements(*sequences):
    if len(sequences) == 0:
        return tuple() # empty tuple
    common_elements = set(sequences[0]) # we can not start with empty set!
    # TODO first sequence has to be tuple,string or list
    # we can not intersect with empty set we will get empty set!
    for sequence in sequences[1:]:
        # let's check if sequence is tuple,string or list
        if isinstance(sequence, (tuple, str, list, set)):
            common_elements.intersection_update(sequence) # inplace update
        # alternative
        # common_elements = common_elements.intersection(sequence)
        # shortcut alternative
        # common_elements &= set(sequence)
    return tuple(common_elements)
 
result = get_common_elements("abc", ['a', 'b'], ('b', 'c'))
print(result)  # ('b',)
# we can pass in 5 sequences
result = get_common_elements("abc", ['a', 'b'], ('b', 'c'), "ab", "bc")
print(result)  # ('b',)
# we can pass in one sequence
result = get_common_elements("abcefddddddd")
print(result)  # ('d',)