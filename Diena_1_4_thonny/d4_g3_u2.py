heigth = int(input("Enter the height of the Christmas tree: "))
for i in range(1, heigth+1):
    print(" "*(heigth - i), "*"*(2*i - 1))



# tree_height = input("Ievadiet egles augstumu: ")
# tree_height = int(tree_height)
# free = tree_height-1
# branches = 1
# while tree_height != 0 :
# #     for i in range(free):
# #         print(' ', end="")
# #     for i in range(branches):
# #         print('*', end="")
# #     print()
#     print(" "*free+"*"*branches)
#     tree_height -= 1
#     free -= 1
#     branches += 2