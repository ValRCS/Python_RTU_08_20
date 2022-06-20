# # # # # # # # # # # # # importing Python Modules and Packages
# # # # # # # # # # # # # https://docs.python.org/3/tutorial/modules.html
# # # # # # # # # # # # # https://realpython.com/python-modules-packages/
# # # # # # # # # # # # # modular programming
# # # # # # # # # # # # # way to divide and conqure larger tasks
# # # # # # # # # # # # # code reusability
# # # # # # # # # # simplicity - subset of the problem
# # # # # # # # # # maintainability - different domains different libraries
# # # # # # # # # # namespaces - avoid naming conflicts/colusions
# # # # one of the most difficult problems in programming is the one of naming conflicts

# # # # # # # # # # # # # # if not found in current directly
# # # # # # # # # # # # # # Python will look for my_mod.py in paths defined in PYTHONPATH enviroment variable
# # # # # # # # usually we import standard libary first
import sys # sys is standard library package, for functionality dealing with system function
print(sys.path)  # this shows where Python will look for modules in order
# # # # import string # string is standard library package, for functionality dealing with strings
# # # # print(string.digits) # this will print all digits
# # # # # but we imported our string...
# # # # # import my_string_mod # this will import my_string_mod.py
# # # # # print(my_string_mod.my_stringie) # so our module was imported... hmm
# import june_mod
# print(june_mod.a) # this will print 42
# june_mod.some_func()
# import my_mod  #works if the module is in same directory
# import antigravity # this will import antigravity.py
# print(antigravity.geohash("Riga"))
# my_mod.add(10,20)
# print(my_mod.txt)
# print(my_mod.mlist)

# # # # # # # # print(my_mod.add(10,20))
# my_garage = my_mod.Garage()
# print(my_garage.gname)

# # # # typically all imports go in the top of the file
# # # import my_mod_2 #works if the module is in same directory

# # # my_mod_2.my_fun()

# import pkg.my_utils  #import pkg not much good
# pkg.my_utils.pkg_add(10,20)


# import pkg.my_utils as mu # shorter way
# mu.pkg_add(10,20)
# print(mu.MY_CONST)

# # # # # # i could go 2 folders deeper and import sub_utils
# import pkg.subp.sub_utils as su # shorter way
# su.subadd(10,20)
# su.badprint()
# print(su.MAGIC_PI)

# # # # If I have a big module, I can import specific parts of it

# from my_mod import add, txt, mlist # this will import only add and txt and mlist
# add(10,20)
# print(txt)
# print(mlist)

# # # careful with naming conflict, we lose namespace - essentially no prefix

# # def subadd(a, b):
# #     print(f"My local subadd {a-b+100}")
# #     return a-b+100

# # # # # we import a single function from module 2 levels down - with alias which name collision
# from pkg.subp.sub_utils import subadd as add # this will import only subadd and badprint
# add(51,55)

# # # # # if i have a naming conflict I can import with alias
# from my_mod import add as my_super_add
# my_super_add(10,20)

# my_mod.add(45,23)
# # # # # new_garage = my_mod.Garage()
# # # # # print(my_mod.mlist)
# # # # # print(my_mod.txt)

# import my_mod as mm # rename module basically, mm can be anything
# mm.add(3,65)
# print(mm.mlist)

# # # # # if I am sure that there are no naming conflicts
# # # # # from my_mod import add, txt # just one function, make sure no name conflicts
# # # # # add(5,67)
# # # # # print(txt)

# # # # # # rarer
# # # # # from my_mod import add as super_add # import just one function with new name
# # # # # super_add(62,66)

# # # # # # # TIP: do not name your files the same name as standard library imports 

# import pkg.my_utils  # import pkg standalone not much good
# pkg.my_utils.pkg_add(10,20)

# import pkg.my_utils as mu  # typical to rename modules
# mu.pkg_add(10,20)

# # # # # from pkg.my_utils import pkg_add
# # # # # pkg_add(10,20)  # this is the same as mu.pkg_add(10,20) previously

# # # # # from pkg.my_utils import pkg_add as pkg_add_new
# # # # # pkg_add_new(10,20) # same as pkg_add(10,20) previously

# # # # # import my_lib.my_tools
# # # # # my_lib.my_tools.complex_fun(5,6)

