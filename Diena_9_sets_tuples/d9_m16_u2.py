## 2.uzdevums
# 2.uzdevums
def get_common_elements_3(seq1,seq2,seq3):
    my_set1 = set(seq1)
    my_set2 = set(seq2)
    my_set3 = set(seq3)
    common_el = my_set1 & my_set2 & my_set3
    return tuple(common_el)

def get_common_elements(*seq):
    # base case
    if len(seq) == 0:
        return tuple()

    common_elements = set(seq[0])

    for el in seq[1:]:
        common_elements = common_elements & set(el)
        # common_elements = common_elements | set(el) # if we need all elements

    return tuple(common_elements)
 
print(get_common_elements_3("abc",['a','b'],('b','c')))
print(get_common_elements("abc",['a','b'],('b','c')))

print(get_common_elements("abc",['a','b'],('b','c'),"abra"))
print(get_common_elements("abc",['a','b'],('b','c','a','d'),"abrac"))
print(get_common_elements("abc",['a','b'],('b','c','a','d'),"abrac",{"a","b","c"}))