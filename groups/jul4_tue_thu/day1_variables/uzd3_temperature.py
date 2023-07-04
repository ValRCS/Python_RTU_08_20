# 3. Uzdevums
celsium = float(input("Please enter temperature in Celsium: "))
farenheit = 32 + celsium * (9/5)
print(f"Temperature {celsium} ℃ in Farenheit is {farenheit:.1f} ℉")
print(f"{celsium:.2f} {chr(176)}C ir {farenheit:.2f} °F pēc fārenheita.")
print(chr(176))
print(chr(257)) # ā
print(chr(4852)) # some symbol in some language
print(chr(128000)) # some Emoji
# we also have a way back for single characters
print(ord("🐀"))
print(ord("ā"))