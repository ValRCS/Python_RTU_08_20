# let us read our Robot list back
# we need pickle
# we also need Robot class
from robot import Robot # otherwise it will fail
import pickle

with open("data/robots.pickle", mode='rb') as fstream:
    # file is open here
    # we will use pickle.load to load the object
    loaded_robot_list = pickle.load(fstream)
    # file is still open here

# file is closed here - no need to close it manually!

# let's print it
print(loaded_robot_list)

# so i can save any Python object to a file using pickle
# exception
# i can use say first robot
print(loaded_robot_list[0].condition())