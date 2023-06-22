#2. uzd
# def get_common_elements(seq1,seq2,seq3):
#     common_elem = []
#     # the following approach will work
#     # but it is not efficient
#     # for large sequences it will take a lot of time
#     # because we need to check arbitrary number of times
#     # in arbitrary type of sequences
#     # instead we should convert our sequences to sets
#     # to get that O(1) membership testing 
#     for elem in seq1:
#         if not(elem in common_elem) and (elem in seq2) and (elem in seq3):
#             common_elem.append(elem)
#     return tuple(common_elem)

# programma kas atgriež kopīgo no 3 listiem
def get_common_elements(seq1,seq2,seq3, debug=False) -> tuple:
    """
    Returns tuple of common elements from 3 sequences
    Args:

        seq1 (iterable): first sequence
        seq2 (iterable): second sequence
        seq3 (iterable): third sequence
    
    """	
    common_list = set(seq1).intersection(seq2).intersection(seq3)
    if debug:
        print(common_list)
    return tuple(common_list)
 
print(get_common_elements("abc",['a','b'],('b','c')))


def common(*args):
    """Return common elements from any number of sequences."""	
    list_of_sets=[]
    for seq in args:
        # print(repr(set(i)))
        converted_to_str={ str(s) for s in set(seq) }
        list_of_sets.append(converted_to_str)
        intersect=set.intersection(*list_of_sets)
    return tuple(intersect)

# alternative in one line - so called code golf
def common_one_liner(*args):
    return tuple(set.intersection(*[set(seq) for seq in args]))
 
kopa=(1,2,4,9)
saraksts=[7,3,2,9]
virkne="1209483"
 
kopejie=common(kopa,saraksts,virkne)
print(kopejie)

print(common_one_liner("abc",['a','b'],('b','c')))