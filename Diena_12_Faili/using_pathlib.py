# Python pathlib library
# since 3.4 combines functionality of different path libraries
# os, glob - those can be still used
# pathlib is safer across many OSes
# https://docs.python.org/3/library/pathlib.html
# https://realpython.com/python-pathlib/

# quick and dirty

# absolute paths are generally not recommended very inflexible!
# with open("C:/Users/val-p1/Github/Python_RTU_08_20/data/stopping_frost.txt") as f:
#     print(f.readlines())
# C:\Users\val-p1\Github\Python_RTU_08_20\data\stopping_frost.txt


# relative is a better option
# .. means go up one dir level relatively
# with open("../data/stopping_frost.txt") as f:
#     print(f.readlines())

# this works but for complicated path manipulation
# library is recommended (OS differences)


from pathlib import Path  # from Python 3.4 onwards
# there is also older os.path library
# . means current path
p = Path('.')
print(p)
print(p.absolute())

# somewhat similar to going up with ../
# print(p.resolve().parents[0])
# print(p.resolve().parents[1])
# print(p.resolve().parents[2])

# for parent in p.resolve().parents:
#     print(parent)

print(__file__)
ogpath = Path(__file__).resolve()  # so full path for your calling path
print(ogpath)
print(ogpath.parents[0])
print(ogpath.parents[1])

# first part has to be Path !
# with this i guarantee OS compatibility
frostpath = ogpath.parents[1] / "data" / "stopping_frost.txt"
print(frostpath, type(frostpath))
# # notice the \ on windows!
# with open(frostpath) as f:
#     print(f.readlines())

p = Path('.')  # our current working directory
# Path could be a file or folder/directory
print(f"Current PATH {p.resolve()}")
# p.glob is a generator so need to cast to list
local_txt_files = list(p.glob("*.txt"))
print(local_txt_files)
for fname in local_txt_files:
    print(fname.suffix)  # just the last suffix
    print(fname.suffixes)  # list of all suffixes
    print(fname.with_suffix(".vstxt"))

# parent = Path('..')  # we go up to our parent
# sub_folders = [fp for fp in parent.iterdir() if fp.is_dir()]
# print(sub_folders)
# for subf in sub_folders:
#     print(subf.resolve())  # so i can get absolute file names also
# parent_files = [x for x in parent.iterdir() if x.is_file()]
# print(parent_files)
# print(parent_files[0])
# parent_py_files = [x for x in parent.iterdir() if x.is_file()
#                    and x.suffix == ".py"]
# print(parent_py_files)

# getting all files recursively
# parent = Path('..')  # we go up to our parent
# pyfiles = sorted(Path('../..').glob('**/*.py'))
# print(pyfiles)
# for fname in pyfiles:
#     print(fname, type(fname), fname.resolve())
#     print(fname.stem, type(fname.stem))
