# we will create a simple robot to demonstrate functions
# we will only use functions and lists

# ideally we would use classes, objests and dictionaries

# we will use a list to store our robot's commands
commands = []
# also we will use a list to store information about robot
robot = ["Robotniks", 0, 0] # name, x, y
# again dictionary or object would be better - but we only know lists

# how about some sayings for our robot
sayings = [
    "I am Robotniks",
    "I am a robot",
    "Hello",
    "Bye",
    "I am lost"
]

# so now we will create a function to say something
# we will pass robot and sayings as arguments
def say(robot, saying):
    print(f"{robot[0]}: {saying}")

# let us test our function
say(robot, sayings[0]) # Robotniks: I am Robotniks

# how about random saying
# we will use random module
import random
def random_say(robot, sayings):
    # we will use random.choice to get a random saying
    random_text = random.choice(sayings)
    say(robot, random_text)

# let us test our function
random_say(robot, sayings)

# how about a function to say something n times
def say_random_n_times(robot, n):
    for _ in range(n):
        random_say(robot, sayings)

# let us test our function
say_random_n_times(robot, 5)

# how about a function to move our robot
def move(robot, x, y):
    # we could include test if x and y are numbers
    # maybe there would be a limit to how far robot can move
    robot[1] += x
    robot[2] += y
    # this function modifies the robot list

# let us test our function
move(robot, 1, 1)
print(robot) # ['Robotniks', 1, 1]

# how about human readable move function
def move_human(robot, direction, debug=False):
    """Move robot in a direction
    First parameter is a list with robot information
    Second parameter is a string with direction
    Valid directions are up, down, left, right
    """
    # i used docstring to document my function
    if direction == "up":
        move(robot, 0, 1)
    elif direction == "down":
        move(robot, 0, -1)
    elif direction == "left":
        move(robot, -1, 0)
    elif direction == "right":
        move(robot, 1, 0)
    else:
        print("I do not understand")
    if debug:
        print(f"Robot {robot[0]} moved to {robot[1]}, {robot[2]}")
    # lets return robot position as a list
    return [robot[1], robot[2]]

# let us test our function
move_human(robot, "up")
move_human(robot, "up")
move_human(robot, "left")
last_location = move_human(robot, "left")
# this last location is not related to robot anymore
print(robot) # ['Robotniks', -1, 3]
print(last_location) # [-1, 3]

# let's make a function accept multiple commands
def accept_commands(robot, commands):
    for command in commands:
        move_human(robot, command)

# let us test our function
accept_commands(robot, commands)
print(robot) 
commands = ["up"]
accept_commands(robot, commands)
print(robot)
commands = ["up", "left", "left", "left", "down",  "right"]
accept_commands(robot, commands)
print(robot)
# now i can debuf if i want
# here debugging simply means printing
move_human(robot, "up", debug=True)
