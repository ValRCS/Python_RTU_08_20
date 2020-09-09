temp = int(input("Kāda Tev ir temperatūra? "))

a = 35

b = 36

c = 37
if temp < a:
    print("nav par aukstu")
# if temp == a or temp == b or temp == c:
if temp in (a,b,c):
    print("viss kārtībā")
if temp > c:
    print("iespējams drudzis")
