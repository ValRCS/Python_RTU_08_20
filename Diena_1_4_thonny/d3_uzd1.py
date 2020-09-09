userTemperature = float(input("Izskaties apslimis, kāda Tev temperatūra?"))
lowTemp = 35
highTemp = 37
if userTemperature > highTemp:
    print("Ufff, tad jau Tu esi pārkarsis!")
elif userTemperature < lowTemp:
    print("Hah, tad jau Tu esi vēsais džeks!")
else:
    print("Tad jau viss kārtībā, bet pārbaudīties tomēr aizej!")