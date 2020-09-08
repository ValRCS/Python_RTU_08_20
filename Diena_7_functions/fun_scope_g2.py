global_var = 500
global_list = [1, 2, 3]

# primitive get assigned a new id upon modification


def my_fun(arg_var):
    print("INSIDE my_fun", arg_var, id(arg_var))
    arg_var += 20
    print("After +=", arg_var, id(arg_var))
    return arg_var

# mutable data can be modified inside function and reference stays


def fun_list(arg_list):
    print(arg_list, id(arg_list))
    arg_list.append(30)
    print(arg_list, id(arg_list))
    return arg_list
    # if we do not write return we get None


print(global_list, id(global_list))
res_list = fun_list(global_list)
print(res_list, id(res_list))
print(global_list, id(global_list))
# print(global_var, id(global_var))
# my_result = my_fun(global_var)
# # arg_var is gone here
# print("Result", my_result, id(my_result))
# print("Global var", global_var, id(global_var))
