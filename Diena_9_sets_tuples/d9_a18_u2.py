#Second
def get_common_elements(seq1,seq2,seq3):
    seq1_set = set(seq1)
    seq2_set = set(seq2) 
    seq3_set = set(seq3)         
 
    common_elements = tuple(seq1_set & seq2_set & seq3_set)
    return common_elements

result = get_common_elements("abc",['a','b'],('b','c')) 
print(result)

def get_common_elements_many(*sequences):
    if len(sequences) == 0:
        return ()
    my_set = set(sequences[0])
    for seq in sequences:
        my_set.intersection_update(set(seq))  # IN PLACE
        # my_set = my_set.intersection(seq)  #rest are OUT OF PLACE
        # my_set = my_set & set(seq)
        # my_set &= set(seq)
    return tuple(my_set)

print(get_common_elements_many("abc",['a','b'],('b','c')) )
print(get_common_elements_many("abc",['a','b'],('b','c'),"abracadbra") )
print(get_common_elements_many("abc",['a','b'],('a','b','c'),"abracadbra") )