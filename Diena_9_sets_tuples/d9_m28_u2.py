#2
def get_common_elements(seq1, seq2, seq3,):
    # inter=set(seq1).intersection(set(seq2)).intersection(set(seq3))
    inter=set(seq1) & set(seq2) & set(seq3)
    print(inter)
    return tuple(inter)

print(get_common_elements("abcde",['a','b','d'],('b','c','d','e')))

# 2. Kopējie Elementi
def get_common_elements_all(*sequences) -> tuple :
    # if len(sequence)==0:
    #     return ()
    # kopa = set(sequence[0])
    # for v in sequence[1:]:
    #     kopa = kopa & set(v)
    # return tuple(kopa)
    # return tuple(set.intersection(*map(set, sequence)))

    # result = set.intersection(*map(set, my_sequences)) # same as above in one line
    return tuple(set.intersection(*map(set, sequences)))

print(get_common_elements_all("abcde",['a','b','d'],('b','c','d','e','f')))
print(get_common_elements_all("abcde",['a','b','d'],('b','c','d','e','f'),"abracadabra"))


print([1,3,6,7,8], sep="__")
print(*[1,3,6,7,8], sep="__")
print(1,3,6,7,8, sep="__")
