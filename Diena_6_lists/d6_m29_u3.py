def uzdevums_3():
    """
    Lietotājs ievada teikumu.
    Izvadam visus teikuma vārdus apgrieztā formā.
    Alus kauss -> Sula ssuak
    PS Te varētu noderēt split un join operācijas.
    """
    err_txt = "Teikumam jābūt vismaz no diviem vārdiem. Mēģiniet velreiz!"
    while True:
        try:
            user_input = input(f"Lūdzu, ievadiet teikumu: ")
            if user_input:
                print(" ".join(x[::-1] for x in user_input.lower().split()).capitalize())
                break
        except ValueError:
            print(err_txt)

# uzdevums_3()

#3. reversed names
sentence = input("Please enter a sentence: ")
words = sentence.split()
print(words)
rev_sent=[word[::-1] for word in words] # list comprehension
# same as above line
also_reverse_sentence = []
for word in words:
    also_reverse_sentence.append(word[::-1])
    # we could do more stuff here
print(also_reverse_sentence)

print(rev_sent)
joint_sent=" ".join(rev_sent)
print(joint_sent.capitalize())