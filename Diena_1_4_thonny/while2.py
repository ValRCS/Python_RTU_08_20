# print("Hello")
# print("Hello")
# DRY - Do not repeat yourself
i = 0
while i < 10:
    # inside the loop
    print("Hello loop", i)
    print("More stuff to be done")
    i += 2 # i = i + 1
    # still inside loop
# now we are outside
print("This will print after loop is done",i)

is_sky_blue = True
while i > 0 and is_sky_blue:
    print("Going down from floor",i)
    i -= 1
print("Now down to", i)
