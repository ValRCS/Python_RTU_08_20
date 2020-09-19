# Creating and using packages
# simply make subfolders
# moved .py there
# create __init__.py
# https://docs.python.org/3/reference/import.html
# https://stackoverflow.com/questions/12229580/python-importing-a-sub-package-or-sub-module
# https://realpython.com/lessons/subpackages/


import pkg.my_utils
import pkg.my_housing
import pkg as pk
import pkg.subp.sub_utils
import pkg.subp.sub_utils as sutils
# from pkg.subp.sub_utils import subadd # can use this thats fine
# from pkg.subp.sub_utils import * # avoid this, because of namespace pollution
from pkg.subp.sub_utils import (
    subadd,
    subprint,
    MAGIC_PI
)

pkg.my_utils.add(30, 50)
gar = pkg.my_housing.Garage("Funny")

pk.my_utils.add(30, 60)

pkg.subp.sub_utils.subadd(100, 20)
sutils.subadd(50, 20)

subadd(30, 90)
subprint("Valdis")
print(MAGIC_PI)
