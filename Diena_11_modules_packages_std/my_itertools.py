from itertools import product

clist = list("kartupelis")
nlist = list(range(5))

cartesian_prod = product(clist, nlist)
print(cartesian_prod)
cartesian_list = list(cartesian_prod)
print(cartesian_list)

big_cart = list(product("abc", [1,2], (True, False)))
print(big_cart)