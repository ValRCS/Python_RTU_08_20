#Task 02
 
# user_input = int(input("Please enter tree height " ))
#  
# i = 1  # line number
# n = 1  # Stars number generator
#  
# while i <= user_input:
#     print(" " * (user_input - i) + "*" * n)
#     i += 1
#     n += 2
#  
# print()

# 2. uzdevums
# tree = int(input("Tree (from 10-30)*: "))
# for x in range(1, tree*2+1, 2):
#     s = '*' * x
#     print(s.center(30))

# 2. uzdevums
h = input("Whats is a tree height?")
h = int(h)
for i in range(h):
    print(" "*(h-i-1)+"*" * (2*i+1))

