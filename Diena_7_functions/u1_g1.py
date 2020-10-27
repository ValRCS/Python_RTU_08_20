def add_mult(*args):
    my_list = sorted(args)
    return (my_list[0]+my_list[1])*my_list[-1]

print(add_mult(1,6,3))
print(add_mult(1,6,3))
print(add_mult(1,6,-5,-2,3,100,2,4))

def add_mult2(arg_list):
    my_list = sorted(arg_list)
    return (my_list[0]+my_list[1])*my_list[-1]

print(add_mult2([1,6,-5,-2,3,100,2,4]))

# def add_mult(a,b,c):
#     num_list = sorted([a,b,c])
#     return (num_list[0]+num_list[1])*num_list[2]
 
# x = int(input("Input first number: "))
# y = int(input("Input second number: "))
# z = int(input("Input third number: "))
 
# print(add_mult(x,y,z))