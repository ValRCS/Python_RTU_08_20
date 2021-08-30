# height = int(input("Enter Christmas tree height: "))
height = 15
i = 0
while i < height:
    print(" "*(height-i) + "*"*(1 + i + i))
    i += 1
print("Beautiful! \U0001F600")

# height = 13
# level = height*2 - 1
# for i in range (1, level+1, 2):
#     j = "*" * i
#     print(j.center(level))

# # height = int(input("Ievadiet eglītes augstumu "))
# height = 4
# i = 0
# for i in range(height):
# #     print(" "*height + "*"*(i+1))
#     print(" "*(height-i),"*"*(2*i+1))
#     
#     ## Uzdevums-2
# # levels = int(input("Enter number of tree levels: "))
#  
# levels = height
# max_stars = levels * 2 - 1 
# for i in range(levels):
#         stars = (i + 1) * 2 - 1
#         spaces = int((max_stars - stars) / 2)
#         print(' '*spaces + '*'*stars + ' '*spaces)
# 