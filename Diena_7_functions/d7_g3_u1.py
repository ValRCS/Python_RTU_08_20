print("The Big Score program!")
print("Write a function:")
# def add_mult():
#     print(" add_mult")
# add_mult()
print("Write a function add_mult that requires 3 arguments:")
def add_mult(a,b,c):
    print(" a,b,c")
    print("Return the sum of the 2 smallest arguments multiplied by the largest argument value:")
    mlist = sorted([a,b,c])
    return (mlist[0]+mlist[1])*mlist[2]
result = add_mult(3,6,9)
print("The Big Score:",result)
result = add_mult(13,6,9)
print("The Big Score:",result)
result = add_mult(1,30,2)
print("The Big Score:",result)
