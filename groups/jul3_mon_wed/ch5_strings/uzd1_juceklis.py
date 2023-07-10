lietotajs=input("Ievadiet savu vārdu ")
reverse_cap = lietotajs[::-1].capitalize() # could argue for title() here as well
first_cap = lietotajs[0].upper() # could use capitalize or even title for single character
print(lietotajs[::-1].capitalize(), ", pamatīgs juceklis, vai ne", lietotajs[0].upper(), "?"))
# if we needed to save the answer to variable
new_text = f"{reverse_cap}, pamatīgs juceklis, vai ne {first_cap}?"
print(new_text)
# same with string concatenation
same_text = reverse_cap + ", pamatīgs juceklis, vai ne " + first_cap + "?"
print(same_text)