def get_common_elements(seq1, seq2, seq3):
    return tuple(set(seq1) & set(seq2) & set(seq3))

print(get_common_elements("abce", ['a', 'b', 'e'], ('b', 'c', 'e')))

def get_common_elements_many(*seq):
    # return tuple(set.intersection(*map(set, seq)))
    # my_set = set(seq[0]) # need to also check for len 0
    # for item in seq[1:]:
    #     my_set = my_set & set(item)
    # return my_set
    my_sets = [set(item) for item in seq] # if we did not know about map 
    return tuple(set.intersection(*my_sets))

print(get_common_elements_many("abce", ['a', 'b', 'e'], ('b', 'c', 'e')))
print(get_common_elements_many("abce", ['a', 'b', 'e'], ('b', 'c', 'e'), "kartupelis"))