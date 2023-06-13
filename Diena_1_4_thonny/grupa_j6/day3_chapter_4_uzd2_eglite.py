#2. Eglīte
#Ievadiet eglītes augstumu
#Izdrukājiet eglīti:
 
#Piem. augstums == 3
#Izdruka būtu:
#  *
# ***
#*****
 
 
eglites_augstums=None

while eglites_augstums is None:
    try:
        eglites_augstums = int(input(f"Eglītes augstums 1+ ?"))
        if eglites_augstums <= 0:
            eglites_augstums = None
            raise ValueError
    except ValueError:
        print("Lūdzu ievadīt eglītes augstumu ar cipariem ")
    
# at this stage
# we are guaranteed positive integer for eglites_augstums
for i in range(0,eglites_augstums):
    zvaigznes=1+i*2 # so our stars will increase by two
    spaces = eglites_augstums - i - 1 # so spaces will decrease by 1 each cycle
    print(f"{' '*spaces}{'*'*zvaigznes}{' '*spaces}")
    
i=1
j=-1 #zvaigznisu skaits
k=0 #atstarpju skaits
# number = int(input("Lūdzu ievadi egles augstumu "))
while i<=eglites_augstums:
    k=eglites_augstums-i
    j+=2 # so increasing number of stars by 2
    i+=1
    print(k*" "+j*"*")
print("end code")
#Piezīme: atceramies, ka vairākus simbolus var izdrukāt piemēram šādi: print(" "*10+"*"*

# without * for strings we would have had to write two nested loops
# inner loop would print the spaces and stars
