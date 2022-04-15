a=input("Kāda Jums ir temperatūra šodien?....")
b=input("Kāds ir Jūsu vārds....?")
# b=str(b) lieka rinda
a=int(a)
if a<35:
    print(f"{b} vai nav par aukstu?")
if a >= 35 and a <= 37:
    print(f"{b} viss kārtībā")
if a > 37:
    print(f"{b} iespējams drudzis")

   
print("this will always happen no matter the value")
