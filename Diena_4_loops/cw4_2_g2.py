n = int(input("Ievadiet eglites augstumu "))
i = 1
a = 1
space = n
while i <= n:
    space = space - 1
    if i <= 1:
        print(" "*space+"*")
    else:
        a = a + 2
        print(" "*space+"*"*a)
    i = i + 1


# while True:
#     try:
#         height = int(input("Insert pine's height in full meters: "))
#         break
#     except ValueError:
#         print("Not height in meters!")
#         
# for n in range(1,height+1):
#     centering = height-n
#     branches_width = 2*n-1
#     print(" "*(centering)+"*"*(branches_width))
# 


# n= int(input("how tall"))
# e=0
# while n>0:
#     print(" "*(n-1)+"*"*(1+e*2))
#     n-=1
#     e+=1