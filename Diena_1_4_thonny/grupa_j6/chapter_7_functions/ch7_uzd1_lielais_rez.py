#1. uzd
 
def add_mult(a, b, c):
    # my_list = [a, b, c]
    # my_list.sort() # in place sorting modifies the list

    sortedList = sorted([a, b, c]) # out of place sorting - returns a new list
 
    return (sortedList[0] + sortedList[1]) * sortedList[2]


# let's test it
assert add_mult(2, 3, 4) == 20
assert add_mult(2, 4, 3) == 20
assert add_mult(3, 2, 4) == 20
assert add_mult(3, 0, 2) == 6