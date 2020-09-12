# Python Tuples (a,b)
# Immutable
# Use - passing data that does not need changing
# Faster than list
# "safer" than list
# Can be key in dict unlike list
# For Heterogeneous data - meaning mixing different data types(int,str,list et al) inside
# https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
# https://realpython.com/python-lists-tuples/

my_tuple = ("Valdis", "programmer", 45, 200, [1, 2, 3])
print(my_tuple)
type(my_tuple)
print(my_tuple[0])
len(my_tuple)
my_tuple[-1]
my_tuple[:3]
my_tuple[::2]
my_tuple[::-1]
my_tuple[1] = "scientist"
my_list = list(my_tuple)
print(my_list)
my_list[1] = "scientist"
new_tuple = tuple(my_list)
print(new_tuple)
t = ()  # empty tuple only question where would you use it?
print(t, type(t))
t = (1, 2)  # 2 or more elements
print(t, type(t))
t = (5,)  # if you really need a tuple of one element
my_tuple.count("programmer")
my_tuple.index(45)
a = 10
b = 20
print(a, b)
# how to change them
temp = a
a = b
b = temp
print(a, b)
# in Python the above is simpler!
print(a, b)
a, b = b, a  # we can even change a,b,c,d = d,c,b,a and more
print(a, b)
(name, job, age, top_speed, favorite_list) = my_list  # tuple unpacking
print(name, job, age, top_speed, favorite_list)
# tuple unpacking and using _ for values that we do need
(name, job, _, top_speed, _) = my_list
print(name, _)  # so _ will have value of last unpacking


def getMinMax(my_num_list):
    # so tuple will be created when returning multiple values
    return min(my_num_list), max(my_num_list)


res = getMinMax([3, 6, 1, 2])
print(res, type(res))
