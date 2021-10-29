#2.
def get_common_elements(seq1, seq2, seq3):
    
    seq1_to_set = set(seq1)
    seq2_to_set = set(seq2)
    seq3_to_set = set(seq3)
    common_elements = tuple(seq1_to_set & seq2_to_set & seq3_to_set)
    return common_elements

print(get_common_elements("abc",['a','b'],('b','c')))
print(get_common_elements("abcde",['a','b','c','f'],('a','b','c')))


# returns union of all elements from all sequences
def get_all_elements_union(*sequences):
    """
    >>> get_common_elements_unlimited("abc",['a','b'],('b','c'))
    """
    common_elements = set()
    for seq in sequences:
        common_elements.update(seq)  # we will get union of all sets
    return tuple(common_elements)

print(get_all_elements_union("abcde",['a','b','c','f'],('a','b','c')))


def get_all_sequences_intersection(*sequences):
    # common_elements = set()  # copilot makes an error here
    if len(sequences) == 0:
        return ()  # empty tuple
    common_elements = set(sequences[0])
    for seq in sequences[1:]:  # we loop through the rest of the sequences
        # common_elements.intersection(seq)  # we will get union of all sets
        common_elements = common_elements & set(seq)  # same as above
    return tuple(common_elements)


print(get_all_sequences_intersection("abcde",['a','b','c','f'],('a','b','c')))
print(get_all_sequences_intersection("abcde"
        ,['a','b','c','f']
        ,('a','b','c')
        , "kartupelis ar bietēm"))
print(get_all_sequences_intersection())