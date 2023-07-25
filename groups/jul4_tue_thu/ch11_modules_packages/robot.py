# so we will store our robot class in a separate file

class Robot:
    def __init__(self, name):
        self.name = name
    
    def say_hi(self):
        print(f"Hi, I am {self.name}")
    
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name


# we could divide our tasks into main and tests functions

def main():
    print("This is the robot module run directly")
    # let's test some robots
    x = Robot("Marvin")
    x.say_hi()
    x.set_name("Henry")
    x.say_hi()
    y = Robot("Alice")
    y.say_hi()
    return [x, y]

def tests(robot_list):
    # Testing all robots if name is set properly
    proper_names = ["Marvin", "Henry", "Alice"]
    # for i, robot in enumerate(robot_list):
    #     assert robot.get_name() == proper_names[i]
    # assert we got 2 robots
    assert len(robot_list) == 2 # good test if we know we only need 2 robots


# we might want to use main guard here
if __name__ == "__main__": # check if we are running this file directly or importing it
    robot_list = main() # could have been called make_robots() functions
    tests(robot_list)