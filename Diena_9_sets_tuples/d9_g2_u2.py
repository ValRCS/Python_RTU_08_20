def get_common_elements(seq1,seq2,seq3):
    return tuple(set(seq1) & set(seq2) & set(seq3))
 
print(get_common_elements("abc",['a','b'],('b','c','d'))) 


#2.uzd.B
def get_common_elements_(*seqs):
    if len(seqs) == 0:
        return () # to keep consistent
    common_values = set(seqs[0])
    for seq in seqs[1:]:
        common_values = common_values & set(seq)
    return tuple(common_values)

print(get_common_elements_("abc",['a','b'],('b','c','d'),{"a","b"},{"c"})) 