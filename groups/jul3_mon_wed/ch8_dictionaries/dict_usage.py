# it is typical to use dictionary to keep state about something
# let's say I have a robot device (and I do not know about classes/objects just yet)

robot = {
    "name": "R2D2",
    "material": "metal",
    "speed": 10,
    "x": 0,
    "y": 0,
    "z": 0
}

print(robot)

# how about many robots?

# usual idea would be to have a list of dictionaries
# but we can also have a dictionary of dictionaries

# let's see list of dictionaries first

robots = [
    {
        "name": "R2D2",
        "material": "metal",
        "speed": 10,
        "x": 0,
        "y": 0,
        "z": 0
    },
    {
        "name": "C3PO",
        "material": "metal",
        "speed": 5,
        "x": 0,
        "y": 0,
        "z": 0
    },
    {
        "name": "Wall-E",
        "material": "metal",
        "speed": 1,
        "x": 0,
        "y": 0,
        "z": 0
    }
]

# so how would i get name of Wally?

print(robots[2]["name"]) # also -1 would work here for index

# so how would I find all robots whose speed is over 5?
speed = 5
fast_robot_list = []
for robot in robots:
    if robot["speed"] > speed:
        print(robot["name"])
        fast_robot_list.append(robot) # this list will contain references to the same dictionaries as robots list
        # if i did not want to use original robot then I would make a copy instead
        # fast_robot_list.append(robot.copy()) # this would be a new robot dictionary
print(fast_robot_list)

fast_robot_list[0]["speed"] = 100 # this will change the speed of the first robot in both lists

print(robots)
print(fast_robot_list)

