# def get_common_elements(seq1, seq2, seq3):
#     result = set(seq1) & set(seq2) & set(seq3)
#     return tuple(result)


# seq1 = (2, 3, 5, 8)
# seq2 = [2, 8, 4]
# seq3 = (7, 9, 2, 8)
# print(get_common_elements(seq1, seq2, seq3))

def get_common_all(*argv):
    my_set = set(argv[0])
    for seq in argv[1:]:
        my_set = my_set & set(seq)
    return my_set


print(get_common_all([1, 2, 3], [1, 2, 3, 4], range(7), range(10)))
print(get_common_all("Valdis", "Liga", "Maija", ['a', 'i', 'j'))
