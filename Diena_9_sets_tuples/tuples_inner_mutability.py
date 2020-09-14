# mutating inside of tuples
# http://radar.oreilly.com/2014/10/python-tuples-immutable-but-potentially-changing.html

my_tuple = ("Valdis", "programmer", 45, 200, [1, 2, 3], {
            'food': 'potatoes', 'drink': 'milk'})
print(my_tuple)
# we can not change references to tuple object
# my_tuple[1] = "coding"
# my_tuple[4] = [1,2,3,5]
# my_tuple[5] = {'key':'value'}
my_tuple[4].append(55)
print(my_tuple)
my_tuple[4].clear()
print(my_tuple)
my_tuple[4].append(66)
print(my_tuple)
my_tuple[-1]['car'] = ['vw']
print(my_tuple)
print(my_tuple[-1]['drink'])
print(my_tuple[-1]['car'])
print(my_tuple[-1]['car'][0])
my_tuple[-1]['car'] = 'tesla'
print(my_tuple)
# to make life easier we could unpack
(name, job, _, _, my_list, my_dict) = my_tuple
my_list.append(777)
print(my_tuple)
my_tuple[4].append(555)
print(my_tuple)
print(my_list)
