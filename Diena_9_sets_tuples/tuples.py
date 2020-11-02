# # Python Tuples (a,b)
# # Immutable
# # Use - passing data that does not need changing
# # Faster than list
# # "safer" than list
# # Can be key in dict unlike list
# # For Heterogeneous data - meaning mixing different data types(int,str,list et al) inside
# # https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
# # https://realpython.com/python-lists-tuples/

my_tuple = ("Valdis", "programmer", 45, 200.8, [1, 2, 3], True, None, {'food':'potatoes', 'drink':'kefir'})
# print(my_tuple)
# print(type(my_tuple))
# print(my_tuple[0])
# print(len(my_tuple))
# print(my_tuple[-1]) 
# print(my_tuple[-1]['drink'])
# print(my_tuple[4][1])
# mykey = ("Valdis",180) # to use tuple as key tuple must only have immutables inside as well
# my_tuple[-1].setdefault(mykey, 500)
# my_tuple[-1][mykey] = 9000
# print(my_tuple[-1])
# print(my_tuple)
# print(my_tuple[-1].get(mykey))
# mini_3 = my_tuple[:3]
# print(mini_3, type(mini_3))
# # my_tuple[1] = "teacher" # will not work because tuples are immutable
# print(my_tuple[::2])
# print(my_tuple[::-1])
# print((4,5,"Valdis"))

# mult_tuple = tuple(el * 2 for el in mini_3)
# print(mult_tuple)
# int_tuple = tuple(el**2 for el in range(1,10)) # this is not but generator meaning it is made on demand not ready
# print(int_tuple)

# my_list = []
# # for el in mini_3:
# for el in my_tuple[:5]:
#     if type(el) == int or type(el) == float:
#         my_list.append(1/el)
#     else:
#         my_list.append(el[::-1])
# my_rev_tuple = tuple(my_list)
# print(my_rev_tuple)

# # print(my_tuple)
# # my_tuple[1] = "scientist"
# my_list = list(my_tuple)
# print(my_list)
# my_list[1] = "scientist"
# new_tuple = tuple(my_list)
# print(new_tuple)
# # t = ()  # empty tuple only question where would you use it?
# # print(t, type(t))
# # t = (1, 2, 55)  # 2 or more elements
# # print(t, type(t))
# # t = (5,)  # if you really need a tuple of one element
# print(my_tuple.count("programmer"))
# print(new_tuple.count("programmer"))
# print(new_tuple.index("scientist"))
# print(my_tuple.index(45))
# a = 10
# b = 20
# # print(a, b)
# # how to change them
# # temp = a
# # a = b
# # b = temp
# # print(a, b)
# # # in Python the above is simpler!
# print(a, b)
# a, b = b, a  # we can even change a,b,c,d = d,c,b,a and more
# print(a, b)
# (name, job, age, top_speed, favorite_list, _ , _ , favorite_dict) = my_tuple  # tuple unpacking
# print(name, job, age, top_speed, favorite_list)
# # name is my_tuple[0]
# # # tuple unpacking and using _ for values that we do need
# (name, job, _, top_speed, _) = my_tuple[:5]
# print(name, _)  # so _ will have value of last unpacking


def getMinMax(my_num_list):
    # so tuple will be created when returning multiple values
    return min(my_num_list), max(my_num_list)


res = getMinMax([3, 6, 1, 2])
print(res, type(res))
