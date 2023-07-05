# while loops
# while True:
#     # block of while loop starts here
#     print("Banana")

i = 0
while i < 5:
    print("Hello", i)
    # crucial we change i somewhat - loop invariant
    i += 1 # same as i = i + 1 # Python does not have ++ or --
    # still inside loop block
    # we will go back to start of while and check condition
# we are outside loop
print("We are outside loop")

# we can also go down
floor = 10
speed = 2
while floor >= 0:
    print(f"We are on floor {floor}")
    if floor == 4:
        print(f"OH we are on special floor {floor}")
    floor -= speed # so we go down by speed
    
start = 100
stop = 120
step = 5

i = start
while i <= stop:
    print(f"DOing something with {i}")
    i += step