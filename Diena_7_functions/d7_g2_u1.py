def add_mult(a,b,c):
    # ascending = list((a,b,c))
    ascending = [a,b,c] # also works
    ascending.sort()
    total = ascending[0]+ascending[1]
    multipl = total*ascending[-1]
    print(multipl)
def add_mult_unlimited(*args):
    # ascending = list((a,b,c))
    ascending = list(args) # also works
    ascending.sort()
    total = ascending[0]+ascending[1]
    multipl = total*ascending[-1]
    print(multipl)
add_mult(2,5,4)

add_mult_unlimited(1,4,6,234,6,3)