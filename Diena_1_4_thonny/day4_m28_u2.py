print("2.Uzdevums_Eglīte")
# Ievadiet eglītes augstumu
 
# height = int(input("Egles augstums"))
# blanks = 1 + 2*height
# symbols = 1
# for n in range(0, height):
#    print(" "*blanks+"*"*symbols, end="\n")
#    blanks -= 1
#    symbols += 2

h = int(input("Augstums: "))
for n in range(h):
    print(' '*(h - n) + '*'+'*'*2*n)
    print(' '*(h - n) + '*'*(1+2*n))
print()