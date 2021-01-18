# # # # importing Python Modules and Packages
# # # # https://docs.python.org/3/tutorial/modules.html
# # # # https://realpython.com/python-modules-packages/
# # # # modular programming
# # # # way to divide and conqure larger tasks
# # # # code reusability


# # # # import my_lib
# import my_mod
# # import mat_lib
# # # # # if not found in current directly
# # # # # Python will look for my_mod.py in paths defined in PYTHONPATH enviroment variable
# # import sys

from my_mod import add # of course make sure there are no naming conflicts
from my_mod import txt # of course make sure there are no naming conflicts

import my_mod as my_big_mod # i can change module name
import my_mod as mm # more often popular libraries use abbreviations

from my_mod import add as big_add

print(add(56,66))
print(txt)
my_big_mod.add(333,11)
mm.add(14324,5)
big_add(62,44535)
# # # # # print("This could be a big program")
# # print(mat_lib.add(50,100))
# print(my_mod.add(4, 7))
# # # # my_mod.add(50, 87)
# print(my_mod.txt)
# print(my_mod.mlist)
# my_mod.mlist.append(55) # somebody else importing this will get a a new list

# print(my_mod.mlist)

# # new_obj = my_mod.Klase()
# # print(type(new_obj))
# # new_obj.new_prop = "Vertiba"
# # print(new_obj.new_prop)
# # garage_1 = my_mod.Garage()
# # garage_2 = my_mod.Garage('Lielaa')
# print(sys.path)
# # # # garage_3 = mlib_mod.Garage("Baismigā")
# # # # mlib_mod.mlist.append(9000)
# # # # print(mlib_mod.mlist)
