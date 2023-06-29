# we can import my_module.py from anywhere as long as it is in the same folder

import my_module # we can import any file that is in the same folder

# now let's change the variable in my_module.py
my_module.my_variable = 150
print(my_module.my_variable)