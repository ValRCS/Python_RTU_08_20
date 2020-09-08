def add_multi(a, b, c):
    myList = [a, b, c]
    myList.sort()
    num1 = myList[0]
    num2 = myList[1]
    num3 = myList[2]
    return (num1+num2)*num3


def add_any(*args):
    my_list = list(args)
    my_list.sort()  # this sorts my_list in place
    n1 = my_list[0]
    n2 = my_list[1]
    n3 = my_list[-1]
    return (n1+n2)*n3


print(add_any(2, 5))
print(add_any(4, 10, 5))
print(add_any(4, 10, 5, 100, 2, 1))

# print(add_multi(4, 10, 5))
# print(add_multi(14, 10, 5))
# print(add_multi(2, 10, 5))
# print(add_multi(4, 10, 5))
# print(add_multi(4, 10, 25))
# print(add_multi(4, 210, 5))
