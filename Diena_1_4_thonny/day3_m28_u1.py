# t = int(input("Lūdzu norādiet savu temperatūru: "))
# print("Vai nav par aukstu?" if t < 35 else ("Iespējams drudzis!" if t > 37 else "Viss kārtībā!"))

# 1.uzdevums
temp = float(input("Kāda ir tava temperatūra?  :"))
if temp < 35:
    print("Nav par aukstu?")
elif 35 <= temp <= 37:
    print("Viss kartībā!")
else: # temp > 37
    print("Iespējams drudzis!")