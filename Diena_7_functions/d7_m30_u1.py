# Ex 1
def add_mult(a, b, c):
    my_list = [a,b,c]
    my_list.sort()
    result = (my_list[0]+my_list[1])*my_list[2]
    print(f"({my_list[0]}+{my_list[1]})*{my_list[2]} = {result}")
    return result

saved_result = add_mult(2, 5, 4)
print(saved_result)