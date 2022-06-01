# Task Nr. 2
 
# the hard way
def get_common_elements(seq1, seq2, seq3):
    elements = []
    # not very efficient on large sequences
    for i in seq1:
        if i in seq2 and i in seq3:
            elements.append(i)
    tuple_elements = tuple(elements)
    print(tuple_elements)
 
get_common_elements('abc', ['a','b'], ("b", "c"))


# 2 get common elements from sequences
def get_common_elements_unlimited(*args):
    # extra safety check for types
    for arg in args:
        if not isinstance(arg, (list, set, tuple, str)):
            return ()  # all arguments need to be iterable
    if args:
        # result = set(args[0])
        # for arg in args[1:]: # this loop will run only when we have two or more arguments
        #     result = set(arg) & result
        # return tuple(result)
        # same as the loop above
        return tuple(set.intersection(*map(set, args)))
    else:
        return ()

print(get_common_elements_unlimited('abc', ['a','b'], ("b", "c")))
print(get_common_elements_unlimited('abc', ['a','b'], ("b", "c"), "abracadabra","Valdis brauc"))
print(get_common_elements_unlimited([1,2,3,6],(5245325,2,4,6,2)))

# so i can use set.intersection on multiple sets at once
print(set.intersection({1,3,5,7},{1,2,3,4,5}, {3,1,6,2,2,3,3,6}))
 