# # # # # importing Python Modules and Packages
# # # # # https://docs.python.org/3/tutorial/modules.html
# # # # # https://realpython.com/python-modules-packages/
# # # # # modular programming
# # # # # way to divide and conqure larger tasks
# # # # # code reusability

# import my_lib will not do much
from my_lib import my_mod
my_mod.add(45,23)
from my_lib.my_mod import add
add(33,666)


# import my_mod
# # # import mat_lib
# # # # # # if not found in current directly
# # # # # # Python will look for my_mod.py in paths defined in PYTHONPATH enviroment variable
# import sys # sys is standard library package, for functionality dealing with system function

# from my_mod import add # of course make sure there are no naming conflicts
# from my_mod import txt # of course make sure there are no naming conflicts

# system_sorted = sorted # it is possible to save system function before rewriting the reference
# from my_mod import sorted # it is possible but not advisable

# import my_mod as my_big_mod # i can change module name
# import my_mod as mm # more often popular libraries use abbreviations

# from my_mod import add as big_add

# print(add(56,66))
# print(txt)
# my_big_mod.add(333,11)
# mm.add(14324,5)
# big_add(62,44535)

# print(mm.sorted([1,2,3,9,5]))

# # which sorted will be called?
# # so our sorted will be called, so it is possible to overwite
# print(sorted([1,2,3,10,4]))
# print(system_sorted([1,2,3,10,4]))
# # # # # # print("This could be a big program")
# # # print(mat_lib.add(50,100))



# # print(my_mod.add(4, 7))
# # # # # # my_mod.add(50, 87)
# # print(my_mod.txt)
# # print(my_mod.mlist)
# # my_mod.mlist.append(55) # somebody else importing this will get a a new list

# # print(my_mod.mlist)

# # new_obj = my_mod.Klase()
# # # # print(type(new_obj))
# # # # new_obj.new_prop = "Vertiba"
# # # # print(new_obj.new_prop)
# # garage_1 = my_mod.Garage()
# # garage_2 = my_mod.Garage('Lielaa')
# print(sys.path) # so sys.path will show where Python will look for modules and packages
# # # # # garage_3 = mlib_mod.Garage("Baismigā")
# # # # # mlib_mod.mlist.append(9000)
# # # # # print(mlib_mod.mlist)
