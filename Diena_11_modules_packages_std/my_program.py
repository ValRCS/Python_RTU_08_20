# # # # # # # importing Python Modules and Packages
# # # # # # # https://docs.python.org/3/tutorial/modules.html
# # # # # # # https://realpython.com/python-modules-packages/
# # # # # # # modular programming
# # # # # # # way to divide and conqure larger tasks
# # # # # # # code reusability
# # # # simplicity - subset of the problem
# # # # maintanibility - different domains different libraries
# # # # namespaces - avoid naming conflicts/colusions

# # # # # # # # if not found in current directly
# # # # # # # # Python will look for my_mod.py in paths defined in PYTHONPATH enviroment variable
# # usually we import standard libary first
import sys # sys is standard library package, for functionality dealing with system function
print(sys.path)

# import my_mod

# my_mod.add(45,23)
# new_garage = my_mod.Garage()
# print(my_mod.mlist)

# import my_mod as mm # rename module basically
# mm.add(3,65)
# print(mm.mlist)

# if I am sure that there are no naming conflicts
from my_mod import add # just one function, make sure no name conflicts
add(5,67)

# from my_mod import add as super_add # import just one function with new name
# super_add(62,66)

# TIP: do not name your files the same name as standard library imports 

# # # import my_lib will not do much
# # from my_lib import my_mod
from my_lib import my_tools # so just llike import my_tools but from subfolder
my_tools.tool_fun("Is this an argument?")
from my_lib import my_tools as myt # so just llike import my_tools but from subfolder
myt.tool_fun("OHO")
from my_lib.my_tools import tool_fun # so just one function from  my_tools file in my_lib folder
tool_fun("This should also work")
from my_lib.my_tools import tool_fun as tf #importing one function and renaming
tf("This should also work")

from pkg.subp import sub_utils # so sub_utils.py is two folders deep pkg/subp/sub_utils.py
print(sub_utils.MAGIC_PI)

from pkg.subp.sub_utils import subadd # so function subadd from 
subadd(60,22)

# new_garage = my_mod.Garage()
# print(my_mod.mlist)
# # from my_lib.my_mod import add
# # add(33,666)
# from my_mod import Garage # so i can import just specific class, value, function etc
# # just careful with name collision, no protection
# # avoid from my_mod import * # this is bad practice
# also_garage = Garage()

# # if I do not like module name I can change it
# import my_mod as mm # very common to use short names
# mm.add(5,16)

# from my_mod import Garage as GG
# another_garage = GG()

# # long way for specific tool
# import my_lib.my_tools
# my_lib.my_tools.tool_fun("AHa!")

# import my_lib.my_tools as mt 
# mt.tool_fun("oho")

# import my_lib

# my_lib.my_tools.tool_fun("oh")
# print(mt.complex_fun(5, 10))

# from my_lib.my_tools import complex_fun as cfun
# print(cfun(6,100))



# # import my_mod
# # # # # import mat_lib


# # from my_mod import add # of course make sure there are no naming conflicts
# # from my_mod import txt # of course make sure there are no naming conflicts

# # # system_sorted = sorted # it is possible to save system function before rewriting the reference
# # # from my_mod import sorted # it is possible but not advisable

# # # import my_mod as my_big_mod # i can change module name
# # import my_mod as mm # more often popular libraries use abbreviations

# # from my_mod import add as big_add

# # print(add(56,66))
# # print(txt)
# # # my_big_mod.add(333,11)
# # mm.add(14324,5)
# # print(mm.mlist)
# # big_add(62,44535)

# # # print(mm.sorted([1,2,3,9,5]))

# # # # which sorted will be called?
# # # # so our sorted will be called, so it is possible to overwite
# # # print(sorted([1,2,3,10,4]))
# # # print(system_sorted([1,2,3,10,4]))
# # # # # # # # print("This could be a big program")
# # # # # print(mat_lib.add(50,100))


# # print(my_mod.add(4, 7))
# # my_mod.add(50, 87)
# # print(my_mod.txt)
# # print(my_mod.mlist)
# # my_mod.mlist.append(55) # somebody else importing this will get a a new list

# # print(my_mod.mlist)

# # new_obj = my_mod.Klase()
# # # # print(type(new_obj))
# # # # # # # new_obj.new_prop = "Vertiba"
# # # # # # # print(new_obj.new_prop)
# # garage_1 = my_mod.Garage()
# # garage_2 = my_mod.Garage('Lielaa')
# # print(sys.path) # so sys.path will show where Python will look for modules and packages
# # # # # # # garage_3 = mlib_mod.Garage("Baismigā")
# # # # # # # mlib_mod.mlist.append(9000)
# # # # # # # print(mlib_mod.mlist)
