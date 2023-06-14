# 1. uzdeuvums
 
text = input("Lūdzu ievadiet tekstu: ")
reversed_text = text[::-1]
cap_text = reversed_text.capitalize()
print(f"{cap_text}, pamatīgs juceklis, vai ne {text[0].upper()}?")