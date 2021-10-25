def get_common_elements(seq1,seq2,seq3):
    seq1=set(seq1)    
    seq2=set(seq2) 
    seq3=set(seq3)
    return tuple(seq1 & seq2 & seq3)
 
print(get_common_elements("abc",['a','b'],('b','c')))
print(get_common_elements("abcd",['a','b', 'd'],('b','c', 'd')))


def get_common_elements_extended(*sequences) -> tuple:
    if len(sequences) == 0:
        return tuple()
    result_list = []
    for n in sequences:
        result_list.append(set(n))
    final = set(result_list[0]) 
    for n in result_list[1:]:
        final = final & n  # &= also should work
    return tuple(final)

print(get_common_elements_extended("abc", ['a','b'], ('b', 'c')))
print(get_common_elements_extended("abc", ['a','b'], ('b', 'c'), ["d", "a", "f", "b"]))
print(get_common_elements_extended("abc"))
print(get_common_elements_extended())