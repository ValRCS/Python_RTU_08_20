text = input("Tekstu ludzu")
if "nav slikts" in text:
    new_text = text.replace("nav slikts", "ir labs")
    print(new_text)
else:
    print(text)
# atrast indexus kur sāks nav un kur sākas slikts (no labas labāk)
# jasalipina kopā jauns strings
