# Python pathlib library
# since 3.4 combines functionality of different path libraries
# os, glob - those can be still used
# pathlib is safer across many OSes
# https://realpython.com/python-pathlib/

from pathlib import Path
p = Path('.')  # our current working directory
print(f"Current PATH {p}")
# p.glob is a generator so need to cast to list
local_txt_files = list(p.glob("*.txt"))
print(local_txt_files)
parent = Path('..')  # we go up to our parent
sub_folders = [x for x in parent.iterdir() if x.is_dir()]
print(sub_folders)
parent_files = [x for x in parent.iterdir() if x.is_file()]
print(parent_files)
