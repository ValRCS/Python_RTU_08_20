#2. Eglīte
#Ievadiet eglītes augstumu
#Izdrukājiet eglīti:
#Piem. augstums == 3
#Izdruka būtu:
#  *
# ***
#*****
#Piezīme: atceramies, ka vairākus simbolus var izdrukāt piemēram šādi: print(" "*10+"*"*6)
 
# stavi = int(input("cik stāvus eglītei šogad? : "))
#  
# for n in range(1,stavi+1):
#     print(" "*(stavi-n)+"*"*(2*n-1))

############
# Task Nr.2
############
sym = "*"
# sym = "🌲" # not good choice not monospace
# sym = "#"
is_valid = False
while not is_valid:
    try:
        height = int(input("Enter height (Number) of a tree: "))
        is_valid = True
    except ValueError:
        print("Enter NUMBER")

line_width = 1

# if is_valid: needed if we had more validation after number entry
for n in range(height):
    spaces = height - n - 1
    print(" " * spaces + sym * line_width + " " * spaces)
    line_width += 2
