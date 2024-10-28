# Kopas 2.uzdevums

def get_common_elements(seq1, seq2, seq3):
    common_elements = set(seq1) & set(seq2) & set(seq3)
    return tuple(common_elements)


print(get_common_elements("abc", ["a", "b"], ("b", "c", "Valdis", 5)))


# let's write it to accept unlimited number of sequences
def get_common_elements_unlimited(*sequences):
    # check first if we have any sequences
    if not sequences:
        return () # early exit when no sequences
    common_elements = set(sequences[0]) # we know we have at least one sequence
    for seq in sequences[1:]:
        common_elements &= set(seq) # same as common_elements = common_elements & set(seq)
    return tuple(common_elements)

# let's test with 3 sequences
print(get_common_elements_unlimited("abc", ["a", "b"], ("b", "c", "Valdis", 5)))

# let's test with 4 sequences
print(get_common_elements_unlimited("abc", ["a", "b"], ("b", "c", "Valdis", 5), "badāc"))
# will work with 2 sequences
print(get_common_elements_unlimited("abc", ["a", "b","D"]))

# one is fine too
print(get_common_elements_unlimited("abra"))