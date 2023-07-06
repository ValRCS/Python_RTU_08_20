# while loops
# idea do something while some condition remains True
# while True:
#     # inside while loop
#     print("Alice talked")
#     # still inside while loop
#     print("and talked...")
# outside while loop
# some infinite loops are actually useful we shall see
# for now let's try to end our while loop
i = 0
while i < 5:
    print("Hello there", i)
    i += 1 # Python has no ++ nor --
    # so i += 1 is same as i = i + 1
    
# we are outside loop
print("Outside")

# we can go the other way
floor = 10
special_floor = 6
speed = 2
ground = 0
while floor > ground:
    print(f"We are on the floor {floor}")
    # we can check for conditions with if inside our loop
    if floor == special_floor:
        print(f"Oh {floor} is on special floor {special_floor}")
    floor -= speed # so going down
    
print("outside loop")

# we can generalize our positive loop as follows
start = 100
stop = 120
step = 5

i = start
while i <= stop:
    print(f"doing something with {i} or such")
    i += step
