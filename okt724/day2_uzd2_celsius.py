# 3. uzd
PRECISION = 3
celsium = float(input("Kāda ir temperatūra °C ℃ pēc Celsija?"))
farenheit = round(32 + celsium*(9/5), PRECISION)
print(f"Vai zināji, ka {celsium} grādi pēc Farenheita skalas būs {farenheit} grādi?")