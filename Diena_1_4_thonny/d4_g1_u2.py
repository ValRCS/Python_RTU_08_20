# height = input("height? ")
# height = int(height)
# i = 1
# while height>0:
#     print(" "*(height-1),"*"*i," "*(height-1))
#     height -= 1
#     i += 2

tree_height  = int(input("Enter height of the tree in full m:"))
 
for i in range(tree_height+1):
    print(" "*(tree_height-i) + (i*2-1)*"*")