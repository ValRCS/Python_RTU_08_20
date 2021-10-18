def enter_num(num_1: int, num_2 : int, num_3: int) -> int:
    my_list = [num_1, num_2, num_3]
    sorted_list = sorted(my_list)
    result = (sorted_list[0] + sorted_list[1]) * sorted_list[2]
    return result
    
result = enter_num(2, 5, 6)
another_result = enter_num(20, 5, 6)
print(result, another_result)