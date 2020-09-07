# def add_mult(a, b, c):
#     if b < a:
#         b, a = a, b
#     if c < a:
#         c, a = a, c
#     if c < b:
#         c, b = b, c
#     return((a+b)*c)


# print(add_mult(2, 5, 4))

def add_mult(a, b, c):
    mylist = [a, b, c]
    list1 = sorted(mylist)
    result = max(mylist) * (list1[0] + list1[1])
    # return print(result) # print returns None
    return result


my_result = add_mult(2, 5, 4)
print(my_result)
