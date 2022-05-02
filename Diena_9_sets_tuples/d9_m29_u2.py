# 2 uzdevums
 
def get_common_elements(seq1,seq2,seq3):
    my_list = set(seq1)
    my_list2 = set(seq2)
    my_list3 = set(seq3)
    result = tuple(my_list.intersection(my_list2, my_list3))
    return result
print(get_common_elements("abcd",['a','b'],('b','c')))


def get_common_elements_all(*sequences) -> tuple:
    """
    :param sequences: funkcija apstrāda patvalīgu skaitu virkņu (list, tuple, string)
    :return: atgriež tuple ar kopējiem elementiem virknēs
             vai NONE, ja funkcijai nav iedota vismāz viena virkne
    """
    # Sākumā pārbaudām, vai funkcijai iedota vismaz viena virkne un visas virknes ir (list, tuple, string)
    if sequences and all(isinstance(x, (list, tuple, str)) for x in sequences):
        # new_set = set(sequences[0])  # Izveidojām jauno set() no pirmās iedotas virknes
        # for seq in sequences:  # Ejam cauri visām funkcijai iedotām virknēm
        #     new_set &= set(seq)  # Ar loģisko AND atstājam tikai kopējus elementus visās virknēs
        # return tuple(new_set)
        return tuple(set.intersection(*map(set, sequences)))
    return () # Ja funkcijai nav iedota vismaz viena virkne, tad atgriežam tuple ar tukšu elementu

print(get_common_elements_all("abcd",['a','b'],('b','c')))
print(get_common_elements_all("abcd",['a','b','c'],('b','c','y'),"abracadbra"))
print(get_common_elements_all("abcd",['a','b','c'],('b','c','y'),"abracadbra", 'abbbba'))

print([1,2,3,6,7])
print(*[1,2,3,6,7]) # will unroll a tuple as well
# same as
print(1,2,3,6,7)