# # # # # # # # # # # # # Python Tuples (a,b) - korteža latviski
# # # # # # # # # # # # # Immutable
# # # # # # # # # # # # # Use - passing data that does not need changing
# # # # # # # # # # # # # Faster than list
# # # # # # # # # # # # # "safer" than list
# # # # # # # # # # # # # Can be key in dict unlike list
# # # # # # # # # # # # # For Heterogeneous data - meaning mixing different data types(int,str,list et al) inside
# # # # # # # # # # # # # https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
# # # # # # # # # # # # # https://realpython.com/python-lists-tuples/

my_tuple = ("Valdis", "programmer", 45, 200.8, 
        [10, 20, 30], True, None, 
        ('also_tuple', 5, True), {'food':'potatoes', 'drink':'kefir'})
print(my_tuple)
print(type(my_tuple))
another_tuple = tuple([1, "Valdis", True]) # i need to pass an iterable to tuple constructor
print(another_tuple)
# print(type(my_tuple))
tuple_from_string = tuple("Valdis")  # i can create a tuple from a string as well
print(tuple_from_string)

# # # # # normal slicing methods will work
print(my_tuple[0])
print(len(my_tuple))
print(my_tuple[-1]) # reverse syntax also works

# # # membership testing
print(45 in my_tuple)
print(46 in my_tuple)
print("Valdis" in my_tuple)
print("al" in my_tuple) # false because we need exact match

# only two methods for tuple index AND count
print(my_tuple.index(45)) # 2 because index starts from 0, so 3rd element
print(my_tuple.count("Valdis"))

# # my_tuple.  # only two methods are available for tuples
# # my_list = [1,2,3,4,5,6,7,8,9,10]
# # my_list. # my list has many methods that can be used on tuples

# # # # # # tuple itself is fixed , immutable meaning we can not change objects inside
# my_tuple[1] = "teacher" # raises TypeError: 'tuple' object does not support item assignment
print(my_tuple[:1])
print(my_tuple[1])  # current 2nd element
print(("teacher",))  #this is a single element tuple
print(my_tuple[2:])  # rest of tuple starting with 3rd element
# # # so I overwrite the whole tuple with new tuple
my_tuple = my_tuple[:1] + ("teacher",) + my_tuple[2:] # this will insert a new element in the tuple
print(my_tuple)
# # # # # # HOWEVER
# # # # # # we can use IN PLACE methods on mutable objects inside the tuple
print(my_tuple[-1]) # here also print(my_tuple[7]) would since we have 8 elements starting 0
print(my_tuple[8]['drink'], my_tuple[-1]['drink'], my_tuple[-1].get('drink')) # get also would work
my_tuple[-1]['drink'] = 'water'
my_tuple[-1]['car'] = 'BMW'  # i can mutate the dictionary inside the tuple
# # # # why? because dictionary is mutable
print(my_tuple)

print(my_tuple[4]) # list assuming I know the 5th element is list
print(my_tuple[4][1]) # 2nd item in list
print(my_tuple[7][1], my_tuple[-2][-2], my_tuple[-2][1]) # all 5s from innner tuple data structure

my_tuple[-1]["dessert"] = "ice cream" # so i can add new keys to my dictionary
print(my_tuple)
my_tuple[4].append(9000) # 5th element in my tuple is a list so we can use IN PLACE methods
print(my_tuple)
my_tuple[4].extend([8300, 4000]) # extend is a list method IN PLACE
print(my_tuple)
my_tuple[4].insert(3, -1) # insert is a list method IN PLACE
print(my_tuple)
my_tuple[4].remove(8300) # remove is a list method IN PLACE
print(my_tuple)
my_tuple[4].sort() # sort is a list method IN PLACE
print(my_tuple)
# # # OUT OF PLACE will give TypeError: 'tuple' object does not support item assignment
# my_tuple[4] = sorted(my_tuple[4]) # can not use OUT OF PLACE METHODS

# # # # i can use hashable tuple as a key for dictionary
mykey = "Valdis", 180 # i can make tuple without parenthesis when there is no confusion
print(mykey)
print(type(mykey))
# # # # # # # # # # # # to use tuple as key tuple must only have immutables inside as well
newdict = {mykey:9000, "secondkey":9050}
print(newdict)
# another_key = "Valdis", 200
# # newdict[another_key] = 9001
# # print(newdict)
# # print(newdict[mykey])
print(newdict[("Valdis", 180)]) # here you will need regular parenthesis to create tuple
print(newdict["Valdis", 180]) # here you will need regular parenthesis to create tuple
# # # not all tuples can be used as keys
# # # newdict[my_tuple] = "no way Jose" # this tuple will not work since it is not hashable

# # # # # # slicing works(makes a new tuple)
print(my_tuple[::-1])
reversed_tuple = my_tuple[::-1]
print(reversed_tuple)

