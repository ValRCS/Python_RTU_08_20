text = input("Ievadiet tekstu: ")
new_text = ""
for c in text:
    if c != " ":
        new_text += "*"
    else:
        new_text += " "
print(new_text)

first_char = input("Ievadiet burtu: ")
for c in text:
    if c != " " and c != first_char:
        c = "*"
    print(c, end="")

# import getpass
# word = getpass.getpass(prompt="Spēlētāj Nr.1 - ievadiet minamo vārdu: ")
# new_word = ""
# for i in word:
#     if i != " ":
#         new_word += " * "
#     else:
#         new_word += " _ "
# print(new_word)
 
# print ("Spēlētāj Nr.2 - izvēlaties burtus!")
 
# guesses = ""
 
# turns = 7 #gājienus var samainīt, 7 testam, var ielikt input
 
# while turns > 0:
#     failed = 0
#     for letter in word:
#         if letter in guesses:
#             if letter == " ":
#                 print("| |", end="")
#             else:
#                 print(letter, end=" ") #kā iebāzt space, lai vienkārši un korekti izskatītos?
#         else:
#             print(" * ", end= "")
#             failed += 1
#      if failed == 0:
#         print(" Jūs vinnējāt! ")
#         print("Atmināmais vārds bija: ", word, end="")
#         break
#     guess = input(" Ievadiet jaunu burtu: ")
#     guesses += guess
 
#     if guess not in word:
 
#         turns -= 1
 
#         print("Nepareizi!", "Jums palika", + turns, "gājieni")
 
#         if turns == 0:
#             print("Jūs zaudējāt ;( ", "Pareizais vārds bija: ", word)