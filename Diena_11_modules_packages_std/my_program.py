# importing Python Modules and Packages
# https://docs.python.org/3/tutorial/modules.html
# https://realpython.com/python-modules-packages/
# modular programming
# way to divide and conqure larger tasks
# code reusability


import my_mod
# if not found in current directly
# Python will look for my_mod.py in paths defined in PYTHONPATH enviroment variable
# import sys
# print(sys.path)


print("This could be a big program")

print(my_mod.add(4, 7))
my_mod.add(50, 87)
print(my_mod.txt)
print(my_mod.mlist)
my_mod.mlist.append(55)
print(my_mod.mlist)

new_obj = my_mod.Klase()
print(type(new_obj))
new_obj.new_prop = "Vertiba"
print(new_obj.new_prop)
garage_1 = my_mod.Garage()
garage_2 = my_mod.Garage('Lielaa')