# # # # # print(my_tuple.count(45)) # should be 1 in my tuple
# # # # # print(my_tuple.index(45))  # so returns 2 - as it is 3rd element

# # # # # # # my_tuple[0] = "Visvaldis" # error since tuple does not support item assignment

# # # # # # # # # # # # # tuples are immutable but you can mutate those data structures inside which are mutable
# # # my_tuple[-1].setdefault(mykey, 500) # so dict is mutable we can perform in place methods
# # # print(my_tuple)
# # # # # # my_tuple[-1][mykey] = 9000
# # # # # # print(my_tuple)

# # # # # # # # # += for lists is same as mylist = mylist + [1,2,3]
# # # # my_tuple[4] += [1,2,3] # i can not write a new list in place of old list, OUT OF PLACE will not work
# # # print(my_tuple[4])
# # # my_tuple[4].extend([1,2,3]) # BUT i can can mutate the old list IN PLACE
# # # print(my_tuple)
# # # my_tuple[4].clear() # clear is a list method IN PLACE
# # # print(my_tuple)

# # # # # # my_tuple[4].append(50)
# # # # # # print(my_tuple)
# # # # # # my_pop = my_tuple[4].pop()
# # # # # # my_tuple[4].append(5000) # BUT i can can mutate the old list
# # # # # # print(my_tuple)
# # # # # my_tuple[4].sort() # .sort() is IN PLACE
# # print(my_tuple)
# # my_tuple[4].clear()  # again IN PLACE clear
# # print(my_tuple)
# # my_tuple[4].append("Booooo")
# # my_tuple[4].append("Dooo")
# # print(my_tuple)

# # # # # # # # # # # # # print(my_tuple[-1])
# # # # # # # # # # # # # print(my_tuple)
# # # # # # # # # # print(my_tuple[-1].get(mykey))

# # # # # # # # # # # # regular slicing works
# mini_3 = my_tuple[:3] # i can extract sub tuple
# print(mini_3)
# mini_slice = my_tuple[:3] + my_tuple[1:4] # i can extract sub tuple
# print(mini_slice, type(mini_slice))
# # # # # # # my_tuple[1] = "teacher" # will not work because tuples are immutable
# # # # # # # so one element tuple is written as follows ("teacher",)
# # # # # new_tuple = my_tuple[:1] + ("teacher",) + my_tuple[2:] # we could slice it together ("teacher",) - single element tuple
# # # # # print(new_tuple)
# my_list = list(my_tuple) # i can cast tuple to list
# my_list[1] = "teacher"
# print(my_list)
# print(my_tuple)
# my_tuple = tuple(my_list) # i can overwrite reference to old tuple with reference to new tuple
# print(my_tuple)

# print(my_tuple[::2]) # new tuuple of every 2nd value
# # # # # # # print(my_tuple[::-1])
# # # # # # print(4,5,"Valdis") # just some values no tuple
# # # # # # print((4,5,"Valdis")) # so i create tuple on the fly - hot tuple

# # # # looping through tuple
for el in my_tuple:  # el is a variable that will be used in the loop, could be named anything
    print(type(el), el)

# # # # # # # # # # # do we have tuple comprehensions?
# # # # # # # # # # # not quite but we can use generator expression then cast to tuple
my_generator = (el * 2 for el in my_tuple[:6]) # generator expression
print(my_generator) # lazy gives values only when needed
for el in my_generator: # will save memory and should be faster than going through list
    print(el)
# mult_tuple = tuple(el * 2 for el in my_tuple[:6]) # should be faster than list comprehension
# print(mult_tuple)
# int_tuple = tuple(el**2 for el in range(1,10)) # this is not tuple but generator meaning it is made on demand not ready
# print(int_tuple)

# # # # # # # my_list = []
# # # # # # # # for el in mini_3:
# # # # # # # for el in my_tuple[:5]:
# # # # # # #     if type(el) is int or type(el) is float:
# # # # # # #         my_list.append(1/el) # could also check for zero
# # # # # # #     else: #list or string or something else even
# # # # # # #         my_list.append(el[::-1]) # might want to check also Booleans and None types and dictionaries
# # # # # # # my_rev_tuple = tuple(my_list)
# # # # # # # print(my_rev_tuple)

# # # # # # # # # # # # # # print(my_tuple)
# # # # # # # # # # # # # # my_tuple[1] = "scientist"
# # # # # # # # # # # # # my_list = list(my_tuple)
# # # # # # # # # # # # # print(my_list)
# # # # # # # # # # # # # my_list[1] = "scientist"
# # # # # # # # # # # # # new_tuple = tuple(my_list)
# # # # # # # # # # # # # print(new_tuple)


