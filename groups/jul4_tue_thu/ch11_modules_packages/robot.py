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


# we might want to use main guard here
if __name__ == "__main__": # check if we are running this file directly or importing it
    print("This is the robot module run directly") # so this runs when we import robot.py
    # let's test some robots
    x = Robot("Marvin")
    x.say_hi()
    x.set_name("Henry")
    x.say_hi()
    y = Robot("Alice")
    y.say_hi()
    # let's check if we can access x's name
    assert x.get_name() == "Henry" # simple sanity check