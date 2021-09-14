#2.uzdevums
def get_common_elements(seq1,seq2,seq3):
    return tuple(set(seq1) & set(seq2) & set(seq3))

print(get_common_elements("abcd",['a','b', 'd'],('b','c', 'd'))) 

### 2. Task  with STAR
#### Common elements 
def get_common_elements(*seq1):
 
    if len(seq1) == 0: 
        return ()
    
    common_set = set(seq1[0])
    for seq_n in seq1[1:]: # this will not run if we have less than 2 sequences
        common_set = common_set.intersection(set(seq_n))
 
    return tuple(common_set)


print(get_common_elements("abctyii"))
print(get_common_elements("abc",('b','c','adfad')))
print(get_common_elements("abc",['a','b'],('b','c')))
print(get_common_elements("ahjkfb",['a','b', 'j', 'h'],('b','c', 'a', 'h'), ('a', 'hb')))
print(get_common_elements())
print(get_common_elements(["ab"]))