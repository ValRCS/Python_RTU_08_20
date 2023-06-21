##############
# 2nd Task
##############

def get_common_elements(seq1, seq2, seq3):
    set1 = set(seq1)
    set2 = set(seq2)
    set3 = set(seq3)
    common = set1.intersection(set2, set3)

    return tuple(common)

print(get_common_elements("abcf",['a','b', 'f'],('b','c', 'f')))

# how about getting commone elements from unlimited number of sequences?
# we can use *args to get unlimited number of arguments

def get_common_elements_unlimited(*args) -> tuple:
    '''Returns tuple of common elements 
    from unlimited number of sequences'''
    if len(args) < 1: # sanity check - early exit
        return tuple() # empty tuple
    
    common = set(args[0]) # careful not to start with empty set ! then intersection will always be empty!
    for seq in args[1:]: # this loop will not run if only 1 argument is passed
        common = common.intersection(set(seq))
    # there is also a one liner for this
    # common = set.intersection(*map(set, args)) - this uses map() function to convert all args to sets
    # then uses * to unpack them as arguments to intersection() function
    return tuple(common)

# let's test it

print(get_common_elements_unlimited("abcf",['a','b', 'f'],('b','c', 'f')))
print(get_common_elements_unlimited("abcf",['a','b', 'f'],('b','c', 'f'), "abcfdfadfa"))
print(get_common_elements_unlimited("abcf",['a','b', 'f'],('b','c', 'f'), "abcfdfadfa"))
print(get_common_elements_unlimited("abcf",['a','b', 'f'],('b','c', 'f'), "abcfdfadfa", "fudge"))