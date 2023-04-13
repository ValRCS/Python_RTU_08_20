# Uzdevums 2
input_text = input("Ievadiet tekstu: ")
cover_text = ""
for letter in input_text:
    if letter == " ":
        cover_text += " "
    else:
        cover_text += "*"
print(cover_text)
 
symbol = input("Ievadiet simbolu: ")
new_text = ""
# for i in range(len(input_text)):
#     if input_text[i].lower() == symbol:
#         new_text += input_text[i]
#     elif input_text[i] == " ":
#         new_text += " "
#     else:
#         new_text += "*"
for c in input_text:
    if c.lower() == symbol:
        new_text += c
    elif c == " ":
        new_text += " "
    else:
        new_text += "*"
print(new_text)