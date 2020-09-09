# while loops
# print("Hello")
# print("Hello")
# print("Hello")
# DRY princips - do not repeat yourself
i = 3
while i < 5:
    print("Hello Nr.", i)
    # do more stuff here inside the loop
    i += 1
# loop is finished here
print("This will happen no matter what")
i = 10
while i > 0:
    print("Going Down the floor:", i)
    i -= 1
print("All done")

total = 0 # do not use sum as a variable please :)
i = 20
while i <= 30:
    total += i # total = total + i
    i += 1
print("20 to 30 summed is", total)
print(sum(range(20,30+1)))