# https://effbot.org/zone/call-by-object.htm
# http://foobarnbaz.com/2012/07/08/understanding-python-variables/
# https://realpython.com/python-pass-by-reference/

# Variable Scope
# Python Call by Object (reference)

glob_var = 5
print(glob_var, id(glob_var))


def do_stuff(arg_var, arg_str="some text", arg_list=None):
    print(arg_var, id(arg_var))
    # typically we do not want to deal with globals! avoid
    print(glob_var, id(glob_var))
    arg_var = 10  # glob_var does not change
    print("Local in fun", arg_var, id(arg_var))
    print("Global variable", glob_var, id(glob_var))
    return arg_var


def fun_string(arg_str):  # remember strings are immutable
    print("Before MOD", arg_str, id(arg_str))
    arg_str += "new string!"
    print("After changing", arg_str, id(arg_str))
    return arg_str


# https://stackoverflow.com/questions/2347265/why-does-behave-unexpectedly-on-lists
def fun_list(arg_list):  # lists are mutable
    print("BEFORE mod", arg_list, id(arg_list))
    arg_list.append(4)  # this happens in-place to the same object!!
    print("AFTER In PLACE mod", arg_list, id(arg_list))
    arg_list += [5]  # still in place modification it turns out!!
    print("AFTER IN PLACE mod !! += mod", arg_list, id(arg_list))
    # turns out += for lists is actually extend method which is in place!!
    arg_list = arg_list + [6]  # as expected out of place
    print("AFTER OUT OF PLACE = mod", arg_list, id(arg_list))
    return arg_list


result = do_stuff(glob_var)
# print("Local in fun", arg_var, id(arg_var))  # there will be dragons!
print(result, id(result))

food = "kartupelis"
str_result = fun_string(food)
print(food, id(food))
print(str_result, id(str_result))

glob_list = [1, 2, 3]
print(glob_list, id(glob_list))
list_result = fun_list(glob_list)
print(list_result, id(list_result))
print(glob_list is list_result)
print(id(glob_list), id(list_result))
