#nedarbojas, ja ir divi vienādi burti un atstarpes vietā arī ir *
text = input("Uzraksti minamo tekstu: ")
text_to_guess = text.lower()  #teksts, kas jāuzmin
text_len = len(text_to_guess)
hidden_text = text_to_guess.replace(text_to_guess, text_len*"*")
print (hidden_text) #aizstāt visus burtus ar *
 
char = str(input("Burta minējums: "))
while char in text_to_guess:
    for c in text_to_guess:
        c = char
        if c in text_to_guess:
            print(f"Pareizi! Tekstā ir burts {char}")
            good_char = text_to_guess.index(c) #iegūts burta index (int)
            hidden_text[good_char].replace("*", c )  #burtu ieliek zvaigznes vietā
            new_text = hidden_text[:good_char]+hidden_text[good_char].replace("*",c)+hidden_text[good_char+1:]
            print(new_text)
            hidden_text = new_text
        else:
            print(f"Burts {char}  tekstā nav")
 
        char = str(input("Nākošais burta minējums: "))
if text_to_guess == new_text:
    print("Apsveicu! Tu uzminēji visus burtus!")





# ######## task2 ############
# user_text = input("Ievādiet tekstu: ")
# output_text = user_text
# for i in user_text:
#     if i != " ":
#         output_text = output_text.replace(i,"*")
# print(output_text)
# symbol = input("Atmini burtu: ")
# output_text = user_text
# for i in user_text:
#     if i == symbol:
#         output_text = output_text.replace(i,symbol)
#     elif i != " ":
#         output_text = output_text.replace(i,"*")
# print(output_text)