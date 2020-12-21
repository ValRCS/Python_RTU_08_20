# n = int(input("Tree height? "))
# for i in range(1, n+1):
#     print("*"*i)
    
tree = int(input('Write height of X-mas tree: '))
for i in range(1, tree + 1):
    print(" " * (tree - i) + "*" * (2*i - 1))