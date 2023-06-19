# let's create a simple robot that will do some tasks
# we will emulate tasks with functions

# will will only use functions

# since we only know lists and functions we will use them
# in order to emulate a robot
# ideally we would use classes and objects
# and possibly dictionaries

# so first we need to create a robot
# first we will need to create a list
# we need to store state of the robot
robot = ["Johnny", 0, 0] # name, x, y - general info about the robot
sayings = ["Hello", "Bye", "I am a robot", "I am hungry", "I am tired"]

# our function will be to say something
# we will need to pass the robot and the saying
def say(robot, saying):
    print(f"{robot[0]} says: {saying}")

# let's call it
say(robot, sayings[0])

# how about we make a random sayings robot
# we will need to import random
import random # we need to import it at the top of the file
# if we want random seed
# random.seed(2023) # we need to import it at the top of the file
# this will make sure that we get the same random numbers
def random_say(robot):
    saying = random.choice(sayings)
    say(robot, saying)

# # let's call it a few times
# for _ in range(5):
#     random_say(robot)
# let's make function to repeat it multiple times
def random_say_multiple(robot, times):
    for _ in range(times):
        random_say(robot)

random_say_multiple(robot, 5)

# now let's make a robot that can move
# we will need to pass the robot and the direction
def move(robot, direction):
    """
    Moves the robot in the given direction
    possible directions: up, down, left, right

    Returns the new position of the robot
    """
    # above is a docstring - it will be used as documentation	
    # TODO rewrite with match - new syntax in python 3.10
    # FIXME - fix this function to work with match
    # we use FIXME to mark something that needs to be fixed - not working code
    # here code works and actually is fine
    if direction == "up":
        robot[2] += 1 # this modifies the list that is passed!
        # we could have also had a function that moves the robot up
    elif direction == "down":
        robot[2] -= 1
    elif direction == "right":
        robot[1] += 1
    elif direction == "left":
        robot[1] -= 1
    else:
        print("Unknown direction") 
    # let's print current position
    # print(robot[1], robot[2]) 
    print(f"{robot[0]} is at {robot[1]}, {robot[2]}")
    # it would be nice to return the position
    # so we can use it later
    return [robot[1], robot[2]] # list of x and y

# let's call it a few times
move(robot, "up")
move(robot, "up")
move(robot, "right")
move(robot, "right")
move(robot, "right")
move(robot, "down")
# so we should be at 3, 1

# we could also create a functionality to move multiple times
# we will need to pass the robot and the directions
def move_multiple(robot, directions):
    for direction in directions:
        move(robot, direction)

# let's call it a few times
move_multiple(robot, ["up", "up", "right", "right", "right", "down"])
# we should be at 6, 2 right?

current_location = move(robot, "up") 
print(current_location) # separate data from robot
print(robot)

