def get_common_elements(seq1,seq2,seq3, debug=False):
    common = set(seq1) & set(seq2) & set(seq3)
    if debug:
        print(f"Common elements are {common}")
    return tuple(common)

result_tuple = get_common_elements("abc",['a','b'],('b','c'))
print(result_tuple)  # izprintē ('b',)


def get_common_elements_more(arg1, *argn):
    my_set = set(arg1)
    for arg in argn:
        my_set = set(arg) & my_set
    return tuple(my_set)

print(get_common_elements_more("abcd",['a','b', 'd'],('d', 'b','c'), "abcde", "dbklsifjds"))
# there is even a more compact version

def get_common_elements_more_compact(*argn):
    '''
    First argument should be a set or a sequence
    '''
    return tuple(set.intersection(*argn))

print(get_common_elements_more_compact({"b","d"}, "abcd",['a','b', 'd'],('d', 'b','c'), "abcde", "dbklsifjds"))