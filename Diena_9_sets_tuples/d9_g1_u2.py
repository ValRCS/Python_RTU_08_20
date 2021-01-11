#2.uzdevums
# def get_common_elements(seq1,seq2,seq3):
#     seq1_set = set(seq1)
#     seq2_set = set(seq2) 
#     seq3_set = set(seq3)         
 
#     intersected_values = tuple(seq1_set & seq2_set & seq3_set)
#     return intersected_values
 
 
# print(get_common_elements("abcd",['a','b'],('b','c'))) 

#2.excersise - multiple (unknown count) elements
def get_common_elements(sequences):
    if len(sequences) == 0: # for safety
        return ()
    intersect = set(sequences[0])
    for n in sequences:
        intersect = intersect & set(n)        
    return tuple(intersect)
 
def get_common_elements_many(*args):
 
    firsttime = True
    for arg in args:
        if not firsttime:
            common_el = common_el & set(arg)
        else:
            common_el = set(arg)    #first time no intersection possible
            firsttime = False
            
    return tuple(common_el)

different_elements = ["abs",['a','b','s'],('b','c','s','p'),"klb",('b','c','s','p'), set("kartupelisb")]
common_letters = get_common_elements(different_elements)
common_letters_many = get_common_elements_many(*different_elements)
print(common_letters, common_letters_many)