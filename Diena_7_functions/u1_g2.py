def add_mult(a, b, c, debug=False):
    sorted_list = []
    sorted_list.append(a)
    sorted_list.append(b)
    sorted_list.append(c)
    sorted_list.sort()

    result = (sorted_list[0] + sorted_list[1]) * sorted_list[2]
    if debug:
        print(sorted_list)
        print(result)
    return result
 

result = add_mult(2,5,4)
print(result)
result = add_mult(2,5,4, debug=True)