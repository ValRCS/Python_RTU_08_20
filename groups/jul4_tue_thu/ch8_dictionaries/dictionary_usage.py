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