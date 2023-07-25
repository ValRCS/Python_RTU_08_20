# we can use wide selection of external libraries
# some sources for libraries
# https://pypi.org/ - main Python library repository

# so i install tqdm with pip install tqdm from command line
# preferably in virtual environment (venv) 
# we create venv with python -m venv venv_name
# venv is the official way to create virtual environments
# docs: https://docs.python.org/3/library/venv.html
# then we activate it with venv_name\Scripts\activate.ps1
# then we install libraries with pip install library_name

# let's see how we can use tqdm
# typically we import tqdm with from tqdm import tqdm
from tqdm import tqdm

# so lets count something
count = 0
# so I wrap range with tqdm
# instead of range it could be any iterable
for i in tqdm(range(10_000_000)):
    count += i
# print result
print(count)