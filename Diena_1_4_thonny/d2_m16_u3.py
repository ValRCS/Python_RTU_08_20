#3. uzd. 
celsijs = float(input(f'Ievadi temperatūru Celsija grādos ℃ '))
farenheits = 32 + celsijs*(9/5)
rounded_farenheit = round(farenheits, 2)

# print(f'Ja Latvijā ir {celsijs} grādu pēc Celsija,\n tad Amerikā - {rounded_farenheit} grādu pēc Fārenheita')
print(f"""Ja Latvijā ir ℃ {celsijs} grādu pēc Celsija,
tad Amerikā - ℉ {rounded_farenheit} grādu pēc Fārenheita""")
print(f"℉ {farenheits:.2f} {farenheits:.4f}")
print(f"℉ {farenheits:10.2f}") # so 10 spaces allowed for our value with 2 required after comma