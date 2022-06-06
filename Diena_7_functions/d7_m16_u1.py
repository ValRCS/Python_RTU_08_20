# 1.udevums
# def add_mult(a, b, c):
#     if a>b and a>c:
#         print("a>b and a>c")
#         result = (b+c)*a
#     elif b>a and b>c:
#         print("b>a and b>c")
#         result = (a+c)*b
#     else:
#         print("c>a and c>b")
#         result = (a+b)*c
#     return result

# modifies original list
def big_result(my_list: list[int]) -> int:
    my_list.sort() # this will sort the original list
    result=(my_list[0]+my_list[1])*my_list[2]
    return result

#1.uzdevums # will NOT modify original list
def add_mult(a,b,c):
    num_list = [a,b,c]
    new_list=sorted(num_list) # we create a new list, keeping original intact
    result=(new_list[0]+new_list[1])*new_list[2]
    return result

my_list= [2,5,4]  # this is a list of numbers
my_tuple = (2,5,4) # this is a tuple of numbers - fixed size
print(big_result(my_list = [10,5,6]))
print(big_result(my_list = my_list))


print(add_mult(2,5,4))