import sys
print(sys.path) # shows paths Pythons looks for when importing

# import pkg.my_utils
# import pkg.my_utils as my_ut
# from pkg.my_utils import add
# import pkg.subp.sub_utils
# import pkg.subp.sub_utils as s_ut

# pkg.subp.sub_utils.subadd(34,6)
# s_ut.subadd(34,6)
# from pkg.subp.sub_utils import MAGIC_PI
from pkg.subp.sub_utils import MAGIC_PI as PI

# print(MAGIC_PI)
print(PI)


# pkg.my_utils.add(5,6)
# my_ut.add(3,3)
# add(5,32)

# import my_mod
# import my_mod as mm # could rename our module, popular libaries have their own short names



# i could import something specific
# from my_mod import add # careful with name collision
# from my_mod import txt 
# from my_mod import Garage

# from my_mod import Garage as GG # so i can rename when importing 

# ng5 = GG()
# ng6 = GG()

# add(5,333)
# print(txt)
# ng = Garage("garazha")
# ng2 = Garage("garazha2")


# ng3 = my_mod.Garage("garazha 3")
# ng4 = my_mod.Garage()
# my_mod.add(5,6)
# print(my_mod.txt)
# print(my_mod.mlist) # so each import gets their own
# my_mod.mlist.append(777)
# print(my_mod.mlist)
# print(mm.add(6,22))
# print(mm.txt)