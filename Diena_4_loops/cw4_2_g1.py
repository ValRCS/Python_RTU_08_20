height: int = int(input('enter height: '))
# Standard tree
for line in range(height):
    for space in range(height-line):
        print(" ", end="")
    for star in range(2*line+1):
        print("*", end="")
    print("")
print('-'*int(2*height+1))
# Python like tree
for line in range(height):
    print(" " * (height-line-1), "*" * int(2*line+1))


# h = int(input("Ievadiet eglites augstumu (naturāls skaitlis!): "))
# for i in range(h):
#     print(" " * (h-i-1),"*" * (i * 2 + 1), sep="")
# 
# high=int(input("Ievādiet egles augstumu - "))
# atstarpe=1
# while atstarpe<=high:
#     print(" "*(high-atstarpe)+"*"*(atstarpe*2-1))
#     atstarpe+=1