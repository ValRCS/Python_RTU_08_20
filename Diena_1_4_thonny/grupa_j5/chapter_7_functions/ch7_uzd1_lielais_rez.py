# 1.uzd
def add_mult(a, b, c, debug=False):
    # assign incoming values to a list
    tlist = [a, b, c]
    tlist.sort() # in place sorting of the list
    if debug:
        print("Debugging", tlist)
    return (tlist[0] + tlist[1]) * tlist[2]

print(add_mult(2, 3, 4))
print(add_mult(2,5,4) )

# we could use assert to check if the function works as expected
assert add_mult(2, 3, 4, debug=True) == 20
assert add_mult(2, 5, 4, debug=True) == 30
assert add_mult(30,20,10,debug=True) == 900
# so assert will throw AssertionError if the condition is not met
# assert add_mult(2, 5, 4) == 36