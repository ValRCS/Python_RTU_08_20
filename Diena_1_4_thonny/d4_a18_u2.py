# height = int(input('Please enter the hight of of a Christmass tree: '))
# width = 1
# for level in range(1,height+1):
#     spacer = height - level
#     print(' '*spacer + '^'*width)
#     width += 2

# spruce_height = int(input("Enter spruce height: "))
# if spruce_height <= 0:
#      print("There's no spruce!")
# else:
#      for iter in range (1, spruce_height + 1):
#          spruce_space = round(spruce_height-iter // 2)
#          print (" " * spruce_space + "*" *iter)

# a = int(input("Tell me the height of your christmass tree: "))
# for b in range(1, a+1, 2):
# #     if b % 2 > 0:
#     print(" "*a+"*"*b)
#     a -= 1
#     b += 1

row = int(input("\nIevadiet eglītes augstumu: "))
 
for n in range(row):
    print(" "*(row-n-1)+"*"*((n*2)+1))
