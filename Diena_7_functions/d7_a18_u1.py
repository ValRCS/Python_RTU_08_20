def add_mult(a, b, c):
    my_list = [a, b, c]
    my_list.sort() # IN PLACE sort, modifies my_list
    result = (my_list[0] + my_list[1]) * my_list[2]
    print(f"({my_list[0]}+{my_list[1]})*{my_list[2]}={result}")
    return result
 
 
my_result = add_mult(2, 5, 4)
print(my_result)