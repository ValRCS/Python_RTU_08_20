# it is typical to use a dictionary to keep some state about some object
# for now we are not using class-based objects - thats next lesson 
# so we will use a dictionary to keep track of robots

robot = {
    "name": "Robocop",
    "material": "titanium",
    "skills": ["walking", "talking", "singing", "dancing","protecting"],
    "year": 1987
} # again this is very loose and flexible
print(robot)
# how about another robot?
# wally
wally = {
    "name": "WALL-E",
    "material": "metal",
    "skills": ["walking", "talking", "singing", "dancing","collecting"],
    "year": 2008
}
print(wally)
# we can also store multiple robots in a list or dictionary
# how about a list of robots?
robots = [robot, wally]
print(robots)
# i can add another robot to the list
robots.append({"name": "Terminator", 
               "material": "flesh", 
               "skills": ["walking", "talking", "shooting", "hunting","killing"], 
               "year": 1984})
print(robots)
# how about getting terminator in separate variable?
terminator = robots[-1]
print(terminator)
# so I have a list of dictionaries
# some dictionaries have same keys, some have different keys
# some values are strings, some are lists, some are numbers
# how about adding a new skill to terminator?
# how about protecting Sarah Connor?
# if we have dictionary in a variable we can use it like any other variable
# terminator["skills"].append("protecting Sarah Connor")
# if we need to get dictionary from a list we would do the following
robots[-1]["skills"].append("protecting Sarah Connor")
# we have 3 possible failures here
# first robots might be empty list, so we need to check that
# just keep in mind that possible key skills might not exist in all dictionaries
# also value for key skills might not be a list