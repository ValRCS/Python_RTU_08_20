# # # # # # Python Tuples (a,b)
# # # # # # Immutable
# # # # # # Use - passing data that does not need changing
# # # # # # Faster than list
# # # # # # "safer" than list
# # # # # # Can be key in dict unlike list
# # # # # # For Heterogeneous data - meaning mixing different data types(int,str,list et al) inside
# # # # # # https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
# # # # # # https://realpython.com/python-lists-tuples/

my_tuple = ("Valdis", "programmer", 45, 200.8, 
        [10, 20, 30], True, None, 
        ('also_tuple', 5, True), {'food':'potatoes', 'drink':'kefir'})
print(my_tuple)
another_tuple = tuple([1, "Valdis", True]) # i need to pass an iterable to tuple constructor
print(another_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(len(my_tuple))
print(my_tuple[-1]) # here also print(my_tuple[7]) would since we have 8 elements starting 0
print(my_tuple[8]['drink'], my_tuple[-1]['drink'], my_tuple[-1].get('drink')) # get also would work
print(my_tuple[4]) # list assuming I know the 5th element is list
print(my_tuple[4][1]) # 2nd item in list
print(my_tuple[7][1], my_tuple[-2][-2], my_tuple[-2][1]) # all 5s from innner tuple data structure

mykey = "Valdis", 180 # i can make tuple without parenthesis when there is no confusion
print(mykey)
print(type(mykey))
# # # # # to use tuple as key tuple must only have immutables inside as well
newdict = {mykey:9000, "secondkey":9050}
print(newdict)
print(newdict[mykey])
print(newdict[("Valdis", 180)]) # here you will need regular parenthesis to create tuple


# # my_tuple.
# my_tuple[0] = "Visvaldis" # error since tuple does not support item assignment

# # # # # # tuples are immutable but you can mutate those data structures inside which are mutable
my_tuple[-1].setdefault(mykey, 500) # so dict is mutable we can perform in place methods
print(my_tuple)
my_tuple[-1][mykey] = 9000
print(my_tuple)

# # += for lists is same as mylist = mylist + [1,2,3]
# my_tuple[4] += [1,2,3] # i can not write a new list in place of old list, OUT OF PLACE will not work
print(my_tuple[4])
my_tuple[4].extend([1,2,3]) # BUT i can can mutate the old list IN PLACE
print(my_tuple)
my_tuple[4].append(50)
print(my_tuple)
my_pop = my_tuple[4].pop()
my_tuple[4].append(5000) # BUT i can can mutate the old list
print(my_tuple)
my_tuple[4].sort() # .sort() is IN PLACE
print(my_tuple)
# # # # # # print(my_tuple[-1])
# # # # # # print(my_tuple)
# # # print(my_tuple[-1].get(mykey))

# # # # # regular slicing works
# mini_3 = my_tuple[:3] # i can extract sub tuple
mini_3 = my_tuple[:3] + my_tuple[1:4] # i can extract sub tuple
print(mini_3, type(mini_3))
# # my_tuple[1] = "teacher" # will not work because tuples are immutable
new_tuple = my_tuple[:1] + ("teacher",) + my_tuple[2:] # we could slice it together
print(new_tuple)
my_list = list(my_tuple) # i can cast tuple to list
my_list[1] = "teacher"
print(my_list)
print(my_tuple)
my_tuple = tuple(my_list) # i can overwrite reference to old tuple with reference to new tuple
print(my_tuple)

print(my_tuple[::2]) # new tuuple of every 2nd value
print(my_tuple[::-1])
print(4,5,"Valdis") # just some values no tuple
print((4,5,"Valdis")) # so i create tuple on the fly - hot tuple

# # # # do we have tuple comprehensions?
# # # # not quite but we can use generator expression then cast to tuple
mult_tuple = tuple(el * 2 for el in my_tuple[:6]) # should be faster than list comprehension
print(mult_tuple)
int_tuple = tuple(el**2 for el in range(1,10)) # this is not tuple but generator meaning it is made on demand not ready
print(int_tuple)

my_list = []
# for el in mini_3:
for el in my_tuple[:5]:
    if type(el) is int or type(el) is float:
        my_list.append(1/el) # could also check for zero
    else: #list or string or something else even
        my_list.append(el[::-1]) # might want to check also Booleans and None types and dictionaries
my_rev_tuple = tuple(my_list)
print(my_rev_tuple)

# # # # # # # print(my_tuple)
# # # # # # # my_tuple[1] = "scientist"
# # # # # # my_list = list(my_tuple)
# # # # # # print(my_list)
# # # # # # my_list[1] = "scientist"
# # # # # # new_tuple = tuple(my_list)
# # # # # # print(new_tuple)


t = ()  # empty tuple only question where would you use it? One use to functions which need some sequence
print(t, type(t))
t = (1, 2, 55)  # 2 or more elements
print(t, type(t))
t = (5,)  # if you really need a tuple of one element
print(t, type(t))
# # # # # my_tuple. # i can use . for Intellisense to suggest methods, we only have 2
print(my_tuple.count("programmer"))
# # # # my_tuple.
print(my_tuple.count("teacher"))
print(my_tuple.index("teacher"))
print(my_tuple.index("Valdis"))
print(my_tuple.index(45))
if "programmer" in my_tuple:
    print(my_tuple.index("programmer"))
else:
    print("Not found the key")
# # # # # # # print(my_tuple.index("notprogrammer"))
# # # # # print("somevalue" in my_tuple)

# # # # # # print(new_tuple.count("programmer"))
# # # # # # print(new_tuple.index("scientist"))
# # # # # # print(my_tuple.index(45))

# # # # # Trick on swapping values
a = 10
b = 20
print(a, b)
# how to change them
temp = a
a = b
b = temp
print(a, b)
# # # # # # # # in Python the above is simpler!
print(a, b)
a, b = b, a  # we can even change a,b,c,d = d,c,b,a and more, so creating tuple on the right and unpack it on the left
print(a, b)

a, b, c = 5, 10, "Booo" # example of tuple packing and unpacking
print(a,b,c)
my_num_tuple = 5, 6, 8
print(my_num_tuple, type(my_num_tuple))
my_num_tuple = (5, 6, 8)
print(my_num_tuple, type(my_num_tuple))

# print(my_tuple)
# print(len(my_tuple))
name, job, age, top_speed, favorite_list, _ , _ , _, favorite_dict = my_tuple  # tuple unpacking
# # _ symbolizes variables we do not care about
print(name, job, age, top_speed, favorite_list, favorite_dict)

# # extended unpacking
head, second, *rest, tail = my_tuple # names you pick yourself *rest will be a list
print(head, second, rest, tail, sep="\n")

# # # # # # name is my_tuple[0]
# # # # # # tuple unpacking and using _ for values that we do need
# # # name, job, _, top_speed, _ = my_tuple[:5]
# # # print(name, _)  # so _ will have value of last unpacking
# # # # (name, job, _, top_speed) = my_tuple[:4]
# # # # print(name, _)  # so _ will have value of last unpacking


def getMinMax(my_num_list):
    # so tuple will be created when returning multiple values
    return min(my_num_list), max(my_num_list)


res = getMinMax([3, 6, 1, 2])
print(res, type(res))

# # # i could also unpack immediately the result from tuple into individual values
my_min, my_max = getMinMax([3, 6, 1, 2])
print(my_min,my_max)

# # list of tuples can be converted into a dictionary
my_tup_list =[("mykey","Myval"),("anoteherkey",50)] # list of inner lists len 2 would also work
my_new_dict = dict(my_tup_list)
print(my_tup_list)
print(my_new_dict)

# regular tuples can be hard to use since you need to know what index the item is at
# improvement to regular tuples is namedtuples
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# named tuples give us another access to members using . notation

print(type(my_tuple[0]) in (list, tuple))
print(type(my_tuple[0]) in (list, tuple, str))

