while True:
    s = input("Kā jūs sauc? ")
    if len(s) >= 2:
        break
print(f"{s.lower()[::-1].capitalize()}, pamatigs juceklis vai ne {s[0]}")