t = ()  # empty tuple only question where would you use it? One use to functions which need some sequence
print(t, type(t))
t = (1, 2, 55)  # 2 or more elements, parenthesis are optional
print(t, type(t))
t = 5,  # if you really need a tuple of one element, parenthesis and comma are required
print(t, type(t))
# # # # # # # # # # # # my_tuple. # i can use . for Intellisense to suggest methods, we only have 2
# # # # print(my_tuple.count("programmer"))
# # # # # # # # # # # my_tuple.
# # # # print(my_tuple.count("teacher"))
# # # # print(my_tuple.index("teacher"))
# # # # # # # print(my_tuple.index("Valdis"))
# # # # # # # print(my_tuple.index(45))
# # # # # # # if "programmer" in my_tuple:
# # # # # # #     print(my_tuple.index("programmer"))
# # # # # # # else:
# # # # # # #     print("Not found the key")
# # # # # # # # # # # # # # print(my_tuple.index("notprogrammer"))
# # # # # # # # # # # # print("somevalue" in my_tuple)

# # # # # # # # # # # # # print(new_tuple.count("programmer"))
# # # # # # # # # # # # # print(new_tuple.index("scientist"))
# # # # # # # # # # # # # print(my_tuple.index(45))

# # # # # # # # # # # # Trick on swapping values
a = 10
b = 20
print(a, b)
# # # # how to change them?
# classical solution - use a temporary variable
temp = a
a = b
b = temp
print(a, b)
# # # # # # # # # # # # # # # in Python the above is simpler!
print(a, b)
# # # tuple unpacking
# # # right side is evaluated first
a, b = b, a  # we can even change a,b,c,d = d,c,b,a and more, so creating tuple on the right and unpack it on the left
print(a, b)
# # # # # (a, b) = (b, a) # so parenthesis are not needed here
# # # # # print(a,b)

# # tuple packing
a_b_tuple = a, b, 5000, "Valdis"  # we can create tuple on the fly
print(a_b_tuple)



# # k, v = "a", 2  # tuple unpacking
# # print(k,v)
# # k, v = ("a", 2), 'myVal'  # tuple unpacking
# # print(k,v)
# a, b, c = 5, 10, "Booo" # example of tuple packing and unpacking
# print(a,b,c)
# # # # # my_num_tuple = 5, 6, 8
# # # # # print(my_num_tuple, type(my_num_tuple))
# # # # # # # my_num_tuple = (5, 6, 8)
# # # # # # # print(my_num_tuple, type(my_num_tuple))

# # # print(my_tuple)
# # # print(len(my_tuple))

# # # # # # # full unpacking
name, job, age, top_speed, favorite_list, my_bool , my_none, my_tup, favorite_dict = my_tuple
print(name, job, age, top_speed, favorite_list, favorite_dict)
name, job, age, top_speed, favorite_list, _ , _ , _,  favorite_dict = my_tuple  # tuple unpacking
# # _ symbolizes variables we do not care about
print(name, job, age, top_speed, favorite_list, favorite_dict)

# # # # # # # # extended unpacking
head, second, *rest_as_list, tail = my_tuple # names you pick yourself *rest_as_list will be a list
print(head, second, rest_as_list, tail, sep="\n")

# # # # # # # # # # # # # name is my_tuple[0]
# # # # # # # # # # # # # tuple unpacking and using _ for values that we do need
# # # # # # # # # # name, job, _, top_speed, _ = my_tuple[:5]
# # # # # # # # # # print(name, _)  # so _ will have value of last unpacking
# # # # # # # # # # # (name, job, _, top_speed) = my_tuple[:4]
# # # # # # # # # # # print(name, _)  # so _ will have value of last unpacking


def getMinMax(my_num_list):
    # so tuple will be created when returning multiple values
    return min(my_num_list), max(my_num_list)  # return multiple values as tuple


res = getMinMax([3, 6, 1, 2])
print(res, type(res))

# # # # # # # # # # i could also unpack immediately the result from tuple into individual values
my_min, my_max = getMinMax([3, 6, 1, 2])
print(my_min,my_max)

# # # # # # # # # list of tuples can be converted into a dictionary
my_tup_list =[("mykey","Myval"),("anoteherkey",50),("alsokey",-343)] # list of inner lists len 2 would also work
my_new_dict = dict(my_tup_list) # requirement is to have a list of tuple pairs
print(my_tup_list)
print(my_new_dict)
# my_items = list(my_new_dict.items())
# print(my_items)

# # # # # # # # regular tuples can be hard to use since you need to know what index the item is at
# # # # # # # # improvement to regular tuples is namedtuples
# # # # # # # # https://docs.python.org/3/library/collections.html#collections.namedtuple
# # # # # # # # named tuples give us another access to members using . notation

# # # # # # # print(type(my_tuple[0]) in (list, tuple))
# # # # # # # print(type(my_tuple[0]) in (list, tuple, str))

# # # for t in enumerate(range(10,20)):
# # #     print(t, t[0], t[1])

# # # for i, n in enumerate(range(10,20)):
# # #     print(i, "and", n)