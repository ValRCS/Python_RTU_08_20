# Pirmais uzdevums
 
# def add_mult(a,b,c):
#     my_list = sorted([a,b,c])
#     result = (my_list[0]+my_list[1])*my_list[-1]
#     print(f"Dotie: {a}, {b}, {c}")
#     print(f"Mazāko argumentu summas reizinājums ar lielāko vērtību:\n({my_list[0]}+{my_list[1]})*{my_list[-1]}={result}")
#     return result


def add_mult(*numbers):
    new_list = sorted(numbers)
    return (sum(new_list[:2])*new_list[-1])

print(add_mult(2,6,5))



# def add_mult(my_list):
#     # my_list.sort() # in place so original list is changed
#     new_list = sorted(my_list) # so I can return a new list so out of place
#     result = (new_list[0]+new_list[1])*new_list[2]
#     return result
    
# my_list=[2,6,5]
# print(add_mult(my_list))
# print(my_list)