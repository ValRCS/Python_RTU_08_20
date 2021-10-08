# userInput = int(input("Ievadiet rindu skaitu: "))
 
# row = 0
# while(row < userInput):
#     row += 1
#     spaces = userInput - row
 
#     spaces_counter = 0
#     while(spaces_counter < spaces):
#         print(" ", end ='')
#         spaces_counter += 1
 
#     num_stars = 2*row-1
#     while(num_stars > 0):
#         print("*", end ='')
#         num_stars -= 1
 
#     print()

# 2. Eglīte
# Ievadiet eglītes augstumu
# Izdrukājiet eglīti:
# Piem. augstums == 3
# Izdruka būtu:
#   *
#  ***
# *****
# Piezīme: atceramies, ka vairākus simbolus var izdrukāt piemēram šādi: print(" "*10+"*"*6)
# n = input("Ievadiet eglītes augstumu n: ")
# n = int(n)
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*(i*2-1))
# for i in range(n): # so we start at 0 and go until n but not including n
#     print(" "*(n-i-1)+"*"*(i*2+1))

# sk=int(input("Ievadi eglītes augstumu (veselu skaitli)!"))
# i=1
# for i in range(sk+1):
#    print(" " * (sk-i) + "* " * i)
# print("Priecīgus Ziemassvētkus!")