# while loops
# print("Hello")
# print("Hello")
# print("Hello")
# DRY princips - do not repeat yourself
i = 0
while i < 5: # while i<5 is true we do the below block
    print("Hello Nr.", i)
    i += 1 # i = i+1
    # do more stuff for each loop cycle
    print("Still inside working on", i)
print(f"Outside Loop i is {i}")
#     
# i = 0    
# total = 0
# when I am typing is sound scratchy ?
# 
# while i < 6:
#     total += i
#     print("Hello Nr.", i, total)
#     # do more stuff here inside the loop
#     i += 1 # i = i + 1
# print(f"Total sum is {total}")
# print(f"I value at the end is {i}")

# i = 1
# print("Hello Nr.", i)
# i += 1
# print("Hello Nr.", i)
# i += 1
# print("Hello Nr.", i)
# i += 1
# print("Hello Nr.", i)
# i += 1
# loop is finished here
# print("This will happen no matter what")

# i = 10
# while i > 0:
#     print("Going Down the floor:", i)
#     i -= 1
# print("All done with i", i)

# i = 10
# while i >= 0:
#     print("Going Down the floor:", i)
#     i -= 2
# print("All done with i", i)
#

# total = 0 # do not use sum as a variable please :)
# i = 0
# while i <= 10:
#     total += i # total = total + i
#     print(f"i is {i} and total is {total}")
#     i += 2.5
# print("20 to 30 summed is", total)
# print(sum(range(20,30+1)))

# num = int(input("Factorial of? "))
# result = 1
# i = num
# while i > 1:
#     result *= i # result = result * i
#     print("Result so far", result) # remember that print is an expensive operation and slow
#     i -= 1
# print(f"Factorial of {num} is {result}")