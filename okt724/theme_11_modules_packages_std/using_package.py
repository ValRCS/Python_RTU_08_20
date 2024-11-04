# so package is a collection of modules
# typically it is in a directory/folder
# it used to be that there was a __init__.py file in the directory to make it a package
# it is not required in Python 3.3 and later

# so let's use a specific module from my_package
# import my_package.stats # now I can use the functions from stats module
# i could import my_package.stats as st # alias
import my_package.stats as st # alias

# now let's use the functions from stats module
data = [1, 2, 3, 4, 5]
# print(my_package.stats.mean(data)) # 3.0
print(st.mean(data)) # 3.0

# let's compare with standard library statistics module
import statistics # this is standard library module - built in
print(statistics.mean(data)) # 3.0

# similary I could import specific functions from the module
# let's import add from my_package.module_1
from my_package.module_1 import add # no namespace protection

# now let's use the add function
print(add(2, 3)) # 5