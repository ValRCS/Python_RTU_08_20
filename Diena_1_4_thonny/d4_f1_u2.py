# 2. Eglīte
# Ievadiet eglītes augstumu
# Izdrukājiet eglīti:
# Piem. augstums == 3
# Izdruka būtu:
#   *
#  ***
# *****
# Piezīme: atceramies, ka vairākus simbolus var izdrukāt piemēram šādi: print(" "*10+"*"*6)
height = int(input("Ievadi egles augstumu: "))
for num in range(height):
    print(" "*(height-num)+"*"*(1 + 2*num))