# # # # # # # # # import my_lib will not do much
# # # # # # # # from my_lib import my_mod
# # # # # # from my_lib import my_tools # so just llike import my_tools but from subfolder
# # # # # # my_tools.tool_fun("Is this an argument?")
# # # # # # from my_lib import my_tools as myt # so just llike import my_tools but from subfolder
# # # # # # myt.tool_fun("OHO")
# # # # # # from my_lib.my_tools import tool_fun # so just one function from  my_tools file in my_lib folder
# # # # # # tool_fun("This should also work")
# # # # # # from my_lib.my_tools import tool_fun as tf #importing one function and renaming
# # # # # # tf("This should also work")

# import pkg.subp.sub_utils as su # import pkg standalone not much good
# su.badprint()
# print(su.MAGIC_PI)

# # # # # # from pkg.subp import sub_utils # so sub_utils.py is two folders deep pkg/subp/sub_utils.py
# # # # # # print(sub_utils.MAGIC_PI)

# # # # # # from pkg.subp.sub_utils import subadd # so function subadd from 
# # # # # # subadd(60,22)


# # # # # # # new_garage = my_mod.Garage()
# # # # # # # print(my_mod.mlist)
# # # # # # # # from my_lib.my_mod import add
# # # # # # # # add(33,666)
# # # # # # # from my_mod import Garage # so i can import just specific class, value, function etc
# # # # # # # # just careful with name collision, no protection
# # # # # # # # avoid from my_mod import * # this is bad practice
# # # # # # # also_garage = Garage()

# # # # # # # # if I do not like module name I can change it
# # # # # # # import my_mod as mm # very common to use short names
# # # # # # # mm.add(5,16)

# # # # # # # from my_mod import Garage as GG
# # # # # # # another_garage = GG()

# # # # # # # # long way for specific tool
# # # # # # # import my_lib.my_tools
# # # # # # # my_lib.my_tools.tool_fun("AHa!")

# # # # # # # import my_lib.my_tools as mt 
# # # # # # # mt.tool_fun("oho")

# # # # # # # import my_lib

# # # # # # # my_lib.my_tools.tool_fun("oh")
# # # # # # # print(mt.complex_fun(5, 10))

# # # # # # # from my_lib.my_tools import complex_fun as cfun
# # # # # # # print(cfun(6,100))



# # # # # # # # import my_mod
# # # # # # # # # # # import mat_lib


# # # # # # # # from my_mod import add # of course make sure there are no naming conflicts
# # # # # # # # from my_mod import txt # of course make sure there are no naming conflicts

# # # # # # # # # system_sorted = sorted # it is possible to save system function before rewriting the reference
# # # # # # # # # from my_mod import sorted # it is possible but not advisable

# # # # # # # # # import my_mod as my_big_mod # i can change module name
# # # # # # # # import my_mod as mm # more often popular libraries use abbreviations

# # # # # # # # from my_mod import add as big_add

# # # # # # # # print(add(56,66))
# # # # # # # # print(txt)
# # # # # # # # # my_big_mod.add(333,11)
# # # # # # # # mm.add(14324,5)
# # # # # # # # print(mm.mlist)
# # # # # # # # big_add(62,44535)

# # # # # # # # # print(mm.sorted([1,2,3,9,5]))

# # # # # # # # # # which sorted will be called?
# # # # # # # # # # so our sorted will be called, so it is possible to overwite
# # # # # # # # # print(sorted([1,2,3,10,4]))
# # # # # # # # # print(system_sorted([1,2,3,10,4]))
# # # # # # # # # # # # # # print("This could be a big program")
# # # # # # # # # # # print(mat_lib.add(50,100))


# # # # # # # # print(my_mod.add(4, 7))
# # # # # # # # my_mod.add(50, 87)
# # # # # # # # print(my_mod.txt)
# # # # # # # # print(my_mod.mlist)
# # # # # # # # my_mod.mlist.append(55) # somebody else importing this will get a a new list

# # # # # # # # print(my_mod.mlist)

# # # # # # # # new_obj = my_mod.Klase()
# # # # # # # # # # print(type(new_obj))
# # # # # # # # # # # # # new_obj.new_prop = "Vertiba"
# # # # # # # # # # # # # print(new_obj.new_prop)
# # # # # # # # garage_1 = my_mod.Garage()
# # # # # # # # garage_2 = my_mod.Garage('Lielaa')
# # # # # # # # print(sys.path) # so sys.path will show where Python will look for modules and packages
# # # # # # # # # # # # # garage_3 = mlib_mod.Garage("Baismigā")
# # # # # # # # # # # # # mlib_mod.mlist.append(9000)
# # # # # # # # # # # # # print(mlib_mod.mlist)
