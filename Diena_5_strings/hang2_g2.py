while True:
    print('Pirmais lietotajs -\n Ievadiet  tekstu:')
    text = str(input())
    if text.isnumeric() == False:  # isnumeric() var lietot try except vietā
        text = text.lower()
        break
    else:
        print("Nav pareizi!")
 
secret_text = text
for letter in range(0,len(secret_text)):
    print(secret_text[letter])
    if ord(secret_text[letter]) == 32:
        continue
    else:
        print("burts seit")
        secret_text = secret_text.replace(secret_text[letter], "*")
 
 
print(f"Pirma lietotaja vards ir:\n {secret_text}!")
 
while True:
    print('Otrais lietotajs -\n Ievadiet  simbolu:')
    symbol = str(input())
    if text.isnumeric() == False and len(symbol) == 1:  # isnumeric() var lietot try except vietā
        break
    else:
        print("Nav pareizi vai simbolu skaits ir par lielu!")
current_text = secret_text
for s_letter in range(0, len(text)):
    if ord(text[s_letter]) != ord(symbol):
        continue
    else:
        current_text = current_text[:s_letter]+ symbol + current_text[s_letter+1:]
print(f"Rezultats: {current_text}")