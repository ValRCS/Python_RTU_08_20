# while loops
# print("Hello there!")
# print("Hello there!")
# print("Hello there!")
# DRY principle - do not repeat yourself
print("Alice ")
# infamous infinite loop
# while something is True do something inside the while block
# while True:
#     print("talked")
    # we could do more here
    # 
# out of loop here

# philosophically speaking
# while loops are for when we do not know how long we want to  loop

i = 0 # iterator variable, can use any name
while i < 5:
    print("talked")
    print(f"i is now {i}")
    i += 1 # same as i = i + 1
    # Python does not have ++ or --
    # still inside loop block
# now code continues when i >= 5, that i < 5 is False
print(f"i after end of the loop is {i}")

# we can the other way
floor = 10
while floor > 3:
    print(f"Going down, currently on floor {floor}")
    floor -= 2  # same as floor = floor - 2
print(f"All done, floor is now {floor}")

total = 0 # do not use sum for variable name, summa is ok
i = 0
while i < 20:
    total += i
    print(f"Total is now {total}, i is {i}")
    # we could many more things here
    i += 1
print("Total finally is {total}")
    