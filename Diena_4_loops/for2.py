# # while loops are for INDEFINITE looping when we are not quite sure when to end loop
# # for loops are for DEFINITE looping
# for n in range(10):
#     print("My number is ", n)
#     # do more stuff while inside loop
# print("n is still 9:",n)
# 
# # so range start and end not including the last value
# for n in range(1,6):
#     print(n)

# for n in range(20):
#     print("*", end="")
# print("")
# no need for this in Python
# print("*V*"*20)
# 
# # for loops with beg, end, and step size
# for n in range(0,10,3): #  start with 0 until 9 with step 2 so only until 8!!
#     print(n)
#do more stuff in here
  
# roman cypher
# myname = "Valdis"
# result = ""
# OFFSET = 5
# for c in myname:
#     print(c)
#     print("Still Working with letter", c)
#     newchar = chr(ord(c)+OFFSET)
#     result += newchar
# print(f"My name {myname} transformed is {result}")
    
# print("Whew all done",c)
# print("\n")
# print("Printing my food")
# food = "kartupelis"
# for mychar in food:
#     print(mychar, end="|") # are end="" es atsledzu newline
# print("Done with food for now")
#
# 
# for i,c in enumerate(food):
#     print(f"index {i} for letter {c}")

myname = "Valdis"
for i, c in enumerate(myname, start=1):
    print(i, c)
    temp = i + 5
    print(temp)
#  
# # sum = 0 # bad bad variable name! because sum is used by Python to sum sequences!
# total = 0
# for i,c in enumerate(food, start=9001):
#     print(f"index {i} for letter {c} and unicode is {ord(c)}")
#     total += ord(c) 
# 
# print('all unicode summed is', total)
# print('total unicode character is', chr(total))

# for n in range(5):
#     if n % 2 == 0:
#         print(f"{n} is even!")
#     else:
#         print(f"{n} is odd!")
# 
# print("*"*12)
# my_list = [1,2,3,6,7,2,19,645,5453,100, -50]
# total = 0
# for num in my_list:
#     print(num)
#     total += num
# print(total)
# print(sum(my_list))
# # 
# # record = None
# # for num in my_list:
# #     if record == None:
# #         record = num
# #     if num > record:
# #         record = num
# # print("The record is held by", record)
# # print(max(*my_list)) # we can unroll the list and use max to find max
# # 
# # for n in (1,6,7,8,-5,10): # we loop through a tuple
# #     print(n)
# #     
# # 