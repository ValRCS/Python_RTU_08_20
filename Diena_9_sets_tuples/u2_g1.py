def get_common_elements(seq1,seq2,seq3):
    a=set(seq1)
    b=set(seq2)
    c=set(seq3)
    # return tuple(list(set(a) & set(b) & set(c)))
    return tuple(a & b & c)
print(get_common_elements("abcd",['a','b','d'],('b','c','d','e')))
print(get_common_elements("kartupelis", "valdis", "visvaldis"))