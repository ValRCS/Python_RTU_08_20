def get_common_elements(seq1,seq2,seq3):
    common = set(seq1) & set(seq2) & set(seq3)
    return tuple(common)
 
print(get_common_elements("abcd",['a','b', 'd'],('b','c', 'd')))
# , {"a","b","c","d", "e"}

def get_common_elements_multi(*multy_arg):
 
    if len(multy_arg) == 0:
        return ()
    my_set = set(multy_arg[0])
 
    for el in multy_arg[1:]:
        my_set = my_set.intersection(set(el))
 
    return tuple(my_set)

print(get_common_elements_multi("abcd",['a','b', 'd'],('b','c', 'd'), {"a","b","c","d", "e"}, {"a","c","d", "e"}))
print(get_common_elements_multi("Valdis", "Voldemārs", "Voldemorts", "Volodja"))
print(get_common_elements_multi())