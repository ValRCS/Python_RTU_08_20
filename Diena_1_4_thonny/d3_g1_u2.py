alga = float(input("Kāda ir jūsu alga? "))
stazs = int(input("Cik pilnus gadus esat nostrādājis uznēmumā? "))
 
if stazs > 2:
    g_virs = stazs-2
    proc = alga*0.15
    bonus = round(g_virs*proc, 2)
    print(f"Jūsu bonuss sastāda {bonus} Euro")
else:
    print("Jums šogad bonus vēl nepienākas")