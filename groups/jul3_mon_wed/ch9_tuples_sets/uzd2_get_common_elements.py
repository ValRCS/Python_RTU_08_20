# def get_common_elements(seq1,seq2,seq3):
#     # we are not sure if our sequences are sets or tuples or lists
#     # so we convert them to sets
#     # if they are sets already nothing will happen
#     common_elements = set(seq1) & set(seq2) & set(seq3)
#     return tuple(common_elements)
 
def get_common_elements(*args):
    # sanity check
    if len(args) == 0:
        return () # empty tuple
    result = None 

    for sequence in args: # we already used first element so we skip it
        # we could add a check if sequence is iterable (range, list, tuple, set, string)
        # how to check multiple types?
        if isinstance(sequence, (list, tuple, set, range, str)):
            if result is None:
                result = set(sequence)
            else:
                result = result & set(sequence)
        # else is not needed since we do nothing on non compatible types
    if result is None: # if all arguments were not iterable
        return () # another edge case
    return tuple(result)
 
my_list = ['a','b']
my_tuple = ('b','c')
my_string = "abc"
another_string ="abracadabra"
 
print(get_common_elements(my_list,my_tuple,my_string,another_string))
print(get_common_elements(my_list,my_tuple,my_string,another_string,"Valdis"))
print(get_common_elements())

res = get_common_elements((1,2,3,'a'), (5,'a',5,2,'z'), ('a','r','t',3,2))
print(res)

print(get_common_elements(777, "abba", 3,6,"Valdis", "abracadabra", None))
print(get_common_elements(777, 3,6, "abracadabra", None))