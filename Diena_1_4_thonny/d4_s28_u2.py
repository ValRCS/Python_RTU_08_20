#2 Eglite
height = int(input("Lūdzu ievadiet egles augstumu: "))
for n in range(height):
    sym = "*"
    offset = 0
#     if n == 0:
#         sym = "⭐"
#         offset = -1
    print(" "*(height-n-1+offset)+sym*(1 + 2*n))