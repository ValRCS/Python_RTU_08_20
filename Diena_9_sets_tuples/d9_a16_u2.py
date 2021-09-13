def get_common_elements(seq1, seq2, seq3):
    # result = set.intersection(*[set(list) for list in p])
    s1 = set(seq1)
    s2 = set(seq2)
    s3 = set(seq3)
 
    return tuple(s1 & s2 & s3)

print(get_common_elements("abc", ["a", "b"], ("b", "c")))
print(get_common_elements("abcd", ["a", "b","d"], ("b", "c", "d", "e")))

# 2b. Uzdevums:
 
def get_common_elements(*my_sequences):
    my_sets = [set(seq) for seq in my_sequences]
    # result = my_sets[0] # we need something, can't start with empty
    # for my_set in my_sets[1:]:
    #     result = result & my_set
    result = set.intersection(*my_sets)
    # result = set.intersection(*map(set, my_sequences)) # same as above in one line
    return tuple(result)
 
print(get_common_elements("ab8c", ["a", "b", "8"], ("b", "8", "c"), ["8", "c"]))