# for loops
for n in range(1,20,2): # range(5) start with 0 until and including 4 !!
    print(n)
    # do more stuff in here
print("Whew all done",n)
print("\n")
print("Printing my food")
food = "kartupelis"
for c in food:
    print(c, "::", end="") # are end="" es atsledzu newline

my_list = [1,2,3,6,7,2,19,645,5453,100, -50]
total = 0
for num in my_list:
    print(num)
    total += num
print(total)
print(sum(my_list))

record = None
for num in my_list:
    if record == None:
        record = num
    if num > record:
        record = num
print("The record is held by", record)
print(max(*my_list)) # we can unroll the list and use max to find max

for n in (1,6,7,8,-5,10): # we loop through a tuple
    print(n)
    
