# 1. uzdevums #
temp = float(input("Cik Jums šobrīd ir temperatūra? "))
if temp < 35:
    print("Vai nav par aukstu?")
elif temp > 37:
    print("Iespējams drudzis!")
else: # 35 to 37 inclusive
    print("Viss kārtībā!")