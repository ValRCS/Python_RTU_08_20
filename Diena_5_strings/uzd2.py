name = input("Ievadi tekstu: ")
just_stars = ""
for c in name:
    if c == " ":
        just_stars += " "
    else:
        just_stars += "*"
print(just_stars)
letter = input("Ievadi simbolu: ")

encrypted = ""
for c in name:
    if c in [" ", letter.lower(), letter.upper()]:
        encrypted += c
    else:
        c = "*"
        encrypted += c
print(encrypted)
