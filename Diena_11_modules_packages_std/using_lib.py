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

import mlib_mod
import my_pak.mpak_mod
import my_pak.supermod as smod

mlib_mod.add(55, 555)
my_pak.mpak_mod.add(100, 24)
smod.add(666, 77)
