#2
# Ievadiet eglītes augstumu
# Izdrukājiet eglīti:
# Piem. augstums == 3 
#   *
#  *** 
# *****
#print(" "*10+"*"*6)
while True:
    height_input = input("Ievadiet eglītes augstumu: ")
    try:
        height = int(height_input)
        break
    except ValueError:
        print("Ievadītais teksts nav skaitlis. Lūdzu ievadiet skaitli!")
#         continue # not required

# t = "🌳"  #will have spacing issues
# would need space as well
t = "*"
space = " "
for i in range(height):
    print(space*(height-i-1) + t*(2*i+1))