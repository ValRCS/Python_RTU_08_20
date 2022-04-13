# #Nr.2
# char = "*"
# guess_me = input("Please write randm word!")
# # hide_me = len(guess_me)*"*" # TODO add empty spaces
# hide_me = ""
# for c in guess_me:
#     if c == " ":
#         hide_me += " "
#     else:
#         hide_me += char
# print(hide_me)

 
# guess = input("Please write a letter!")

# answer = ""
# for x in guess_me:
#     if x == guess:
#         answer += guess
#     else:
#         answer += char
 
# print(answer)
def uzdevums_2():
    """
    Lietotājs (pirmais spēlētājs) ievada tekstu.
    Tiek izvadītas tikai zvaigznītes burtu vietā. Pieņemsim, ka cipari nebūs, bet atstarpes gan var būt
    Lietotājs(tātad otrs spēlētājs) ievada simbolu.
    Ja burts ir tad tas burts attiecīgajās vietās tiek parādīts, visi pārējie burti paliek par zvaigznītēm.
    Kartupeļu lauks -> ********* *****
    ievada a -> *a****** *a***
    """

    def valid_char(char: int) -> bool:
        """
        :param char: ASCII table Python char code
        :return: True - ja parametrs char IR latiņu A-Z, a-z vai atstarpe
                    False - ja parametrs char NAV latiņu A-Z, a-z vai atstarpe
        """
        return char == 32 or (64 < char < 91) or (96 < char < 123)


    err_txt = "Tekstam jābūt vismaz no viena simbola. Mēģiniet velreiz!"
    while True:
        try:
            user1_input = input(f"Lūdzu, ievadiet tekstu no latiņu būrtiem A-Z, a-z (var izmantot atstarpes): ")
            if user1_input:  # Sākumā pārbaudam, vai lietotajs vispār ko ievadījis
                user1_input_correct = True  # sākumā pieņemsim, ka visi simboli ir atļautie
                for char in user1_input:  # Tagad pārbaudam, vai visi simboli TIEŠAM ir atļautie
                    if not valid_char(ord(char)):
                        print(f'Simbols "{char}" ir neatļauts!')  # Rādam neatļauto simbolu
                        user1_input_correct = False  # Veiksim pārbaudi līdz galam, parādīsim visus nepareizus simbolus
                if not user1_input_correct:  # Ja ievadā tika konstatēti neatļautie simboli
                    print("Mēģiniet velreiz!")
                    continue  # Sākam lietotaja ievadu no sākuma

                #Lietotajs nr.1 ir ievadījis korektu tekstu (ievadu). Sākam spēli.
                print("Ievadītais teksts ir korrekts. Sākam speli!")
                user1_input_mask = len(user1_input) * "*"
                while user1_input_mask.find("*") > -1:  # kamer ir kaut viens neatminēts simbols
                    print(f"Pāslaik lietotāja Nr.1 ievadītais teksts izskatas šādi: {user1_input_mask}")
                    user2_input_char = input(f"Lūdzu ievadiet VIENU simbolu A-Z, a-z vai atstarpi: ")
                    if len(user2_input_char) != 1 or not valid_char(ord(user2_input_char)):
                        continue  # User2 ievadīja ENTER, vairakus vai neatļautos simbolus, atkārtosim ievadu

                    # User2 ievadītais simbols ir korrekts
                    find_flag = False  # Flag priekš simbola uzminēšanas/neuzminēšanas
                    for i in range(len(user1_input)):
                        if user1_input[i] == user2_input_char:
                            user1_input_mask = user1_input_mask[:i] + user2_input_char + user1_input_mask[i + 1:]
                            print(f'Labi! Simbols "{user2_input_char}" IR tekstā!')
                            find_flag = True
                    if not find_flag:
                        print(f'Hi-hi! Simbola "{user2_input_char}" NAV tekstā!')

                print(f"Apsveicu! Spēle ir beigusies. Lietotāja Nr.1 ievadītais teksts bija: {user1_input}")
                break
        except ValueError:
            print(err_txt)

uzdevums_2()
