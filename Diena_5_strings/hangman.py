# Arna risinajums 2. uzd pilnais
my_text = input(
    "ievadiet tekstu (bez pieturzīmēm, lieliem/maziem burtiem nav nozīmes): ")
if all(x.isalpha() or x.isspace() for x in my_text) and not my_text.isspace():
    my_text = my_text.lower()
    hidden_text = ""
    for c in my_text:
        if c == " ":
            hidden_text = hidden_text + " "
        else:
            hidden_text = hidden_text + "*"
    # outputs 80 blank lines after plain text input / before hidden text output ;-)
    print("\n" * 80 + hidden_text)
    guess_text = hidden_text
    a = 1
    a_limit = 3
    while a <= a_limit:
        letter = input(f"ievadi meklējamo burtu ({a}. burts no {a_limit}): ")
        if letter.isalpha() and len(letter) == 1:
            #    print(my_text.index(letter))
            i = 0
            for c in my_text:
                if c == " ":
                    guess_text = guess_text[:i] + " " + guess_text[i+1:]
                elif c == letter:
                    guess_text = guess_text[:i] + letter + guess_text[i+1:]
                # else:
                #    guess_text = guess_text + str(i) + ":" + "*"
                i += 1
            print(guess_text)
            if "*" in guess_text:
                a += 1
            else:
                print("Uzminēji!")
                exit()
        else:
            print("Nekorekta ievade!")
    while True:
        my_guess = input(
            "tagad mēģini uzminēt tekstu (tev ir tikai viens mēģinājums): ")
        if all(x.isalpha() or x.isspace() for x in my_guess):
            my_guess = my_guess.lower()
            if my_guess == my_text:
                print("Uzminēji!")
            else:
                print(f"Garām! Pareizā atbilde ir: \"{my_text}\"")
            break
        else:
            print("Nekorekta ievade!")
else:
    print("Nekorekta ievade!")
