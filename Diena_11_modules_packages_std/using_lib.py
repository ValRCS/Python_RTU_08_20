# import my_lib.my_mod
# import my_lib.my_mod as mmod
# from my_lib.my_mod import add

# my_lib.my_mod.add(6, 10)
# mmod.add(10, 60)
# add(666, 111)

# this does not relaly work
# from ..mlib import my_mod

# this does work
# import sys
# sys.path.append("..")
# print("hmm")
# import mlib.my_mod

# import mlib_mod
# import my_pak.mpak_mod
# import my_pak.supermod as smod

# mlib_mod.add(55, 555)
# my_pak.mpak_mod.add(100, 24)
# smod.add(666, 77)

import my_cool_lib.my_cool_mod
from my_cool_lib import my_cool_mod
from my_cool_lib import my_cool_mod as mcm # very common to rename modules
from my_cool_lib.my_cool_mod import add # careful could have name collission with another module
from my_cool_lib.my_cool_mod import add as my_add

my_cool_lib.my_cool_mod.add(5,11)
my_cool_mod.add(10,11)
mcm.add(50,10)
add(55,22)
my_add(66,66)
