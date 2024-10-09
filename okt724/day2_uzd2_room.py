# 2.uzdevums

ISTABAS_PLATUMS = float(input("Lūdzu ievadi istabas platumu: "))
ISTABAS_AUGSTUMS = float(input("Lūdzu ievadi istabas augstumu: "))
ISTABAS_GARUMS = float(input("Lūdzu ievadi istabas garumu: "))

TELPAS_TILPUMS = ISTABAS_PLATUMS * ISTABAS_AUGSTUMS * ISTABAS_GARUMS
print(f"Telpas tilpums ir {TELPAS_TILPUMS} m³!")
# we can output formatted numbers without changing the value
# we will output to 2 digit precision here
print(f"Telpas tilpums ir {TELPAS_TILPUMS:.2f}!")
# so 10 digits including comma total and 4 after comma rest should be padding
print(f"Telpas tilpums ir {TELPAS_TILPUMS:10.4f}!")
# here we create new variable
volume = round(TELPAS_TILPUMS, 2)
print(f"Telpas tilpums ir {volume}!")
